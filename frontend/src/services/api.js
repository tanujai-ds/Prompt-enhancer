import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const promptAPI = {
  improve: async (prompt, techniques = '') => {
    try {
      const response = await api.post('/api/v1/prompts/improve', {
        prompt,
        techniques,
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Failed to improve prompt');
    }
  },

  health: async () => {
    try {
      const response = await api.get('/health');
      return response.data;
    } catch (error) {
      throw new Error('Backend service unavailable');
    }
  },
};

export default api;
