<template>
  <div>
  
    <h4>{{ review.id }}번 리뷰</h4>
    <h3>리뷰제목: {{ review.title }}</h3>
    <h5>내가 준 평점: {{review.rank}}</h5>
    <h5>리뷰내용:{{review.content}}</h5>
   
          <div v-if="review.rank==5"> 
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i>
          
          </div>
          <div v-else-if="review.rank==4">
            <i class="fas fa-star" style="color:yellow"></i> 
            <i class="fas fa-star" style="color:yellow"></i> 
            <i class="fas fa-star" style="color:yellow"></i> 
            <i class="fas fa-star" style="color:yellow"></i>
            
          </div>
          <div v-else-if="review.rank==3">
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i>
          </div>
          <div v-else-if="review.rank==2">
            <i class="fas fa-star" style="color:yellow"></i>
            <i class="fas fa-star" style="color:yellow"></i>
          </div>
          <div v-else-if="review.rank==1">
            <i class="fas fa-star" style="color:yellow"></i>
          </div>
        
     
    <div v-if="review.user === this.user">
      <button class="btn btn-secondary m-1" @click="reviewModify(review)">수정</button>
      <button class="btn btn-secondary m-1" @click="reviewDelete(review)">삭제</button>
    </div>
<!-- 리뷰 수정 -->
  <div>
      <!--뺏다넣었다하면 됨v-if="reviewModify(review)" -->
      <!-- 그냥 아래에 뭘 넣고 빼면 됨 -->
      <app-update-modal title="리뷰 수정" v-show="visible">
        <hr>
              <h2>리뷰 수정</h2>
              <div class="row">
                  <div class="col-lg-8 mx-auto">
                      
                    <div>
                        <div>
                            <label>리뷰 제목:</label>
                            <input v-model.trim="title" class="form-control" id="reviewTitle" type="text" :placeholder="review.title" required="required" data-validation-required-message="Please enter your review title." />
                            
                        </div>
                    </div>

                        <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                            <label>영화 제목: {{ movie.title }}</label>
                            
                        </div>
                      <span>내가 생각하는 영화 평점:</span>
                      <select v-model="myMovieRate2">
                        <option>5</option>
                        <option>4</option>
                        <option>3</option>
                        <option>2</option>
                        <option>1</option>
                      </select>

                        <div>
                            <label>리뷰 내용</label>
                            <textarea v-model.trim="content" class="form-control" id="content" rows="5" :placeholder="review.content" required="required" data-validation-required-message="Please enter a content."></textarea>
                            
                        </div>
                    <br />
                    <div id="success"></div>
                    <div class="text-white st-font form-group"><button @click="update(review)" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">수정 !</button></div>
                  </div>
              </div>
          
      </app-update-modal>
      <hr>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import updateModal from './updateModal'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'MovieReviewDetail',
  components: {
    appUpdateModal: updateModal,
  },
  data: function () {
    return {
      myMovieRate2: 0,
    }
  },
  props: {
    review: {
      type: Object,
    },
    movie: {
      type: Object
    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    // close2:function () {
    //   this.show2 = false
    // },
    // 리뷰수정
    reviewModify: function() { //수정버튼 눌렀을 때 
      this.visible = !this.visible
        // this.show2 = true
        console.log(this.visible)
    },
    update: function (review) {
    console.log('업데이트 함수 들어옴')
    const config = this.getToken()
    const reviewItem = {
      title: this.title,
      content: this.content,
      rank: this.myMovieRate2,
      movie: review.movie,
    }
    axios.put(`${SERVER_URL}/movies/review/${review.id}/`, reviewItem, config)
    .then( (res) => {
      if (res.data.message) {
        alert("본인이 작성한 글만 수정 가능합니다!")
      }
      else {
        // this.close2()
        this.$emit("reviews-updated")
      }
    })
    .catch( (err) => {
      console.log(err)
    })
    },
   // 리뷰 삭제
    reviewDelete: function(review) {
      console.log('삭제된다')
      
          // if (res.data.message) {
          //   alert("본인이 작성한 글만 삭제 가능합니다!")
            
          // }
          // else {
            this.$emit('reviewDelete',review.id)
          // }
        
    },

    
  },
  watch: {
    visible: function () {
      
    }

  }
}
</script>

<style>

</style>