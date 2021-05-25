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
      <!-- <b-modal
        hide-footer
        v-model="show2"
        id="review-modal"
        size="lg"
        :title="review.title"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
        :body-bg-variant="bodyBgVariant"
        :body-text-variant="bodyTextVariant"
        :footer-bg-variant="footerBgVariant"
        :footer-text-variant="footerTextVariant"
      > -->
      <!--뺏다넣었다하면 됨 v-if="reviewModify(review)" -->
      <app-update-modal  title="리뷰 수정" :visible.sync="visible">
        <hr>
        <!-- <section class="page-section" id="contact"> -->
          <!-- <div class="container"> -->
              <!-- Contact Section Heading-->
              <h2>리뷰 수정</h2>
              <!-- Contact Section Form-->
              <div class="row">
                  <div class="col-lg-8 mx-auto">
                      <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19.-->
                    <div>
                        <div>
                            <label>리뷰 제목:</label>
                            <input v-model.trim="title" class="form-control" id="reviewTitle" type="text" :placeholder="review.title" required="required" data-validation-required-message="Please enter your review title." />
                            <p class="help-block text-danger"></p>
                        </div>
                    </div>

                        <div class="st-font form-group floating-label-form-group controls mb-0 pb-2">
                            <label>영화 제목: {{ movie.title }}</label>
                            <!-- <p class="help-block text-danger"></p> -->
                        </div>
                      <span>내가 생각하는 영화 평점:</span>
                      <select v-model="myMovieRate" id="myMovieRate">
                        <option>5</option>
                        <option>4</option>
                        <option>3</option>
                        <option>2</option>
                        <option>1</option>
                      </select>

                        <div>
                            <label>리뷰 내용</label>
                            <textarea v-model.trim="content" class="form-control" id="content" rows="5" :placeholder="review.content" required="required" data-validation-required-message="Please enter a content."></textarea>
                            <!-- <p class="help-block text-danger"></p> -->
                        </div>
                    <br />
                    <div id="success"></div>
                    <div class="text-white st-font form-group"><button @click="update(review)" class="btn btn-secondary btn-xl" id="sendMessageButton" type="submit">수정 !</button></div>
                  </div>
              </div>
          <!-- </div> -->
        <!-- </section> -->
        <!-- <div class="text-white st-font form-group">
          <button @click="close2" class="btn btn-secondary m-1" id="sendMessageButton" type="submit">수정 창 닫기</button>
        </div> -->
      <!-- </b-modal> -->
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
  // data: function () {
  //   return {
  //     show2:false,
  //   }
  // },
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
    reviewModify: function() {
      this.visible = !this.visible
        // this.show2 = true
        console.log(this.visible)
    },
    update: function (review) {
    const config = this.getToken()
    const reviewItem = {
      title: this.title,
      content: this.content,
      rank: this.myMovieRate,
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
      const config = this.getToken()
      axios.delete(`${SERVER_URL}/movies/review/${review.id}/`, config)
        .then((res) => {
          if (res.data.message) {
            alert("본인이 작성한 글만 삭제 가능합니다!")
          }
          else {
            this.$emit('reviewDelete')
          }
        })
    },

    // created: function () {
    //   this.close2()
    // },
  }
}
</script>

<style>

</style>