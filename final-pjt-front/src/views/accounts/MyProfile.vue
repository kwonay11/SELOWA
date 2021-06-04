<template>
  <div id="app">
    <h2>{{ user.age }}살 {{ user.username }}님의 마이페이지</h2>
    <hr>
    <h2>{{ user.username }}님이 좋아요한 영화</h2>
    <vue-glide v-if="my_like_movies.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 5}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for = "(movie, idx) in my_like_movies"
        :key="idx">
        
        <MovieCard
          :movie="movie"
        />
      </vue-glide-slide>
    </vue-glide>
  </div>
</template>

<script>
import axios from 'axios'
import { Glide, GlideSlide } from 'vue-glide-js'
import MovieCard from "@/components/MovieCard"
import VueJwtDecode from "vue-jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "MyProfile",
  data: function () {
    return { 
      like_movies: [],
      my_like_movies: [],
      user: '',
    }
  },
  components: {
    MovieCard,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide
  },
   methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },

     getMyName: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/myprofile/`, info, config)
      .then( (res) => {
        // console.log(res.data)
        this.user = res.data
        this.like_movies = res.data.like_movies
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    getMovieDatas: function () {
      axios.get(`${SERVER_URL}/movies/`)
      .then( (res) => {
        for(var i = 0; i < this.like_movies.length; i++){
          this.my_like_movies.push(res.data[this.like_movies[i]-1])
        }
      })
      .catch( (err) => {
        console.log(err)
      })
    },
  },
  created: function () {
    this.getMyName()
    this.getMovieDatas()
  },
  
}
</script>

<style>

</style>