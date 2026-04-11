import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://melhoresreceitasfit.com.br',
  output: 'static',
  integrations: [],
  image: {
    domains: ['melhoresreceitasfit.com.br'],
  },
  build: {
    assets: '_assets',
  },
  compressHTML: true,
});
