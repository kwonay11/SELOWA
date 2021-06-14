<template>
  <div id="app">
    <br>
    <img src="@/assets/logo1.png" alt="logo" style="width: 300px">
    <!-- 로고 클릭하면 메인페이지로 -->

    <!-- <Menu style="position:fixed; top:0; z-index:3;"></Menu> -->
    <div id="nav" class="card" style="border: 1px solid rgb(78, 51, 62); background-color: rgba(0, 0, 0, 0.726);">
      
      <span v-if="login">
        <!-- <router-link :to="{ name: 'Home' }" >Home</router-link> | -->
        <router-link :to="{ name: 'Home' }" class="fas fa-home font-weight-bolder " style="text-decoration:none"> Home</router-link> |
        <router-link :to="{ name: 'Movie' }" class="fas fa-film font-weight-bolder " style="text-decoration:none"> Movie</router-link> |
        <router-link :to="{ name: 'Recommend' }" class="fas fa-video font-weight-bolder " style="text-decoration:none"> Recommended Movie</router-link> |
        <router-link :to="{ name: 'Community' }" class="fas fa-comment font-weight-bolder " style="text-decoration:none"> Community</router-link> | 
        <span v-if="login"><router-link :to="{ name: 'MyProfile' }" class="fas fa-id-card-alt font-weight-bolder " style="text-decoration:none"> MyProfile</router-link></span> |
        <router-link @click.native="logout" to="#" class="fas fa-sign-out-alt font-weight-bolder " style="text-decoration:none"> LOGOUT</router-link> 
        <!-- 로그아웃하면 클릭시 로그인화면으로 보내기 -->
      </span>
      <span v-else>
        <!-- <router-link :to="{ name: 'Home' }" class="fas fa-home font-weight-bolder " style="text-decoration:none"> Home</router-link> | -->
        <router-link :to="{ name: 'Signup' }" class="fas fa-user-plus font-weight-bolder " style="text-decoration:none"> Signup</router-link> |
        <router-link :to="{ name: 'Login' }" class="fas fa-sign-in-alt font-weight-bolder " style="text-decoration:none">Login</router-link> 
      </span>
      
    </div>
    <router-view @login="login = true"/>

    <Slide id="page-wrap">
    <!-- 로그인했을 때 -->
    <span v-if="login"><router-link :to="{ name: 'Home' }" class="fas fa-home font-weight-bolder " style="color:#e0435e;text-decoration:none"> Home</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'Movie' }" class="fas fa-film font-weight-bolder " style="color:#e0435e;text-decoration:none"> Movie</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'Recommend' }" class="fas fa-video font-weight-bolder " style="color:#e0435e;text-decoration:none"> Recommended Movie</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'Community' }" class="fas fa-comment font-weight-bolder " style="color:#e0435e;text-decoration:none"> Community</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'MyProfile' }" class="fas fa-id-card-alt font-weight-bolder " style="color:#e0435e; text-decoration:none"> MyProfile</router-link></span>
    <span v-if="login"><router-link @click.native="logout" to="#" class="fas fa-sign-out-alt font-weight-bolder " style="color:#e0435e;text-decoration:none"> Logout</router-link></span>
   <!-- 로그인 안했을 때 -->
    <span v-if="!login"><router-link :to="{ name: 'Signup' }" class="fas fa-user-plus font-weight-bolder " style="color:#e0435e; text-decoration:none"> Signup</router-link></span>
    <span v-if="!login"><router-link :to="{ name: 'Login' }" class="fas fa-sign-in-alt font-weight-bolder " style="color:#e0435e; text-decoration:none"> Login</router-link></span>
    <!-- <span v-if="login"><router-link :to="{ name: 'Recommend' }" class="far fa-thumbs-up font-weight-bolder " style="color:#e0435e;text-decoration:none"> Recommend</router-link></span> -->
    <!-- <span v-if="login"><router-link :to="{ name: 'Users' }" class="fas fa-user-friends font-weight-bolder "> Users</router-link></span> -->
    
  </Slide>


  </div>

  


</template>

<script>
import { Slide } from 'vue-burger-menu'
export default {
  name: 'App',
  components: {
    Slide
  },
  props: {
    login_info: Boolean
  },
  data: function () {
    return {
      login: false, //flag
    }
  },
  methods: {
    
    logout: function() {
      console.log('logout 됨')
      // 로그아웃 처리
      this.login = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },



    
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
  font-family:'Raleway','Sunflower', sans-serif;
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

#nc-main {
    position: relative;
    height: 100vh;
    overflow-x: hidden;
    -webkit-box-shadow: 0 0 30px #241d20;
    box-shadow: 0 0 30px #241d20;
    -webkit-transition: -webkit-transform 0.4s;
    transition: -webkit-transform 0.4s;
    transition: transform 0.4s;
    transition: transform 0.4s, -webkit-transform 0.4s;
}




</style>
