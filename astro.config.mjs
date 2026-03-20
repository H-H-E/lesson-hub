import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel/static';

export default defineConfig({
  output: 'static',
  adapter: vercel(),
  build: {
    format: 'file'
  },
  vite: {
    css: {
      devSourcemap: true
    }
  }
});
