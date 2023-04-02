<template>
  <div v-show="visible" class="dialog-content main">
    <img src="@/assets/img/home/dialog_close.png" alt="" @click="onClose" class="close-btn" />
    <div class="dialog-block"></div>
    <div class="dialog-text">
      <slot></slot>
    </div>
  </div>
</template>
<script setup>
const prop = defineProps({
  visible: {
    type: Boolean,
    default: false
  }
})
const emits = defineEmits(['update:visible'])
const onClose = () => {
  emits('update:visible', false)
}
</script>
<style lang="scss" scoped>
.dialog-content {
  position: relative;
  display: flex;
  flex-direction: column;
  text-align: left;
  align-items: flex-start !important;
  border-radius: 20px;
  padding: 2rem 2rem 1rem;
  background: rgba(255, 255, 255, 1);
  box-shadow: 0px 0px 15px 4px rgba(0, 0, 0, 0.25);

  .close-btn {
    position: absolute;
    right: 63px;
    width: 24px;
    height: 24px;
    top: 48px;
    cursor: pointer;
  }

  .dialog-block {
    width: 25px;
    height: 25px;
    background-color: var(--theme-color-blue);
    margin-bottom: 4px;
  }

  .dialog-text {
    font-size: 16px;
    line-height: 24px;
  }
}

@media screen and (max-width: 600px) {
  .dialog-content {
    position: relative;
    display: flex;
    flex-direction: column;
    text-align: left;
    align-items: flex-start !important;
    border-radius: 20px;
    padding: 2rem;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 0px 15px 4px rgba(0, 0, 0, 0.25);

    .close-btn {
      right: 23px;
      width: 16px;
      height: 16px;
      top: 28px;
    }

    .dialog-block {
      width: 16px;
      height: 16px;
      margin-bottom: 10px;
    }

    .dialog-text {
      font-size: 1.4rem;
      line-height: 1.6rem;
    }
  }
}
@media (min-width: 600px) and (max-width: 900px) {
  .dialog-content {
    padding: 2rem 3rem;

    .close-btn {
      right: 23px;
      width: 16px;
      height: 16px;
      top: 16px;
    }

    .dialog-block {
      width: 16px;
      height: 16px;
      margin-bottom: 10px;
    }

    .dialog-text {
      font-size: 14px;
      line-height: 16px;
    }
  }
}
</style>