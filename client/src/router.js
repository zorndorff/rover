import Vue from 'vue';
import Router from 'vue-router';
import Controller from './views/Controller.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'controller',
      component: Controller,
    },
  ],
});
