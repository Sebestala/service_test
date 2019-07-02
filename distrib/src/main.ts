import Vue from 'vue';
import App from './App.vue';
import router from './router';
import Axios from 'axios';
import VueAxios from 'vue-axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import '@/styles/index.scss';

Vue.use(ElementUI, {size:'small'});

Vue.use(VueAxios, Axios.create({
  baseURL: 'http://127.0.0.1:5000'
}));

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
