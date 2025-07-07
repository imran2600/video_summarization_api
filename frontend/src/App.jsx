import React from 'react';
import { useState } from 'react';
import { summarizeVideo, downloadVideo } from './api';
import FileUpload from './components/FileUpload';
import ProgressBar from './components/ProgressBar';
import ResultSection from './components/ResultSection';
import './App.css';

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleFileSelect = async (file) => {
    setIsLoading(true);
    setProgress(0);
    setError(null);
    
    try {
      // Simulate progress (in real app, you might use websockets for real progress)
      const interval = setInterval(() => {
        setProgress((prev) => {
          if (prev >= 90) {
            clearInterval(interval);
            return prev;
          }
          return prev + 10;
        });
      }, 500);

      const response = await summarizeVideo(file);
      clearInterval(interval);
      setProgress(100);
      setResult(response);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app">
      <h1>Video Summarization</h1>
      <p>Upload a video to get a summarized version</p>
      
      <FileUpload onFileSelect={handleFileSelect} isLoading={isLoading} />
      
      {isLoading && <ProgressBar progress={progress} />}
      
      {error && <div className="error">{error}</div>}
      
      <ResultSection result={result} onDownload={downloadVideo} />
    </div>
  );
}

export default App;