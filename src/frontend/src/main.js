// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// import Inicio from './Inicio.vue'

import router from './router'

import BootstrapVue from 'bootstrap-vue'

// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueSweetalert2 from 'vue-sweetalert2'
 
// If you don't need the styles, do not connect
// import 'sweetalert2/dist/sweetalert2.min.css';
 


Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(VueSweetalert2);

/* eslint-disable no-new */

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

