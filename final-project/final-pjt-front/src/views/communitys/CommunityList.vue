<template>
  <div>
    <ul>
      <li v-for="(community, idx) in communitys" :key="idx">
        <span @click="updateCommunityStatus(community)" :class="{ completed: community.completed }">{{ community.title }}</span>
        <button @click="deleteCom(community)" class="community-btn">X</button>
      </li>
    </ul>
    <button @click="getCommunitys">Get Communitys</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommunityList',
  data: function () {
    return {
      communitys: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        }
      }
      return config
    },
    getcommunitys: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/communitys/`, config)
        .then((res) => {
          console.log(res)
          this.communitys = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deletecommunity: function (community) {
      const config = this.setToken()
      axios.delete(`${SERVER_URL}/communitys/${community.id}/`, config)
        .then((res) => {
          console.log(res)
          // 1. findIndex(array helper methods)로 응답받은 아이디와 일치하는 요소의 index 찾기
          const targetCommunityIdx = this.communitys.findIndex((community) => {
            return community.id === res.data.id
          })
          // 2. 기존 배열(this.communitys)에서 삭제한(target) community를 삭제
          this.communitys.splice(targetCommunityIdx, 1)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updatecommunityStatus: function (community) { // community는 클릭한 community를 의미
      const config = this.setToken()
      const communityItem = {
        ...community, // spread operator -> communityItem의 속성중에서 completed만 변경하려고 사용
        completed: !community.completed
      }

      axios.put(`${SERVER_URL}/communitys/${community.id}/`, communityItem, config)
        .then((res) => {
          console.log(res)
          community.completed = !community.completed
        })
      },
    },
  created: function () {
    this.getcommunitys()
  }
}
</script>

<style scoped>
  .community-btn {
    margin-left: 10px;
  }

  .completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>