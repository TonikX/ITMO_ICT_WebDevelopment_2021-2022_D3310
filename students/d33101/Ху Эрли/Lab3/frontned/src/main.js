import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false
Vue.use(VueAxios, axios)
// axios.defaults.baseURL = '/goods';
new Vue({
  store: store,
  router,
  vuetify,
  // axios,
  render: function (h) { return h(App) }
}).$mount('#app') 