<template>
<div class="col" >

<!-- <button class="btn btn-sm btn-dark m-4" type="submit"> -->
  <div class="card m-4 bg-dark" style="width: 20rem;">
      
      <img @click="movieDetail" :src="movieImage" alt="poster_path" style="width:320px" class="m-1" >
        <hr>
        <MovieDetail :movie="movie"/>
        <br>
        <!-- <button @click="movieDetail()" class ="btn btn-outline-danger">See more info</button> -->
        
  </div>
<!-- </button> -->
</div>
</template>

<script>
import MovieDetail from '@/components/MovieDetail'

export default {
    name:'MovieCard',
    components: {
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
        console.log('디테일은 넘어가는데...')
        // 여기서 각 무비 id에 해당하는 object데이터를 디테일로 넘겨줘야할듯?.?
        console.log(this.movie)
    },


    
    
  }

}
</script>

<style>
/* 영화 하나 커서 올렸을 때 확대 됨 */
.card img {
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transform: scale(1);
  -webkit-transition: 0.3s;
  -moz-transition: 0.3s;
  -ms-transition: 0.3s;
  -o-transition: 0.3s;
  transition: 0.3s;
}
.card:hover img {
  -webkit-transform: scale(1.2);
  -moz-transform: scale(1.2);
  -ms-transform: scale(1.2);
  -o-transform: scale(1.2);
  transform: scale(1.2);
}

</style>