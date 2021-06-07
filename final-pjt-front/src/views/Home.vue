<template>
  <div>
    <br>
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

#nc-main {
    position: relative;
    height: 100vh;
    overflow-x: hidden;
    -webkit-box-shadow: 0 0 30px #241d20;
    box-shadow: 0 0 30px #241d20;
    -webkit-transition: -webkit-transform 0.4s;
    transition: -webkit-transform 0.4s;
    transition: transform 0.4s;
    transition: transform 0.4s, -webkit-transform 0.4s;
}

#nc-main
{
  background-image: url("https://images.unsplash.com/photo-1486241975555-382b4ae9e12f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1567&q=80");
}

.full-wh {
    position: absolute;
    top: 0px;
    left: 0px;
    bottom: 0px;
    width: 100%;
}

.bg-animation {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

</style>