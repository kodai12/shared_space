import Vue from 'vue';
import Router from 'vue-router';

import MainPage from '@/components/pages/Main';
import LoginPage from '@/components/pages/Login';

Vue.use(Router);

export default new Router({
  base: '/',
  mode: 'history',
  routes: [
    {
      path: '/',
      component: MainPage
    },
    {
      path: '/login',
      component: LoginPage
    }
  ]
});
