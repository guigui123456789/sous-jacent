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

export const collections = { mecanisme, etudes, fondamentaux };
