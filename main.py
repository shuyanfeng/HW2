from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import openai
import os
import requests
from datetime import datetime, timedelta
import json

app = Flask(__name__, static_folder='..', static_url_path='')
CORS(app)

# Set Google Gemini API configuration
GEMINI_API_KEY = 'AIzaSyD2Kx9FgTyHpTX5ZUOsCpy6DaC4fTqYGU8'  # Replace with your actual Gemini API key
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta"

def get_stock_data(symbol):
    """Generate mock stock data for demonstration"""
    # For demo purposes, generate realistic-looking stock data
    import random
    import math
    
    # Base price for different symbols
    base_prices = {
        'AAPL': 150.0,
        'MSFT': 300.0,
        'GOOGL': 2500.0,
        'TSLA': 200.0,
        'AMZN': 3000.0,
        'META': 300.0,
        'NVDA': 400.0,
        'NFLX': 400.0
    }
    
    base_price = base_prices.get(symbol.upper(), 100.0)
    
    # Generate 30 days of mock data
    recent_data = []
    current_price = base_price
    
    for i in range(30):
        # Add some realistic price movement
        change_pct = random.uniform(-0.05, 0.05)  # ±5% daily change
        current_price = current_price * (1 + change_pct)
        
        # Generate OHLC data
        high = current_price * random.uniform(1.0, 1.03)
        low = current_price * random.uniform(0.97, 1.0)
        open_price = current_price * random.uniform(0.98, 1.02)
        close_price = current_price
        
        # Generate volume
        volume = random.randint(1000000, 10000000)
        
        recent_data.append({
            'date': (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d'),
            'open': round(open_price, 2),
            'high': round(high, 2),
            'low': round(low, 2),
            'close': round(close_price, 2),
            'volume': volume
        })
    
    return recent_data

def analyze_stock_with_ai(symbol, stock_data):
    """Use OpenAI to analyze stock data and provide bullish/bearish views"""
    
    if not stock_data:
        return {
            "bullish_views": ["Insufficient data for analysis"],
            "bearish_views": ["Insufficient data for analysis"]
        }
    
    # Prepare data summary for AI
    latest_price = stock_data[0]['close']
    price_change = latest_price - stock_data[1]['close']
    price_change_pct = (price_change / stock_data[1]['close']) * 100
    
    # Calculate some basic technical indicators
    prices = [day['close'] for day in stock_data]
    avg_volume = sum(day['volume'] for day in stock_data) / len(stock_data)
    
    # Simple moving averages
    sma_5 = sum(prices[:5]) / 5
    sma_20 = sum(prices[:20]) / 20
    
    data_summary = f"""
    Stock Symbol: {symbol}
    Current Price: ${latest_price:.2f}
    Price Change: ${price_change:.2f} ({price_change_pct:.2f}%)
    5-day SMA: ${sma_5:.2f}
    20-day SMA: ${sma_20:.2f}
    Average Volume: {avg_volume:,.0f}
    
    Recent Price History (last 10 days):
    """
    
    for i, day in enumerate(stock_data[:10]):
        data_summary += f"Day {i+1}: ${day['close']:.2f} (Vol: {day['volume']:,})\n"
    
    prompt = f"""
    As a professional financial analyst, analyze the following stock data and provide exactly 3 bullish views and 3 bearish views for {symbol}.
    
    {data_summary}
    
    Please provide your analysis in the following JSON format:
    {{
        "bullish_views": [
            "Bullish view 1 with specific reasoning",
            "Bullish view 2 with specific reasoning", 
            "Bullish view 3 with specific reasoning"
        ],
        "bearish_views": [
            "Bearish view 1 with specific reasoning",
            "Bearish view 2 with specific reasoning",
            "Bearish view 3 with specific reasoning"
        ]
    }}
    
    Make each view specific, actionable, and based on the data provided. Include technical analysis, volume patterns, and price action insights.
    """
    
    try:
        # Use Google Gemini API
        headers = {
            "Content-Type": "application/json"
        }
        
        # Prepare the prompt for Gemini
        system_prompt = "You are a professional financial analyst with expertise in technical and fundamental analysis. Always respond with valid JSON format."
        full_prompt = f"{system_prompt}\n\n{prompt}"
        
        data = {
            "contents": [{
                "parts": [{
                    "text": full_prompt
                }]
            }],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": 800,
                "topP": 0.8,
                "topK": 10
            }
        }
        
        response = requests.post(
            f"{GEMINI_BASE_URL}/models/gemini-2.5-flash-lite:generateContent?key={GEMINI_API_KEY}",
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            analysis_text = result['candidates'][0]['content']['parts'][0]['text']
        else:
            raise Exception(f"Gemini API request failed with status {response.status_code}: {response.text}")
        
        # Try to parse JSON response
        try:
            analysis = json.loads(analysis_text)
            return analysis
        except json.JSONDecodeError:
            # Fallback if AI doesn't return proper JSON
            return {
                "bullish_views": [
                    "Strong upward momentum based on recent price action",
                    "Volume patterns suggest institutional interest",
                    "Technical indicators show bullish divergence"
                ],
                "bearish_views": [
                    "Potential resistance at current price levels",
                    "Volume decline indicates weakening momentum",
                    "Technical indicators show overbought conditions"
                ]
            }
            
    except Exception as e:
        print(f"Error in AI analysis: {e}")
        print(f"Gemini API Key: {GEMINI_API_KEY[:20]}...")
        print(f"Base URL: {GEMINI_BASE_URL}")
        return {
            "bullish_views": ["AI analysis temporarily unavailable"],
            "bearish_views": ["AI analysis temporarily unavailable"]
        }

@app.route('/api/analyze/<symbol>', methods=['GET'])
def analyze_stock(symbol):
    """Analyze a stock symbol and return bullish/bearish views"""
    try:
        # Fetch stock data
        stock_data = get_stock_data(symbol.upper())
        
        if not stock_data:
            return jsonify({
                "error": "Unable to fetch stock data. Please check the symbol and try again.",
                "symbol": symbol.upper()
            }), 400
        
        # Analyze with AI
        analysis = analyze_stock_with_ai(symbol.upper(), stock_data)
        
        return jsonify({
            "symbol": symbol.upper(),
            "current_price": stock_data[0]['close'],
            "price_change": stock_data[0]['close'] - stock_data[1]['close'],
            "price_change_pct": ((stock_data[0]['close'] - stock_data[1]['close']) / stock_data[1]['close']) * 100,
            "analysis": analysis,
            "last_updated": datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            "error": f"An error occurred: {str(e)}",
            "symbol": symbol.upper()
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/')
def serve_index():
    """Serve the main HTML file"""
    return send_from_directory('..', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory('..', path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

