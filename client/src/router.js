import Vue from 'vue';
import Router from 'vue-router';
import Control from './views/Control.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'controller',
      component: Control,
    },
  ],
});
