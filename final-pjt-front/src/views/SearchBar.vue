<template>
 <div class="card bg-dark">
     <h2>검색어 : {{$route.query.keyword}}</h2>
     <div >
       <!-- keyword와 영화제목이 같은것의 무비카드 보여주기 -->

     
    <h3>영화 제목: {{ keyword }}</h3>

        <MovieCard
          :movie="movie"
        />
    </div>
 </div>
</template>

<script>
import axios from "axios"
const SERVER_URL = process.env.VUE_APP_SERVER_URL

import MovieCard from "@/components/MovieCard"

export default {
  name: 'SearchBar',
  components: {
    MovieCard,
   
  },
  data: function () {
    return {
      keyword: '',
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
        if (this.keyword in this.movies[i].title) {
          this.result.push(this.movies[i])
        }
      }
      console.log(this.result)
    },
   
  },
  created: function () {
    this.keyword = this.$route.query.keyword
    console.log(this.keyword)
    this.getMovies()
    this.findMovie()
}
}
</script>

<style>

</style>