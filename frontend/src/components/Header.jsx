import { motion } from 'framer-motion';
import { headerVariants } from '../animations/variants';

export const Header = () => {
  return (
    <motion.div 
      className="py-16 px-8 text-center mb-12 card"
      variants={headerVariants}
      initial="hidden"
      animate="visible"
    >
      <motion.h1 
        className="text-5xl md:text-6xl font-black mb-4 text-black"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2, duration: 0.8 }}
      >
        ✨ Prompt Improver AI
      </motion.h1>
      <motion.p 
        className="text-lg text-gray-600 font-light"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.4, duration: 0.8 }}
      >
        Professional-Grade Prompt Enhancement & Optimization Engine
      </motion.p>
    </motion.div>
  );
};

export default Header;
