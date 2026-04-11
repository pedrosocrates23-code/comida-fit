import { defineCollection, z } from 'astro:content';

const receitasCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title:          z.string(),
    description:    z.string().max(160),
    categoria:      z.enum([
      'cafe-da-manha',
      'almoco-fit',
      'lanches-saudaveis',
      'jantar-low-carb',
      'sobremesas-fit',
      'smoothies-e-sucos',
      'pre-treino',
      'pos-treino',
    ]),
    tempoPreparo:    z.number(),
    tempoCozimento:  z.number().optional(),
    porcoes:         z.number(),
    calorias:        z.number(),
    proteinas:       z.number(),
    carboidratos:    z.number(),
    gorduras:        z.number(),
    ingredientes:    z.array(z.string()),
    instrucoes:      z.array(z.string()),
    keywords:        z.array(z.string()),
    publishDate:     z.date(),
    image:           z.string(),
    imageAlt:        z.string(),
    rating:          z.number().min(1).max(5).default(4.8),
    ratingCount:     z.number().default(127),
    featured:        z.boolean().default(false),
  }),
});

export const collections = { receitas: receitasCollection };
