<template>

  <div class="row d-flex justify-content-center align-items-center " >
  <div>
    <h2 style="margin-bottom:30px">제목을 옆 버튼을 눌러 상세페이지로, 유저를 눌러 프로필로 넘어가보세요</h2>
    <div class="row d-flex justify-content-center align-items-center " >
      <div class="card text-white bg-dark m-3 p-5 row d-flex justify-content-center align-items-center" style="width: 40%; ">
      <div class="col-lg-8 col-md-10 mx-auto">
        <div style="cursor:pointer;" v-for="(community, idx) in communities" :key="idx">
            <h3 @click="DetailCommunity(community)">{{community.id}}번 글</h3>
            <h2>{{community.title}}</h2>
            <button  @click="DetailCommunity(community)" class ="btn btn-outline-danger">Detail</button>
            <h4>{{community.content}}</h4>
          <p  @click="moveToProfile(community.user, community.userName)">Written by
              {{community.userName}}
          </p>
        <hr>
        </div>
      </div>
    </div>
    </div>
  </div>

</div>
</template>


<script>
export default {
  name: 'CommunityList',
  props: {
    // Community에서 v-for을 이용해 보내준 게시글 한개의 데이터를 props를 통해 받고 보여준다.
    communities: [Array, Object]
  },
  methods: {
    DetailCommunity: function (community) {
      // console.log(community)
      // this.$store.dispatch('createDetailCommunity', community)
      this.$router.push({ name: 'CommunityDetail', params: { community_pk: `${community.id}` }})
    },
    moveToProfile: function (user, username) {
      // console.log(user)
      this.$router.push({ name: "Profile", params: { user_pk: `${user}`, username: `${username}` }})
    },    
  }
}
</script>

<style>
</style>