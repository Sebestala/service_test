import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
// import Money from './components/MoneyDistributor2.vue';
// import CreateCustomer from './components/CreateCustomer.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/createcustomer',
      name: 'create',
      component: () => import('./components/CreateCustomer.vue'),
      // component: CreateCustomer,
    },
    {
      path: '/deletecustomer',
      name: 'delete',
      component: () => import('./components/DeleteCustomer.vue'),
    },
    {
      path: '/transaction',
      name: 'transaction',
      component: () => import('./components/Transaction.vue'),
    },
    {
      path: '/',
      name: 'home',
      component: () => import('./components/Home.vue'),
    },
  ],
});
