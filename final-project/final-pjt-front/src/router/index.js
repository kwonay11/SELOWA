import Vue from 'vue'
import VueRouter from 'vue-router'
import CommunityList from '@/views/communitys/CommunityList'
import CreateCommunity from '@/views/communitys/CreateCommunity'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'

Vue.use(VueRouter)

const routes = [
  {
    path: '/communitys',
    name: 'CommunityList',
    component: CommunityList,
  },
  {
    path: '/communitys/create',
    name: 'Createcommunity',
    component: CreateCommunity,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
