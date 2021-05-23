<template>
  <div id="app">
    <br>
    <img @click="main" src="@/assets/logo1.png" alt="logo" style="width: 300px">
    <!-- 로고 클릭하면 메인페이지로 -->

    <Menu style="position:fixed; top:0; z-index:3;"></Menu>

    <div id="nav">
      <span v-if="login">
        <router-link :to="{ name: 'Movie' }">Movie</router-link> |
        <router-link :to="{ name: 'Community' }">Community</router-link> | 
        <router-link :to="{ name: 'Login' }" @click.native="logout">LOGOUT</router-link> 
        <!-- 로그아웃하면 클릭시 로그인화면으로 보내기 -->
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </span>
    </div>
    <router-view @login="login = true"/>

    <!-- <button @click="onClickBtn">전체 영화 불러오기</button>
    <div class="row row-cols-1 row-cols-md-4 ms-5">
    <MovieCard /> -->
    <!-- </div> -->
  </div>
</template>

<script>
import Menu from '@/components/Menu'
// import MovieCard from '@/components/MovieCard'
// import axios from 'axios'
// const API_URL = 'https://gist.githubusercontent.com/eduChange-hphk/d9acb9fcfaa6ece53c9e8bcddd64131b/raw/9c8bc58a99e2ea77d42abd41376e5e1becabea69/movies.json'


export default {
  name: 'App',
  components: {
    Menu,
    // MovieCard,
  },
  data: function () {
    return {
      login: false, //flag
    }
  },
  methods: {
    //로고 누르면 메인페이지로
    main: function () {
      console.log('MainPage')
      this.$router.push({ name: 'App' })
    },
    logout: function() {
      console.log('logout 됨')
      // 로그아웃 처리
      this.login = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    //1. vue instance가 생성된 직후에 jwt를 가져오는 함수 실행하기
    const token = localStorage.getItem('jwt')
    // 2. 토큰이 있따면..
    if (token) {
      this.login = true
    }
  },
  // onClickBtn: function (){
  //     this.movies
  //     axios.get(API_URL, {})
  //     .then((res) => {
  //       console.log(res)
  //       this.movies = res.data
  //       console.log(this.movies)
        
  //     })
  //     .catch((err) => {
  //       console.log(err)
  //     })
    

  //   },

}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: white;
}

#nav a.router-link-exact-active {
  color: #e0435e;
}
</style>
