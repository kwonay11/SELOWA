<template>
 <div class="card bg-dark d-flex justify-content-center align-items-center">
     <h2>검색어 : {{ keyword }}</h2>
     <!-- 자료가 없을 때-->
    <div v-if="result.length === 0">
    <h1>해당 영화에 대한 정보가 없습니다.</h1>
    </div>
    <div v-else>

      <h3>{{ result }}</h3>
      
      <MovieCard />
      
      
       
      </div>
       
    

 </div>
</template>

<script>
import axios from "axios"
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import { Glide, GlideSlide } from 'vue-glide-js'
import MovieCard from "@/components/MovieCard"

export default {
  name: 'SearchBar',
  components: {
    MovieCard,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
  },
  data: function () {
    return {
      keyword: '',
      movies: [],
      result: [],
      
    }
  },
  methods: {
      getMovies: function () {
      axios.get(`${SERVER_URL}/movies/`)
        .then((res) => {
          this.movies = res.data
          for(var i=0; i<this.movies.length; i++) {
        if (this.keyword === this.movies[i].title) {
          this.result.push(this.movies[i])
          console.log(this.movies[i])
          console.log('에러안남')

          
          
        }
      }
         
        })
        .catch((err) => {
          console.log(err)
          console.log('에러')
        })
      },
    //   findMovie: function () {
    //   for(var i=0; i<this.movies.length; i++) {
    //     if (this.keyword === this.movies[i].title) {
    //       this.result.push(this.movies[i])
    //       console.log(this.movies[i])
          
          
    //     }
    //   }
    //   console.log(this.result) //값이 안들어감
    //   console.log('영화찾아짐')
    // },
   
  },
  created: function () {
    this.keyword = this.$route.query.keyword //검색창에서 받아옴
    // console.log(this.keyword)
    this.getMovies()
    // this.findMovie()
}
}
</script>

<style>

</style>