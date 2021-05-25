<template>
  <div>
    <h2 style="margin-bottom:30px">Review List</h2>
    <h5 v-if="reviews">리뷰 상세페이지로 넘어가고 싶으시면 제목을 클릭하세요!</h5>    
    <ul>
      
      <div v-for="(review, idx) in reviews" :key="idx">
        <!-- {{ review }} -->
        <MovieReviewDetail 
          :reviews="reviews"
          :movie="movie"
          @deleteReview="deleteReview"
          @reviews-updated="updateRiview"
        />
        <hr>
      </div>
    </ul>
  </div>
</template>

<script>
import MovieReviewDetail from '@/components/MovieReviewDetail'
export default {
  name: "ReviewList",
  components: {
    MovieReviewDetail,
  },
  props: {
    reviews: {
      type: [Array, Object],
    },
    movie: {
      type: Object,
    },
  },
  data: function () {
    return {

    }
  },
  methods: {
    deleteReview: function () {
      this.$emit('deleteReview')
    },
    updateRiview: function () {
      this.$emit('reviews-updated')
    }
  },
}
</script>

<style>
</style>
