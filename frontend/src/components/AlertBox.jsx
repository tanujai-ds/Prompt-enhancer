import { motion, AnimatePresence } from 'framer-motion';

export const AlertBox = ({ type, message, onClose }) => {
  const bgColors = {
    success: 'bg-green-50 border-green-300',
    error: 'bg-red-50 border-red-300',
    warning: 'bg-yellow-50 border-yellow-300',
    info: 'bg-blue-50 border-blue-300',
  };

  const textColors = {
    success: 'text-green-700',
    error: 'text-red-700',
    warning: 'text-yellow-700',
    info: 'text-blue-700',
  };

  const icons = {
    success: '✅',
    error: '❌',
    warning: '⚠️',
    info: 'ℹ️',
  };

  return (
    <AnimatePresence>
      {message && (
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -20 }}
          className={`p-4 rounded-lg border-2 ${bgColors[type]} ${textColors[type]} flex items-start justify-between`}
        >
          <div className="flex items-start gap-3">
            <span className="text-xl mt-0.5">{icons[type]}</span>
            <p className="font-medium">{message}</p>
          </div>
          {onClose && (
            <button
              onClick={onClose}
              className="text-xl hover:opacity-70"
            >
              ✕
            </button>
          )}
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default AlertBox;
