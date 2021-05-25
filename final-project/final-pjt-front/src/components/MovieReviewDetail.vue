<template>
  <div>
  
    <h4>{{ review.id }}번 리뷰</h4>
    <h3>리뷰제목: {{ review.title }}</h3>
    <h5>영화 평점: {{review.rank}}</h5>
    <h5>리뷰내용:{{review.content}}</h5>
   <hr>
  
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'MovieReviewDetail',
  props: {
    review: {
      type: Object,
    },
    movie: {
      type: Object
    }
  },
  methods: {
     getComments: function () {
      const config = this.getToken()
      axios.get(`${SERVER_URL}/movies/${this.movie.id}/reviews/`, config)
        .then((res) => {
          this.comments = res.data
          console.log('뜬거냐?' + res)
        })
        .catch((err) => {
          alert(err)
          console.log(err)
        })
  },
  computed: {
    commentsList: function () {
      console.log('저장')
      return this.comments
    },
  },
  created: function () {
    alert('시작')
    this.getComments()
  }
}
}
</script>

<style>

</style>