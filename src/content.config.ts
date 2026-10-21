import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const commun = {
  titre: z.string(),
  chapo: z.string(),
  date: z.coerce.date(),
  brouillon: z.boolean().default(false),
};

const mecanisme = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/mecanisme' }),
  schema: z.object({ ...commun, fait: z.string().optional() }),
});

const etudes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/etudes' }),
  schema: z.object({
    ...commun,
    societe: z.string(),
    isin: z.string().optional(),
    periode: z.string().default('2005 – 2025'),
    donneesCsv: z.string().optional(),
    numero: z.number(),
    resumePdf: z.string().optional(),
    memoirePdf: z.string().optional(),
    cours: z.string().optional(),
    partage: z.string().optional(),
    prochaineRevue: z.string().optional(),
    imageTete: z.string().optional(),
    pagesPdf: z.number().optional(),
    classeurXlsx: z.string().optional(),
    objectif: z.string().optional(),
    methode: z.string().default('1.0'),
    horizon: z.string().optional(),
    citations: z.array(z.string()).optional(),
    publication: z.object({ date: z.string(), valeur: z.string() }).optional(),
    revisions: z.array(z.object({
      date: z.string(),
      valeur: z.string(),
      motif: z.string(),
    })).default([]),
  }),
});

const fondamentaux = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/fondamentaux' }),
  schema: z.object({ ...commun, rubrique: z.string() }),
});

/* Les notes de suivi : une page après chaque publication trimestrielle d'une
   société couverte. Elles testent la thèse de l'étude et, le cas échéant,
   révisent l'objectif de cours. L'étude elle-même n'est jamais réécrite. */
const notes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/notes' }),
  schema: z.object({
    ...commun,
    societe: z.string(),
    etude: z.string(),
    trimestre: z.string(),
    cours: z.string(),
    objectif: z.string().optional(),
    objectifPrecedent: z.string().optional(),
    sens: z.enum(['confirmé', 'relevé', 'abaissé', 'initié']).default('confirmé'),
    methode: z.string().default('1.1'),
    partage: z.string().optional(),
    citations: z.array(z.string()).optional(),
  }),
});

/* Le graphique de la semaine : un graphique dessiné pour le site, sa source,
   et trois phrases. Format court, publié entre deux études. */
const graphique = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/graphique' }),
  schema: z.object({
    ...commun,
    image: z.string(),
    alt: z.string(),
    source: z.string(),
    lecture: z.string().optional(),
    lien: z.string().optional(),
    lienLibelle: z.string().optional(),
    partage: z.string().optional(),
  }),
});

export const collections = { mecanisme, etudes, fondamentaux, notes, graphique };
