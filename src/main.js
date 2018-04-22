// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Header from './Header'
import LoginForm from './LoginForm'
import router from './router'

Vue.config.productionTip = false

Vue.component('custom-header', Header);
Vue.component('login-form', LoginForm);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
})
