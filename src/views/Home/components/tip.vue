<template>
  <div class="box" v-if="type==1">
    <div class="f1"></div>
    <div class="f2">
        <div class="f3"></div>
    </div>
    <div class="f4"></div>
  </div>
  <div class="box" v-if="type==3">
    <div class="f31"></div>
    <div class="f32">
        <div class="f33"></div>
    </div>
    <div class="f34"></div>
  </div>
  <div class="box" v-if="type==2">
    <div class="f5"></div>
    <div class="f6"></div>
    <div class="f7"></div>
  </div>
</template>
<script setup>
const prop = defineProps({
    type: {
        default: 1
    }
})
</script>
<style lang="scss" scoped>
.box {
    display: inline-block;
    position: relative;
    .f1 {
        position: absolute;
        left: 0;
        top: 0;
        transform: translateX(-100%);
        width: 8px;
        height: 8px;
        background-color: var(--theme-color-blue);
    }
    .f2 {
        width: 19px;
        height: 19px;
        position: relative;
        background-color: var(--theme-color-orange);
    }
    .f3 {
        position: absolute;
        bottom: 0;
        right: 0;
        width: 11px;
        height: 11px;
        background-color: rgba(255, 211, 175, 1);
    }
    .f4 {
        position: absolute;
        bottom: 0;
        right: 0;
        width: 11px;
        height: 11px;
        transform: translateY(100%);
        background-color: var(--theme-color-blue);
    }
    .f31 {
        position: absolute;
        bottom: 0;
        left: 0;
        transform: translateX(-100%);
        width: 8px;
        height: 8px;
        background-color: var(--theme-color-blue);
    }
    .f32 {
        width: 19px;
        height: 19px;
        position: relative;
        background-color: var(--theme-color-orange);
    }
    .f33 {
        position: absolute;
        bottom: 0;
        right: 0;
        width: 11px;
        height: 11px;
        background-color: rgba(255, 211, 175, 1);
    }
    .f34 {
        position: absolute;
        top: 0;
        right: 0;
        width: 11px;
        height: 11px;
        transform: translateY(-100%);
        background-color: var(--theme-color-blue);
    }
    .f5 {
        width: 16px;
        height: 25px;
        background-color: var(--theme-color-orange);
    }
    .f6 {
        width: 16px;
        height: 63px;
        background-color: rgba(255, 211, 175, 1);
    }
    .f7 {
        width: 16px;
        height: 16px;
        background-color: var(--theme-color-blue);
    }
}
@media screen and (max-width: 600px) {
    .box {
    display: inline-block;
    position: relative;
    .f1 {
        position: absolute;
        left: 0;
        top: 0;
        transform: translateX(-100%);
        width: 10px;
        height: 10px;
        background-color: var(--theme-color-blue);
    }
    .f2 {
        width: 18px;
        height: 18px;
        position: relative;
        background-color: var(--theme-color-orange);
    }
    .f3 {
        position: absolute;
        bottom: 0;
        right: 0;
        width: 12px;
        height: 12px;
        background-color: rgba(255, 211, 175, 1);
    }
    .f4 {
        position: absolute;
        bottom: 0;
        right: 0;
        width: 12px;
        height: 12px;
        transform: translateY(100%);
        background-color: var(--theme-color-blue);
    }
    .f5 {
        width: 16px;
        height: 20px;
        background-color: var(--theme-color-orange);
    }
    .f6 {
        width: 16px;
        height: 76px;
        background-color: rgba(255, 211, 175, 1);
    }
    .f7 {
        width: 16px;
        height: 16px;
        background-color: var(--theme-color-blue);
    }
}
}
</style>