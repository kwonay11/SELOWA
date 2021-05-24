<template>
<transition name="modal" appear>
  <div class="my-modal" 
    v-if="visible" @click.self="handleWrapperClick">
    <div class="my-modal__dialog">
      <header class="my-modal__header">
        <span>{{title}}</span>
        <!-- update:visible', !visible 모달 바깥을 클릭해서 모달을 닫음 -->
        <button @click="$emit('update:visible', !visible)" class ="btn btn-outline-danger m-4">X</button>
      </header>
      <div class="my-modal__body">
        <slot></slot>
      </div>
    </div>
  </div>
</transition>
</template>

<script>
export default {
  name: 'my-modal',
  props: {
    visible: {
      type: Boolean,
      require: true,
      default: false
    },
    title: {
      type: String,
      require: false,
    },
  },
  methods: {
    handleWrapperClick(){
      this.$emit('update:visible', false)
    },
  },
}
</script>

<style lang="scss">
$module: 'my-modal';
.#{$module} {
  // This is modal bg
  align-items: center;
  justify-content: center;
  // 모달이 맨 위로 나오게 하기
  z-index: 30;
    top: 0;
    left: 0;
  background-color: rgba(0,0,0,.7);
  top: 0; right: 0; bottom: 0; left: 0;
  position: fixed;
  overflow: auto;
  margin: 0;
  //This is modal layer
  &__dialog{
    left: 35%;
    top: 75px;
    width: 600px;
    position: absolute;
    background: rgb(170, 130, 130);
    margin-bottom: 50px;
  }

  &__header {
    font-size: 28px;
    font-weight: bold;
    line-height: 1.29;
    padding: 16px 16px 0 25px;
    position: relative;
  }
  &__body {
    padding: 25px;
    min-height: 150px;
    max-height: 412px;
    overflow-y: scroll;
  }
}
</style>