import Vue from 'vue'
import VueRouter from 'vue-router'
import SignIn from '../views/SignIn.vue'
import SignUp from '../views/SignUp.vue'
import ChickensList from '../views/Chickens.vue'
import BreedsList from '../views/Breeds.vue'
import CellsList from '../views/Cells.vue'
import UserInfo from '../views/Settings.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/chickenslist',
    name: 'ChickensList',
    component: ChickensList
  },
  {
    path: '/breedslist',
    name: 'BreedsList',
    component: BreedsList
  },
  {
    path: '/cellslist',
    name: 'CellsList',
    component: CellsList
  },
  {
    path: '/settings',
    name: 'UserInfo',
    component: UserInfo
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
