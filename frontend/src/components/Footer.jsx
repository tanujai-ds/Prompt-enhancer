import { motion } from 'framer-motion';

export const Footer = () => {
  return (
    <motion.footer 
      className="text-center py-12 border-t border-gray-300 mt-12"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay: 0.5 }}
    >
      <p className="text-gray-600 text-sm mb-2">⚡ Powered by Groq AI - Lightning Fast Processing</p>
      <p className="text-gray-500 text-xs">🔒 Enterprise-Grade Security | 🚀 Production Ready | ✨ React Powered</p>
    </motion.footer>
  );
};

export default Footer;
