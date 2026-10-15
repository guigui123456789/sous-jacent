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
  }),
});

const fondamentaux = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/fondamentaux' }),
  schema: z.object({ ...commun, rubrique: z.string() }),
});

export const collections = { mecanisme, etudes, fondamentaux };
