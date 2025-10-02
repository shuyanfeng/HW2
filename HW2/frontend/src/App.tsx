import React, { useState } from 'react';
import './App.css';
import StockAnalyzer from './components/StockAnalyzer';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>📈 Stock Analyzer AI</h1>
        <p>Get AI-powered bullish and bearish analysis for any stock</p>
      </header>
      <main>
        <StockAnalyzer />
      </main>
    </div>
  );
}

export default App;

