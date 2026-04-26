import { useState, useCallback } from 'react';
import { promptAPI } from '../services/api';

export const usePromptImprove = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  const improvePrompt = useCallback(async (prompt, techniques) => {
    setLoading(true);
    setError(null);
    
    try {
      const data = await promptAPI.improve(prompt, techniques);
      setResult(data);
      return data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  return { 
    improvePrompt, 
    loading, 
    error, 
    result,
    setResult,
    setError 
  };
};

export default usePromptImprove;
