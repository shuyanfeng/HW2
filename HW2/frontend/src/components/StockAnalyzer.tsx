import React, { useState } from 'react';
import axios from 'axios';
import './StockAnalyzer.css';

interface AnalysisData {
  symbol: string;
  current_price: number;
  price_change: number;
  price_change_pct: number;
  analysis: {
    bullish_views: string[];
    bearish_views: string[];
  };
  last_updated: string;
}

const StockAnalyzer: React.FC = () => {
  const [symbol, setSymbol] = useState('');
  const [loading, setLoading] = useState(false);
  const [analysis, setAnalysis] = useState<AnalysisData | null>(null);
  const [error, setError] = useState('');

  const handleAnalyze = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!symbol.trim()) return;

    setLoading(true);
    setError('');
    setAnalysis(null);

    try {
      const response = await axios.get(`/api/analyze/${symbol.toUpperCase()}`);
      setAnalysis(response.data);
    } catch (err: any) {
      setError(err.response?.data?.error || 'An error occurred while analyzing the stock');
    } finally {
      setLoading(false);
    }
  };

  const formatPrice = (price: number) => {
    return `$${price.toFixed(2)}`;
  };

  const formatChange = (change: number, changePct: number) => {
    const sign = change >= 0 ? '+' : '';
    return `${sign}${change.toFixed(2)} (${sign}${changePct.toFixed(2)}%)`;
  };

  return (
    <div className="stock-analyzer">
      <form onSubmit={handleAnalyze} className="search-form">
        <div className="input-group">
          <input
            type="text"
            value={symbol}
            onChange={(e) => setSymbol(e.target.value.toUpperCase())}
            placeholder="Enter stock symbol (e.g., AAPL, MSFT, GOOGL)"
            className="symbol-input"
            disabled={loading}
          />
          <button type="submit" className="analyze-btn" disabled={loading || !symbol.trim()}>
            {loading ? 'Analyzing...' : 'Analyze Stock'}
          </button>
        </div>
      </form>

      {error && (
        <div className="error-message">
          <h3>❌ Error</h3>
          <p>{error}</p>
        </div>
      )}

      {analysis && (
        <div className="analysis-results">
          <div className="stock-header">
            <h2>{analysis.symbol}</h2>
            <div className="price-info">
              <span className="current-price">{formatPrice(analysis.current_price)}</span>
              <span className={`price-change ${analysis.price_change >= 0 ? 'positive' : 'negative'}`}>
                {formatChange(analysis.price_change, analysis.price_change_pct)}
              </span>
            </div>
            <p className="last-updated">
              Last updated: {new Date(analysis.last_updated).toLocaleString()}
            </p>
          </div>

          <div className="analysis-grid">
            <div className="analysis-section bullish">
              <h3>🟢 Bullish Views</h3>
              <ul>
                {analysis.analysis.bullish_views.map((view, index) => (
                  <li key={index}>{view}</li>
                ))}
              </ul>
            </div>

            <div className="analysis-section bearish">
              <h3>🔴 Bearish Views</h3>
              <ul>
                {analysis.analysis.bearish_views.map((view, index) => (
                  <li key={index}>{view}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default StockAnalyzer;

