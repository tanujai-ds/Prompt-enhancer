/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: "#f8f9fa",
          100: "#f0f1f3",
          500: "#1a1a1a",
          600: "#0d0d0d",
          700: "#000000",
        },
        dark: {
          900: "#ffffff",
          800: "#f5f5f5",
          700: "#efefef",
          600: "#e0e0e0",
        },
        accent: {
          purple: "#2c3e50",
          indigo: "#34495e",
        },
      },
      animation: {
        slideInDown: "slideInDown 0.6s ease-out",
        slideInUp: "slideInUp 0.6s ease-out",
        fadeInUp: "fadeInUp 0.6s ease-out",
        fadeIn: "fadeIn 0.6s ease-out",
        pulse: "pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite",
      },
      keyframes: {
        slideInDown: {
          "0%": { opacity: "0", transform: "translateY(-40px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        slideInUp: {
          "0%": { opacity: "0", transform: "translateY(40px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        fadeInUp: {
          "0%": { opacity: "0", transform: "translateY(20px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        fadeIn: {
          "0%": { opacity: "0" },
          "100%": { opacity: "1" },
        },
      },
      backgroundImage: {
        gradient: "linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f172a 100%)",
        "gradient-card": "linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(51, 65, 85, 0.8) 100%)",
      },
      backdropBlur: {
        xs: "2px",
        sm: "4px",
        md: "10px",
      },
    },
  },
  plugins: [],
}
