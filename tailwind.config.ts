import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        ink: "#1d252c",
        paper: "#fbfaf7",
        line: "#d8d2c7",
        moss: "#60735f",
        steel: "#426071",
        rust: "#a5553c",
        wheat: "#e6d7b8"
      }
    }
  },
  plugins: []
};

export default config;
