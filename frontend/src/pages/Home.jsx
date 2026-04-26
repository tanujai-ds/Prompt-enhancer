import { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { containerVariants } from '../animations/variants';
import Header from '../components/Header';
import PromptInput from '../components/PromptInput';
import TechniqueSelector from '../components/TechniqueSelector';
import ResultCard from '../components/ResultCard';
import AlertBox from '../components/AlertBox';
import Footer from '../components/Footer';
import usePromptImprove from '../hooks/usePromptImprove';

export const Home = () => {
  const [prompt, setPrompt] = useState('');
  const [techniques, setTechniques] = useState([]);
  const { improvePrompt, loading, error, result, setError } = usePromptImprove();

  const handleImprove = async () => {
    if (!prompt.trim()) {
      setError('Please enter a prompt to enhance!');
      return;
    }
    
    try {
      await improvePrompt(prompt, techniques.join(', '));
    } catch (err) {
      console.error('Error improving prompt:', err);
    }
  };

  const handleCopyResult = () => {
    if (result?.improved_prompt) {
      navigator.clipboard.writeText(result.improved_prompt).then(() => {
        alert('✅ Copied to clipboard!');
      });
    }
  };

  return (
    <motion.div 
      className="min-h-screen bg-white px-4 md:px-8 py-12"
      variants={containerVariants}
      initial="hidden"
      animate="visible"
    >
      <div className="max-w-7xl mx-auto">
        <Header />
        
        <div className="grid md:grid-cols-2 gap-8 mb-8">
          <motion.div>
            <PromptInput 
              prompt={prompt}
              setPrompt={setPrompt}
              onImprove={handleImprove}
              loading={loading}
            />
          </motion.div>
          
          <motion.div>
            <TechniqueSelector 
              selectedTechniques={techniques}
              onChange={setTechniques}
            />
          </motion.div>
        </div>

        {(error || result) && (
          <motion.div className="mb-8">
            <AlertBox 
              type={error ? 'error' : 'success'}
              message={error || '✅ Prompt enhanced successfully!'}
              onClose={() => error && setError(null)}
            />
          </motion.div>
        )}

        <div className="grid md:grid-cols-2 gap-8 mb-8">
          <ResultCard
            title="Original Prompt"
            content={prompt || null}
            icon="📄"
            loading={false}
          />
          
          <ResultCard
            title="Enhanced Prompt"
            content={result?.improved_prompt || null}
            icon="✨"
            loading={loading}
            onCopy={result?.improved_prompt ? handleCopyResult : null}
          />
        </div>

        <Footer />
      </div>
    </motion.div>
  );
};

export default Home;
