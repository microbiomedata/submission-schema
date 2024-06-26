import { DataHarmonizer, Footer, Toolbar } from 'data-harmonizer';
import menu from './menu.json';

import 'data-harmonizer/data-harmonizer.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';

document.addEventListener('DOMContentLoaded', function () {
  const dhRoot = document.querySelector('#data-harmonizer-grid');
  const dhFooterRoot = document.querySelector('#data-harmonizer-footer');
  const dhToolbarRoot = document.querySelector('#data-harmonizer-toolbar');

  const params = new URLSearchParams(location.search);
  const templatePath = params.get('template');

  const dh = new DataHarmonizer(dhRoot);
  
  new Footer(dhFooterRoot, dh);

  new Toolbar(dhToolbarRoot, dh, menu, {
    templatePath,
    getSchema: async (schema) => {
      return (await import(`../project/json/${schema}.json`)).default
    },
  });
});
