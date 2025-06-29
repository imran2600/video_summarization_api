// src/api/axiosClient.js
import axios from "axios";

const axiosClient = axios.create({
  baseURL: "http://localhost:8000", // Update to your deployed URL when needed
  headers: {
    "Content-Type": "multipart/form-data",
  },
});

export default axiosClient;
