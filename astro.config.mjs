import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://sous-jacent.com',
  integrations: [sitemap()],
  markdown: { shikiConfig: { theme: 'github-light' } }
});
