// import { useState } from 'react';
// import { summarizeVideo } from '../api';  // If api.js is in src/ // Make sure path is correct

// const FileUpload = ({ onFileSelect, isLoading }) => {
//   const [selectedFile, setSelectedFile] = useState(null);

//   const handleFileChange = (e) => {
//     setSelectedFile(e.target.files[0]);
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     if (!selectedFile) return;
    
//     try {
//       const result = await summarizeVideo(selectedFile);
//       console.log("Summary created at:", result.summary_video_path);
//       // Call parent handler if needed
//       if (onFileSelect) onFileSelect(result); 
//     } catch (error) {
//       alert("Error: " + error.message);
//     }
//   };

//   return (
//     <div className="file-upload">
//       <h2>Upload Your Video</h2>
//       <form onSubmit={handleSubmit}>
//         <input
//           type="file"
//           accept="video/*"
//           onChange={handleFileChange}
//           disabled={isLoading}
//           required
//         />
//         <button 
//           type="submit" 
//           disabled={!selectedFile || isLoading}
//         >
//           {isLoading ? 'Processing...' : 'Summarize Video'}
//         </button>
//       </form>
//     </div>
//   );
// };

// export default FileUpload;






import React, { useState } from 'react';  // Added React import

const FileUpload = ({ onFileSelect, isLoading }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [downloadInfo, setDownloadInfo] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
    setDownloadInfo(null);
    setError(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedFile) return;
    
    try {
      const result = await onFileSelect(selectedFile);
      setDownloadInfo(result);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="file-upload">
      <h2>Upload Your Video</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept="video/*"
          onChange={handleFileChange}
          disabled={isLoading}
          required
        />
        <button type="submit" disabled={!selectedFile || isLoading}>
          {isLoading ? 'Processing...' : 'Summarize Video'}
        </button>
      </form>

      {error && <div className="error">{error}</div>}

      {downloadInfo && (
        <div className="download-section">
          <h3>Your summary is ready!</h3>
          <a
            href={downloadInfo.downloadUrl}
            download={downloadInfo.filename}
            className="download-btn"
          >
            Download Summary
          </a>
        </div>
      )}
    </div>
  );
};

export default FileUpload;