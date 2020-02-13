import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import router from '@/router';
import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';

Vue.use(VueRouter);
Vue.config.productionTip = false;

Vue.use(VueMaterial);

new Vue({
  render: h => h(App),
  router
}).$mount('#app');
