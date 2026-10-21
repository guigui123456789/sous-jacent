import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const noms = ['mecanisme', 'etudes', 'fondamentaux', 'notes', 'graphique'];
  const tout = [];
  for (const nom of noms) {
    const entrees = await getCollection(nom);
    for (const e of entrees) {
      if (e.data.brouillon) continue;
      tout.push({
        title: e.data.titre,
        description: e.data.chapo,
        pubDate: e.data.date,
        link: `/${nom}/${e.id}/`,
      });
    }
  }
  tout.sort((a, b) => b.pubDate - a.pubDate);
  return rss({
    title: 'sous-jacent',
    description: "Les mécanismes derrière les prix.",
    site: context.site,
    items: tout,
  });
}
