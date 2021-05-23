<template>
  <div class="home ms-5">
    <button  @click="onClickBtn" class ="btn btn-outline-danger m-1">Total Movie</button> 
    <button class ="btn btn-outline-danger m-1" >Recomanded Movie</button>
    <hr>
    <div class="row row-cols-1 row-cols-md-4 ms-5">
      <!-- 그리드 카드 형태로  -->
    <MovieCard v-for="(movie,idx) in movies" :key="idx" :movie="movie"/>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import axios from 'axios'
// @ is an alias to /src
const API_URL = 'https://gist.githubusercontent.com/eduChange-hphk/d9acb9fcfaa6ece53c9e8bcddd64131b/raw/9c8bc58a99e2ea77d42abd41376e5e1becabea69/movies.json'

export default {
  name: 'Movie',
  data: function(){
    return{
      movies: [],
    }
  },
  components: {
    MovieCard,
  },
  methods:{
    onClickBtn: function (){
      this.movies
      axios.get(API_URL, {})
      .then((res) => {
        console.log(res)
        this.movies = res.data
        console.log(this.movies)
        
      })
      .catch((err) => {
        console.log(err)
      })
    

    },

    
    
  }
}
</script>
