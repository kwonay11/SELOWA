<template>
  <Slide id="page-wrap">
    <!-- 로그인했을 때 -->
    <span v-if="login"><router-link :to="{ name: 'Home' }" class="fas fa-home font-weight-bolder " style="color:#e0435e;text-decoration:none"> Home</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'Movie' }" class="fas fa-film font-weight-bolder " style="color:#e0435e;text-decoration:none"> Movie</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'Recommend' }" class="fas fa-video font-weight-bolder " style="color:#e0435e;text-decoration:none"> Recommended Movie</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'Community' }" class="fas fa-comment font-weight-bolder " style="color:#e0435e;text-decoration:none"> Community</router-link></span>
    <span v-if="login"><router-link @click.native="logout" to="#" class="fas fa-sign-out-alt font-weight-bolder " style="color:#e0435e;text-decoration:none"> Logout</router-link></span>
    <span v-if="login"><router-link :to="{ name: 'MyProfile' }" class="fas fa-id-card-alt font-weight-bolder " style="color:#e0435e; text-decoration:none"> MyProfile</router-link></span>
   <!-- 로그인 안했을 때 -->
    <span v-if="!login"><router-link :to="{ name: 'Signup' }" class="fas fa-user-plus font-weight-bolder " style="color:#e0435e; text-decoration:none"> Signup</router-link></span>
    <span v-if="!login"><router-link :to="{ name: 'Login' }" class="fas fa-sign-in-alt font-weight-bolder " style="color:#e0435e; text-decoration:none"> Login</router-link></span>
    <!-- <span v-if="login"><router-link :to="{ name: 'Recommend' }" class="far fa-thumbs-up font-weight-bolder " style="color:#e0435e;text-decoration:none"> Recommend</router-link></span> -->
    <!-- <span v-if="login"><router-link :to="{ name: 'Users' }" class="fas fa-user-friends font-weight-bolder "> Users</router-link></span> -->
    
  </Slide>
</template>

<script>
import { Slide } from 'vue-burger-menu'
export default {
  name: "Menu",
  components: {
    Slide
  },
  props: {
    login_info: Boolean
  },
  data: function () {
    return {
      login: false,
    }
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      console.log('logout 됨__menu')
      this.login = false
      this.$router.push({ name: "Login" })
    },
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.login = true
    }
  },
  computed: {
    loginStatus: function () {
      return this.$store.state.login
    }
  },
  watch: {
    // loginCheck: function () {
    //   if (this.$store.state.login) {
    //     this.login=true
    //   }
    // }
    loginCheck: function () {
      console.log(this.login)
      if(this.login) {
        this.login = true
      }
    }
  }
}
</script>

<style>
</style>