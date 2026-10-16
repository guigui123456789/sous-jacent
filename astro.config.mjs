import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.sousjacent.com',
  integrations: [sitemap()],
  markdown: { shikiConfig: { theme: 'github-light' } }
});
