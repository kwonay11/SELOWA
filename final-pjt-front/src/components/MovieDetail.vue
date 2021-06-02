<template>
  <div>
    <button @click="handleClickButton" class ="btn btn-outline-danger" style="width: 70%;">More Info</button>
    <app-my-modal title="More Info" :visible.sync="visible">
      <div>
        
        <h2 style="font-weight: bold;">{{ movie.title }} </h2>
        <hr>
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
        <i id="heart" v-if="isLiking" @click="like" style="color:crimson; font-size:60px; text-align:left;" class="fas fa-heart"></i>
        <i id="heart" v-else @click="like" style="font-size:60px; text-align:left; margin-top:30px;" class="far fa-heart"></i>
        <p class="st-font" style="text-align:center; margin-top:5px">좋아요 {{ numLike }}개</p>
       
        <!-- 싫어요 -->
        <!-- <i id="dislike" v-if="isLiking" @click="like" style="color:blue; font-size:60px; text-align:center;" class="far fa-thumbs-down"></i>
        <i id="dislike" v-else @click="like" style="font-size:60px; text-align:center; margin-top:30px;" class="far fa-thumbs-down"></i>  -->
        <!-- <p class="st-font" style="text-align:center; margin-top:5px">싫어요 {{ numDislike }}개</p>
        <! -- 보고싶어요 -->
        <!-- <i id="want" v-if="isLiking" @click="like" style="color:pink; font-size:60px; text-align:right;" class="far fa-laugh-squint"></i>
        <i id="want" v-else @click="like" style="font-size:60px; text-align:right; margin-top:30px;" class="far fa-laugh-squint"></i> -->
        <!-- <p class="st-font" style="text-align:right; margin-top:5px">보고싶어요 {{ numWant }}개</p> -->
        </div>
        <hr>
        <MovieReview 
          :movie="movie"
        />
      </div>
    </app-my-modal>
  </div>
</template>

<script>
import myModal from './myModal'

import MovieReview from '@/components/MovieReview'

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
        this.getMyName()
        this.check()
        // console.log(res)
      })
    },
    number: function () {
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
  },
  created: function () {
    this.getMyName()
    this.number()
    this.ratingToInt()
  }

}
</script>

<style>
p {white-space: nowrap;}
</style>