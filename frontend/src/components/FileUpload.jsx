import { useState } from 'react';

const FileUpload = ({ onFileSelect, isLoading }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setSelectedFile(file);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (selectedFile) {
      onFileSelect(selectedFile);
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
    </div>
  );
};

export default FileUpload;