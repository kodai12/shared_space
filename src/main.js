// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import ja from 'element-ui/lib/locale/lang/ja';

import Header from './components/Header';
import LoginForm from './components/LoginForm';
import FileList from './components/FileList';
import UploadButton from './components/UploadButton';
import router from './router';

Vue.config.productionTip = false;

Vue.use(ElementUI, { ja });

Vue.component('custom-header', Header);
Vue.component('login-form', LoginForm);
Vue.component('file-list', FileList);
Vue.component('upload-button', UploadButton);

new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  router,
  data: {
    message: 'Hello',
  },
});
