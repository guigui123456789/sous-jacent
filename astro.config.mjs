import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.sousjacent.com',
  integrations: [sitemap()],
  redirects: {
    '/mentions-legales': '/informations-legales',
    /* Le graphique de la semaine a d'abord eu sa propre rubrique, le 21 octobre
       2026. Elle a été repliée dans « Le mécanisme » le jour même, pour ne pas
       charger le menu. Les adresses soumises à IndexNow restent valables. */
    '/graphique': '/mecanisme',
    '/graphique/2026-10-21-vicor-produits-et-redevances':
      '/mecanisme/2026-10-21-vicor-produits-et-redevances',
  },
  markdown: { shikiConfig: { theme: 'github-light' } }
});
