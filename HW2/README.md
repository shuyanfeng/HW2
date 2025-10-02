# Stock Analyzer AI

An AI-powered stock market analysis tool that provides 3 bullish and 3 bearish views for any stock symbol using OpenAI's GPT-3.5-turbo model.

## Features

- 🔍 **Real-time Stock Data**: Fetches live stock data from Alpha Vantage API
- 🤖 **AI Analysis**: Uses OpenAI GPT-3.5-turbo for intelligent market analysis
- 📊 **Bullish & Bearish Views**: Provides 3 specific bullish and 3 bearish perspectives
- 💻 **Modern UI**: Beautiful, responsive React frontend with TypeScript
- 🚀 **Live Deployment**: Ready for production deployment

## Tech Stack

### Backend
- **Flask**: Python web framework
- **OpenAI API**: AI-powered analysis
- **Alpha Vantage API**: Stock market data
- **Flask-CORS**: Cross-origin resource sharing

### Frontend
- **React 18**: Modern React with hooks
- **TypeScript**: Type-safe JavaScript
- **Axios**: HTTP client for API calls
- **CSS3**: Modern styling with gradients and animations

## Setup Instructions

### Prerequisites
- Python 3.11+
- Node.js 16+ (for local development)
- OpenAI API key
- Alpha Vantage API key

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Copy the example file
cp env.example .env

# Edit .env and add your API keys
OPENAI_API_KEY=your_openai_api_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key_here
```

4. Run the Flask server:
```bash
python main.py
```

The backend will be available at `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

### GET /api/analyze/{symbol}
Analyzes a stock symbol and returns bullish/bearish views.

**Parameters:**
- `symbol` (string): Stock symbol (e.g., AAPL, MSFT, GOOGL)

**Response:**
```json
{
  "symbol": "AAPL",
  "current_price": 150.25,
  "price_change": 2.15,
  "price_change_pct": 1.45,
  "analysis": {
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
  },
  "last_updated": "2024-01-15T10:30:00.000Z"
}
```

### GET /api/health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00.000Z"
}
```

## Deployment

### Heroku Deployment

1. Install Heroku CLI
2. Login to Heroku:
```bash
heroku login
```

3. Create a new Heroku app:
```bash
heroku create your-stock-analyzer-app
```

4. Set environment variables:
```bash
heroku config:set OPENAI_API_KEY=your_openai_api_key
heroku config:set ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
```

5. Deploy:
```bash
git add .
git commit -m "Initial deployment"
git push heroku main
```

### Railway Deployment

1. Connect your GitHub repository to Railway
2. Set environment variables in Railway dashboard:
   - `OPENAI_API_KEY`
   - `ALPHA_VANTAGE_API_KEY`
3. Deploy automatically on push

## Getting API Keys

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and add it to your environment variables

### Alpha Vantage API Key
1. Visit [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Add it to your environment variables

## Usage

1. Open the application in your browser
2. Enter a stock symbol (e.g., AAPL, MSFT, GOOGL)
3. Click "Analyze Stock"
4. View the AI-generated bullish and bearish analysis

## Project Structure

```
stock-analyzer-ai/
├── backend/
│   ├── main.py              # Flask application
│   ├── requirements.txt     # Python dependencies
│   └── env.example         # Environment variables template
├── frontend/
│   ├── public/
│   │   └── index.html      # HTML template
│   ├── src/
│   │   ├── components/
│   │   │   ├── StockAnalyzer.tsx    # Main component
│   │   │   └── StockAnalyzer.css    # Component styles
│   │   ├── App.tsx         # Main app component
│   │   ├── App.css         # App styles
│   │   ├── index.tsx       # React entry point
│   │   └── index.css       # Global styles
│   ├── package.json        # Node.js dependencies
│   └── tsconfig.json       # TypeScript configuration
├── Procfile               # Heroku deployment configuration
├── runtime.txt            # Python version specification
└── README.md              # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Disclaimer

This tool is for educational and informational purposes only. It should not be considered as financial advice. Always do your own research and consult with a financial advisor before making investment decisions.

