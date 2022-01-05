import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import vuetify from './plugins/vuetify'
Vue.config.productionTip = false
Vue.use(VueAxios, axios, BootstrapVue, IconsPlugin)
new Vue({
  router,
  axios,
  vuetify,
  render: h => h(App)
}).$mount('#app')
