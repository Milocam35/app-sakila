import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [tailwindcss(), react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://ec2-3-87-74-58.compute-1.amazonaws.com:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    },
    host: '0.0.0.0', // O la IP específica que quieras
    port: 5173, // Puedes cambiarlo si es necesario
    strictPort: true, // Para asegurarte de que usa ese puerto
    allowedHosts: ['ec2-3-95-29-251.compute-1.amazonaws.com']
  }
})
