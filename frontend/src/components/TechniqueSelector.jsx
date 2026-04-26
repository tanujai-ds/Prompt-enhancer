import { useState } from 'react';
import { motion } from 'framer-motion';
import { itemVariants } from '../animations/variants';

const TECHNIQUES = [
  { id: 'specific', label: '📌 Be Specific - Add Details & Constraints', value: 'Be specific (add details and constraints)' },
  { id: 'role', label: '👤 Assign Role - Define AI Purpose', value: 'Give a role (assign AI a role)' },
  { id: 'examples', label: '📚 Few-Shot Examples - Provide References', value: 'Few-shot examples' },
  { id: 'cot', label: '🧠 Chain of Thought - Enable Reasoning', value: 'Chain of thought reasoning' },
  { id: 'format', label: '📋 Define Format - Specify Output Structure', value: 'Define output format' },
];

export const TechniqueSelector = ({ selectedTechniques, onChange }) => {
  const handleToggle = (value) => {
    const newSelected = selectedTechniques.includes(value)
      ? selectedTechniques.filter(t => t !== value)
      : [...selectedTechniques, value];
    onChange(newSelected);
  };

  return (
    <motion.div 
      className="card"
      variants={itemVariants}
    >
      <h2 className="text-xl md:text-2xl font-bold mb-6 flex items-center gap-3 text-black">
        <span>🎯</span> Enhancement Methods
      </h2>
      
      <div className="grid md:grid-cols-2 gap-4">
        {TECHNIQUES.map((technique) => (
          <motion.label
            key={technique.id}
            className="flex items-center p-4 rounded-lg hover:bg-black hover:bg-opacity-5 cursor-pointer transition-all border border-gray-200 hover:border-black"
            whileHover={{ x: 5 }}
          >
            <input
              type="checkbox"
              checked={selectedTechniques.includes(technique.value)}
              onChange={() => handleToggle(technique.value)}
              className="w-5 h-5 cursor-pointer accent-black"
            />
            <span className="ml-3 text-gray-800 font-medium">{technique.label}</span>
          </motion.label>
        ))}
      </div>
    </motion.div>
  );
};

export default TechniqueSelector;
