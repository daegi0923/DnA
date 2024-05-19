import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      '/api': {
        target: 'https://news.naver.com',
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, '')
      },
      '/openai': {
        target: 'https://api.openai.com',
        changeOrigin: true,
        rewrite: path => path.replace(/^\/openai/, ''),
        headers: {
          'Access-Control-Allow-Origin': '*',
        }
      }
    }
  }
})


