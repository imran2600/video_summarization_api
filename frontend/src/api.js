// frontend/src/api.js
export const summarizeVideo = async (file) => {
  const formData = new FormData();
  formData.append('video', file);

  const response = await fetch('/api/summarize', {
    method: 'POST',
    body: formData
  });

  if (!response.ok) throw new Error('Failed to summarize video');
  return await response.json();
};
export const downloadVideo = (path) => {
  window.open(`/api${path}`, '_blank');
};