// src/App.jsx
import React, { useState } from "react";
import UploadForm from "./components/UploadForm";

function App() {
  const [videoURL, setVideoURL] = useState("");

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <h1 className="text-3xl font-bold mb-6">AI Video Summarizer</h1>
      <UploadForm onComplete={setVideoURL} />
      {videoURL && (
        <div className="mt-6">
          <h2 className="text-lg font-semibold mb-2">Summary Video:</h2>
          <video src={videoURL} controls className="max-w-full h-auto" />
        </div>
      )}
    </div>
  );
}

export default App;
