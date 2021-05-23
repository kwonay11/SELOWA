<template>
  <div id="app">
    <br>
    <img @click="main" src="@/assets/logo1.png" alt="logo" style="width: 300px">
    <!-- 로고 클릭하면 메인페이지로 -->
    <div id="nav">
      <span v-if="login">
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

    
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      login: false, //flag
    }
  },
  methods: {
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
