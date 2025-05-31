// src/services/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://saborescaseros-backend-h9dsh5fddaf8epgf.canadaeast-01.azurewebsites.net/api',
});

export default api;
