const ResultSection = ({ result, onDownload }) => {
  if (!result) return null;

  return (
    <div className="result-section">
      <h3>Your Summary is Ready!</h3>
      <button onClick={() => onDownload(result.summary_video_path)}>
        Download Summary Video
      </button>
    </div>
  );
};

export default ResultSection;