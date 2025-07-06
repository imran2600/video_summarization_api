// src/api.js
import axios from 'axios';

const API_BASE = 'http://localhost:8000'; // FastAPI backend

export const uploadVideo = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  const res = await axios.post(`${API_BASE}/summarize`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });

  return res.data;
};
