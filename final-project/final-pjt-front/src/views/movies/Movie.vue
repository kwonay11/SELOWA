<template>
  <div class="home ms-5">
    <button  @click="onClickBtn" class ="btn btn-outline-danger m-1">Total Movie</button> 
    <button class ="btn btn-outline-danger m-1" >Recomanded Movie</button>
    <hr>
    <div class="row row-cols-1 row-cols-md-4 ms-5">
      <!-- 그리드 카드 형태로  -->
      <MovieCard v-for="(movie,idx) in movies" :key="idx" :movie="movie"/>
      <MovieDetail />
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import MovieDetail from '@/components/MovieDetail'
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
// @ is an alias to /src

export default {
  name: 'Movie',
  data: function(){
    return{
      movies: [],
    }
  },
  components: {
    MovieCard,
    MovieDetail,
  },
  methods:{
    onClickBtn: function (){
      axios.get(`${SERVER_URL}/movies/`, {})
      .then((res) => {
        this.movies = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    

    },

    
    
  }
}
</script>
