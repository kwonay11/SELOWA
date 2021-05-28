  
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import Community from '@/views/communitys/Community'
import CommunityDetail from '@/views/communitys/CommunityDetail'
import CommunityDetailUpdate from '@/views/communitys/CommunityDetailUpdate'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Movie from '@/views/movies/Movie'
import Recommend from '@/views/movies/Recommend'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home,
  },
  {
    path: '/movies/recommend',
    name: 'Recommend',
    component: Recommend,
  },
  {
    path: '/movies',
    name: 'Movie',
    component: Movie,
  },
  {
    path: '/community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/communitydetail/:community_pk',
    name: 'CommunityDetail',
    component: CommunityDetail,
  },
  {
    path: '/CommunityDetailUpdate/:community_pk',
    name: 'CommunityDetailUpdate',
    component: CommunityDetailUpdate,
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