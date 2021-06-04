<template>
  <div class="d-flex text-align:center col m-1">
        <p class="st-font" style="margin-left: 1em;">좋아요 {{ numLike }}개</p>
    <vue-star  animate="animated bounceIn" color="#F05654" >
      <i v-if="isLiking" @click="like" slot="icon" style="color:crimson" class="fa fa-heart"></i>
      <i v-else @click="like" slot="icon" style="color:white" class="fa fa-heart"></i>
    </vue-star>
   <div class="col">
    <button @click="handleClickButton" class ="btn btn-outline-danger" style="width: 60%;">More Info</button>
    </div>
    <app-my-modal title="More Info" :visible.sync="visible">
      <div>
        
        <h2 style="font-weight: bold;">{{ movie.title }} </h2>
        <hr>
        <div class="video-container">
          <iframe :src="videoURI" frameborder="0" allow="fullscreen"></iframe>
        </div>
        <div class="movie-information-wrapper mt-4 d-flex align-items-center">
        <img :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`">
        <br>
        
    
        <div class="col">
          
        <!-- <h5 style="margin-bottom:10px" class="content-font">인기도 : {{ movie.popularity }}%</h5> -->
        <h5 style="margin-bottom:10px" class="content-font">평점 : {{ movie.vote_average }}점</h5>
        <h5 style="margin-bottom:10px" class="content-font">상영 시간 : {{ movie.runtime }}분</h5>
        <h5 style="margin-bottom:10px" class="content-font">개봉 일자 : {{ movie.release_date }}</h5>
        <h5 class="m-3">{{ movie.overview }}</h5>
        </div>
        </div>
        <hr>
        <!-- 좋아요 -->
        <div>
          <!-- <vue-star  animate="animated bounceIn" color="#F05654" >
            <i v-if="isLiking" @click="like" slot="icon" class="fa fa-heart"></i>
            <i v-else @click="like" slot="icon" class="fa fa-heart"></i>
          </vue-star> -->
        </div>
          <!-- <i id="heart" v-if="isLiking" @click="like" style="color:crimson; font-size:60px; text-align:left;" class="fas fa-heart"></i>
          <i id="heart" v-else @click="like" style="font-size:60px; text-align:left; margin-top:30px;" class="far fa-heart"></i> -->
        
          
        
        <!-- 싫어요 -->
        <!-- <i id="dislike" v-if="isLiking" @click="like" style="color:blue; font-size:60px; text-align:center;" class="far fa-thumbs-down"></i>
        <i id="dislike" v-else @click="like" style="font-size:60px; text-align:center; margin-top:30px;" class="far fa-thumbs-down"></i>  -->
        <!-- <p class="st-font" style="text-align:center; margin-top:5px">싫어요 {{ numDislike }}개</p>
        <! -- 보고싶어요 -->
        <!-- <i id="want" v-if="isLiking" @click="like" style="color:pink; font-size:60px; text-align:right;" class="far fa-laugh-squint"></i>
        <i id="want" v-else @click="like" style="font-size:60px; text-align:right; margin-top:30px;" class="far fa-laugh-squint"></i> -->
        <!-- <p class="st-font" style="text-align:right; margin-top:5px">보고싶어요 {{ numWant }}개</p> -->
        </div>
        
        <MovieReview 
          :movie="movie"
        />
      
    </app-my-modal>
  </div>
</template>

<script>
import myModal from './myModal'
import VueStar from 'vue-star'
import MovieReview from '@/components/MovieReview'
import _ from 'lodash'
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"



const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetail',
  data: function () {
    return {
      
      visible: false,
      me: [],
      liking: '',
      numLike: '',
      rating: Number(this.movie.vote_average),
    }
  },
  props: {
        movie:{
            type: Object,
        },
  },
  components: {
    appMyModal: myModal,
    MovieReview,
    VueStar,

  },
  methods: {
    handleClickButton(){
      this.visible = !this.visible
    },
    ratingToInt: function () {
      this.rating = Math.ceil(this.rating / 2)
    },
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
        this.me = res.data
        if (this.me.like_movies.includes(this.movie.id)) {
          this.liking = true
        } else {
          this.liking = false
        }
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    like: function () {
      const config = this.getToken()
      const item = {
        myId: this.me.id,
        movieId: this.movie.id,
      }
      axios.post(`${SERVER_URL}/movies/${this.me.id}/${this.movie.title}/like/`, item, config)
      .then( () => {
        console.log('좋아요')
        this.getMyName()
        this.check()
        // console.log(res)
      })
    },
    number: function () {
      // console.log(this.me)
      this.numLike = this.movie.like_users.length
    },
    check: function () {
      if (this.liking) {
        this.numLike -= 1
      } else {
        this.numLike += 1
      }
    },
  },
  computed: {
    isLiking: function () {
      return this.liking
    },
    videoURI: function () {
      const videoId = this.movie.id.title
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  },
  created: function () {
    this.getMyName()
    this.number()
    this.ratingToInt()
  }

}
</script>


<style>
.video-container > iframe {
  /* position: relative;   container를 기준으로 위치를 지정 */
  /* top: 0;               container의 가장 위쪽으로 위치를 지정 */
  /* left: 0; */
  width: 600px;
  height: 400px;
}
          
</style>
