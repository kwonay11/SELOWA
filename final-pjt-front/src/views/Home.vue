<template>
  <div>
    <br>
    <div class='column'>
  <div class='search'>
    <div class='search_bar'>
      <input id='searchOne' type='checkbox'>
      <label for='searchOne'>
        <i class="fas fa-search font-weight-bolder " ></i>
        <!-- <i class='fas fa-times font-weight-bolder'></i> -->
        <p>|</p>
      </label>
      <input placeholder='Search...' type='text'>
    </div>
  </div>
</div>
    <div class="container">
  <div class="row">
    <div class="col-md-3">
      <div @click="Movie" class="card card-1">
        <h3>Total Movie</h3>
        <br>
        <!-- <background-image src="@/assets/1.png" alt="1" > -->
        <p>Get movie data using TMDB API. There are 100 data. Click the View Details button to view information about the movie. You can also register a review.</p>
      </div>
    </div>
    <div class="col-md-3">
      <div @click="Recommend" class="card card-2">
        <h3>Recommend Movie</h3>
        <br>
        <p>This page offers movie recommendations. There are about three. Randomly recommends 30 movies, other people's likes based on my likes data, high rating-based recommendations.</p>
      </div>
    </div>
    <div class="col-md-3">
      <div @click="Community" class="card card-3">
        <h3>Community</h3>
        <br>
        <p>This is a community page. You can tell your own story with Selowa users. There is also a function to register a comment under the article. Only you can edit or delete posts and comments..</p>
      </div>
    </div>
    <div class="col-md-3">
      <div @click="Profile" class="card card-4">
        <h3>Profile</h3>
        <br>
        <p>This is your profile page. You can watch your favorite movies. Not only that, but my personal information is also displayed. have a nice day.</p>
      </div>
    </div>
  </div>
</div>
    <!-- <div>
     <h1 style="text-align:center" class="m-2">Welcome to the SELOWA!</h1>
     <img src="@/assets/apeach2.png" alt="apeach2">
     </div>
      <video width="1300px" src="@/assets/video.mp4" controls autoplay muted></video> -->
    </div>
</template>

<script>
export default {
    name:"Home",
     methods: {
    Movie: function () {
        this.$router.push({ name: 'Movie' })
      },
    Recommend: function () {
        this.$router.push({ name: 'Recommend' })
      },
    Community: function () {
        this.$router.push({ name: 'Community' })
      },
    Profile: function () {
        this.$router.push({ name: 'MyProfile' })
      }
    }
}
</script>

<style scoped>
body{
  font-family: 'Nunito', sans-serif;
  padding: 50px;
}
.card{
  border: 1px solid rgb(107, 70, 85);
  height: 400px;
    border-radius: 4px;
    background: rgb(13, 20, 17);
    box-shadow: 0 6px 10px rgba(197, 194, 194, 0.08), 0 0 6px rgba(0,0,0,.05);
      transition: .3s transform cubic-bezier(.155,1.105,.295,1.12),.3s box-shadow,.3s -webkit-transform cubic-bezier(.155,1.105,.295,1.12);
  padding: 14px 80px 18px 36px;
  cursor: pointer;
}

.card:hover{
  
     transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(230, 219, 219, 0.87), 0 4px 8px rgba(214, 204, 204, 0.904);
}

.card h3{
  font-weight: 600;
}

.card img{
  position: absolute;
  top: 20px;
  right: 15px;
  max-height: 100px;
}

.card-1{
  background-image: url(https://image.flaticon.com/icons/png/512/4221/4221844.png);
 /* <a href="https://www.flaticon.com/kr/authors/iconixar" title="iconixar">iconixar</a> from <a href="https://www.flaticon.com/kr/" title="Flaticon">www.flaticon.com</a> */
      background-repeat: no-repeat;
    background-position: right;
    background-size: 100px;
    text-align: left;
}

.card-2{
   background-image: url(https://image.flaticon.com/icons/png/512/4221/4221859.png);
   
      background-repeat: no-repeat;
    background-position: right;
    background-size: 100px;
    text-align: left;
}

.card-3{
   background-image: url(https://image.flaticon.com/icons/png/512/4221/4221392.png);
    background-repeat: no-repeat;
    background-position: right;
    
     background-size: 100px;
    text-align: left;
}

.card-4{
   background-image: url(https://image.flaticon.com/icons/png/512/4221/4221843.png);
      background-repeat: no-repeat;
    background-position: right;
  
    background-size: 100px;
    
    text-align: left;
}

@media(max-width: 990px){
  .card{
    margin: 20px;
  }
} 

.column {
  /* background: #F6F792; */
  height: 90px;
  float: left;
  width: 100%;
  position: relative;
}
.search {
  position: absolute;
  left: 0;
  right: 0;
  margin: auto;
  top: 30%;
  transform: translateY(-50%);
  width: 100%;
  text-align: center;
  overflow: hidden;
}
.search_bar {
  width: 280px;
  position: relative;
  margin: 0 auto;
}
.search_bar input[type=text] {
  width: 15px;
  background: transparent;
  transition: border 0.3s 0s, width 0.2s 0.3s cubic-bezier(0.225, 0.01, 0.475, 1.01), text-indent 0.2s 0.3s;
  padding: 20px;
  border-color: #441ee9;
  text-indent: 30px;
  outline: none;
  border: 0px solid #441ee9;
  font-size: 15px;
  color: #ac88e7;
  border-radius: 5px;
  font-family: "Nunito", sans-serif;
}
.search_bar ::-webkit-input-placeholder {
  /* Safari, Chrome and Opera */
  color: #441ee9;
  font-weight: 400;
  font-family: "Nunito", sans-serif;
}
.search_bar ::-moz-input-placeholder {
  /* Safari, Chrome and Opera */
  color: #441ee9;
  font-weight: 400;
  font-family: "Nunito", sans-serif;
}
.search_bar ::-o-input-placeholder {
  /* Safari, Chrome and Opera */
  color: #441ee9;
  font-weight: 400;
  font-family: "Nunito", sans-serif;
}
.search_bar input[type=checkbox] {
  display: none;
}
.search_bar input[type=checkbox]:checked + label + input {
  width: 230px;
  border: 5px solid #441ee9;
  text-indent: 0px;
}
.search_bar input[type=checkbox]:checked + label i {
  right: 0px;
  transform: translateY(-50%) translateX(50%) rotate(360deg) scale(0);
  color: #441ee9;
}
.search_bar input[type=checkbox]:checked + label .last {
  left: 220px;
  transform: translateY(-50%) rotate(360deg) scale(1);
}
.search_bar input[type=checkbox]:checked + label p {
  top: 50%;
  transition: all 0.3s 0.45s;
}
.search_bar input[type=checkbox]:not(checked) + label p {
  top: -50%;
  transition: all 0.3s 0s;
}
.search_bar .last {
  transform: translateY(-50%) rotate(0deg) scale(0);
}
.search_bar i {
  position: absolute;
  font-size: 30px;
  top: 50%;
  transform: translateY(-50%) translateX(50%) rotate(0deg) scale(1);
  cursor: pointer;
  z-index: 2;
  margin: auto;
  border-radius: 4px;
  width: 56px;
  right: 50%;
  height: 54px;
  background: transparent;
  transition: right 0.3s 0.3s, transform 0.3s 0.3s, color 0.3s;
  line-height: 60px;
  color: #eb1e8e;
}
.search_bar i:hover {
  color: #441ee9;
}
.search_bar p {
  position: absolute;
  margin: 0;
  right: 52px;
  color: #441ee9;
  font-weight: 700;
  font-size: 30px;
  top: -50%;
  transform: translateY(-50%) rotate(0deg) scale(1);
}

</style>