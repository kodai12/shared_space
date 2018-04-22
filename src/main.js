// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Header from './components/Header'
import LoginForm from './components/LoginForm'
import FileList from './components/FileList'
import UploadButton from './components/UploadButton'
import router from './router'

Vue.config.productionTip = false

Vue.component('custom-header', Header);
Vue.component('login-form', LoginForm);
Vue.component('file-list', FileList);
Vue.component('upload-button', UploadButton);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
})
