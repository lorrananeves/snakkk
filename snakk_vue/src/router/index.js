import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import About from '../views/About.vue'

import LogIn from '../views/LogIn.vue'
import SignUp from '../views/SignUp.vue'

import Dashboard from '../views/dashboard/Dashboard.vue'
import AddTeam from '../views/dashboard/AddTeam.vue'
import Chat from '../views/dashboard/Chat.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
  path: '/dashboard/add-team',
  name: 'AddTeam',
  component: AddTeam
  },
  {
  path: '/dashboard/chat:team_id',
  name: 'Chat',
  component: Chat
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
