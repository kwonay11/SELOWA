<template>
 <div class="card bg-dark">
     <h2>검색어 : {{$route.query.inputText}}</h2>
    <h3>영화 제목: {{ inputText }}</h3>
 </div>
</template>

<script>
import axios from "axios"
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'SearchBar',
  data: function () {
    return {
      inputText: '',
      movies: [],
      result: []
    }
  },
  methods: {
      getMovies: function () {
      axios.get(`${SERVER_URL}/movies/`)
        .then(res => {
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
      },
      findMovie: function () {
      for(var i=0; i<this.movies.length; i++) {
        if (this.inputText in this.movies[i].title) {
          this.result.push(this.movies[i])
        }
      }
      console.log(this.result)
    },
   
  },
  created: function () {
    this.inputText = this.$route.query.inputText
    console.log(this.inputText)
    this.getMovies()
    this.findMovie()
}
}
</script>

<style>

</style>