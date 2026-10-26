import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.sousjacent.com',
  /* Une seule forme d'adresse fait foi : avec barre oblique finale, comme le
     canonical. Vercel renvoie la forme sans barre en 308 (voir vercel.json),
     ce qui supprime les doublons « Alternate page with proper canonical »
     relevés dans la Search Console le 26 octobre 2026. */
  trailingSlash: 'always',
  integrations: [sitemap()],
  /* Les anciennes adresses sont redirigées par Vercel en 308 (vercel.json),
     et non plus par une page HTML intermédiaire portant un noindex :
     une vraie redirection transmet l'autorite, la page HTML ne transmet rien. */
  markdown: { shikiConfig: { theme: 'github-light' } }
});
