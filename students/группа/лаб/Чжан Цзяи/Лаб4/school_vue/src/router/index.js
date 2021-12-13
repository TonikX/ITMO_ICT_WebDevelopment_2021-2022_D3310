import Vue from 'vue'
import VueRouter from 'vue-router'
import Report from '../components/Report'
import Login from '../components/Login'
import Register from '../components/Register'
import Student from '../components/Student'
import Schedule from '../components/Schedule'
import Teacher from '../components/Teacher'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'report',
    component: Report
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/student',
    name: 'student',
    component: Student
  },
  {
    path: '/schedule',
    name: 'schedule',
    component: Schedule
  },
  {
    path: '/teacher',
    name: 'teacher',
    component: Teacher
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
