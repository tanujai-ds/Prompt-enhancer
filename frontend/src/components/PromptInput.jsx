import { motion } from 'framer-motion';
import { itemVariants } from '../animations/variants';

export const PromptInput = ({ prompt, setPrompt, onImprove, loading }) => {
  return (
    <motion.div 
      className="card"
      variants={itemVariants}
    >
      <motion.h2 className="text-xl md:text-2xl font-bold mb-6 flex items-center gap-3 text-black">
        <span>📝</span> Your Prompt
      </motion.h2>
      
      <textarea
        className="input-field h-32 mb-6 resize-none text-gray-900"
        placeholder="Type or paste your prompt here to begin enhancement..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        disabled={loading}
      />
      
      <motion.button
        className="btn-primary w-full text-lg font-bold"
        whileHover={{ scale: 1.02 }}
        whileTap={{ scale: 0.98 }}
        onClick={onImprove}
        disabled={loading || !prompt.trim()}
      >
        {loading ? (
          <span className="flex items-center justify-center gap-2">
            <span className="inline-block animate-spin">⚙️</span>
            Processing...
          </span>
        ) : (
          <span>🚀 ENHANCE PROMPT NOW</span>
        )}
      </motion.button>
    </motion.div>
  );
};

export default PromptInput;
