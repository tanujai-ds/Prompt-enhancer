import { motion } from 'framer-motion';
import { cardHover, fadeInVariants } from '../animations/variants';

export const ResultCard = ({ title, content, onCopy, icon, loading }) => {
  return (
    <motion.div 
      className="card h-96 flex flex-col"
      variants={fadeInVariants}
      whileHover={cardHover}
    >
      <h3 className="text-xl font-bold mb-4 flex items-center gap-3 text-black">
        <span>{icon}</span> {title}
      </h3>
      
      {loading ? (
        <div className="flex-1 flex items-center justify-center">
          <motion.div
            animate={{ rotate: 360 }}
            transition={{ duration: 2, repeat: Infinity }}
            className="text-4xl"
          >
            ⚙️
          </motion.div>
        </div>
      ) : content ? (
        <div>
          <div className="flex-1 overflow-y-auto mb-4 pr-2 text-gray-700 leading-relaxed">
            {content}
          </div>
          
          {onCopy && (
            <motion.button
              className="btn-primary w-full text-sm py-2 flex items-center justify-center gap-2"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={onCopy}
            >
              📋 Copy to Clipboard
            </motion.button>
          )}
        </div>
      ) : (
        <div className="flex-1 flex items-center justify-center text-gray-400 italic">
          Results will appear here after processing...
        </div>
      )}
    </motion.div>
  );
};

export default ResultCard;
