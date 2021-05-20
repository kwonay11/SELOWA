<template>
  <div>
    <input type="text" v-model.trim="title" @keypress.enter="createCommunity">
    <button @click="createCommunity">+</button>
  </div>
</template>

<script>
import axios from'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateCommunity',
  data: function () {
    return {
      title: '',
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

    createCommunity: function () {
      const config = this.setToken()
      const communityItem = {
        title: this.title,
      }

      if (communityItem.title) {
        axios.post(`${SERVER_URL}/communitys/`, communityItem, config) // axios(url, data, config)
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'ComList' }) // 페이지 이동을 하고 싶을 때 사용.
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
  }
}
</script>