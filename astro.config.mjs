import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://sousjacent.com',
  integrations: [sitemap()],
  markdown: { shikiConfig: { theme: 'github-light' } }
});
