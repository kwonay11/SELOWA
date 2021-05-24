<template>
  <div>
    <button @click="handleClickButton">Toggle Modal</button>
    <app-my-modal
      title="This is modal"
      :visible.sync="visible">
      <div>
        {{ movie.title }}
      </div>
    </app-my-modal>
  </div>
</template>

<script>
import myModal from './myModal'
export default {
  name: 'MovieDetail',
  props: {
        movie:{
            type: Object,
        },
  },
  data: function () {
    return {
      visible: false,
    }
  },
  components: {
    appMyModal: myModal
  },
  methods: {
    handleClickButton(){
      this.visible = !this.visible
    } 
  }
}
</script>

<style>
</style>