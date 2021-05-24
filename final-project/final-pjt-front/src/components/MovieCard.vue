<template>
<div class="col" >
  <div class="card m-1 " style="width: 20rem;">
      <img @click="movieDetail" :src="movieImage" alt="poster_path" >
        <MovieDetail :movie="movie"/>
        <!-- <button @click="movieDetail()" class ="btn btn-outline-danger">See more info</button> -->
        
  </div>
</div>
</template>

<script>
import { Glide, GlideSlide } from 'vue-glide-js'
import MovieDetail from '@/components/MovieDetail'

export default {
    name:'MovieCard',
    components: {
        [Glide.name]: Glide,
        [GlideSlide.name]: GlideSlide,
        MovieDetail,
    },
    props: {
        movie:{
            type: Object,
        }
    },
    computed:{
       movieImage: function () {
           return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
           //https://image.tmdb.org/t/p/w500/를 붙여서 리턴
       },

    },
    methods:{
    movieDetail: function () {
        // 여기서 각 무비 id에 해당하는 object데이터를 디테일로 넘겨줘야할듯?.?
        console.log(this.movie)
    },


    
    
  }

}
</script>

<style>
</style>