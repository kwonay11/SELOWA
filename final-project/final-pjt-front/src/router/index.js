  
import Vue from 'vue'
import VueRouter from 'vue-router'
import Community from '@/views/communitys/Community'
import CommunityDetail from '@/views/communitys/CommunityDetail'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Movie from '@/views/movies/Movie'

Vue.use(VueRouter)

const routes = [
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