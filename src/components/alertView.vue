<template>
    <div class="alert-view" :style="`top: ${topPos}px;`">
        <div style="width: 100%; height: 100%; position: relative;">
            <div class="close" @click="emits('alertViewClose', 0)"></div>
        </div>
        <div style="box-sizing: border-box; padding: 50px 50px;">
            <div style="display:block; width: 25px; height: 25px; background-color: var(--blue);"></div>
            <slot></slot>
        </div>
    </div>
    <div
        @click="emits('alertViewClose', 0)" 
        :style="`display: block; position: absolute; top: 0; left: 0; background-color: #d3d3d3; width: 100%; height: ${bodyHeight}px; z-index: 101; background-color: rgba(0, 0, 0, 0.4);`">
    </div>
</template>

<script setup>
import { onMounted, ref, onBeforeUnmount } from 'vue';
const props = defineProps({
    topPos: Number
});
const emits = defineEmits(["alertViewClose"]);

// 让黑边框更适配页面
const bodyHeight = ref(0);
const ready = () => {
    bodyHeight.value = document.querySelector("html").scrollHeight;
}
let aTid = 0;
onMounted(() => {
    aTid = setInterval(() => {
        if(bodyHeight != document.querySelector("html").scrollHeight) ready();
    }, 100);
});
onBeforeUnmount(() => {
    clearInterval(aTid);
});
</script>

<style scoped>
.alert-view {
    display: block;
    position: absolute;
    width: 100%;
    min-height: 64px;
    max-width: 1200px;
    border-radius: 20px;
    box-shadow: var(--grey) 20px 20px 20px;
    background-color: var(--bg2);
    z-index: 102;
}
.alert-view .close {
    display: block;
    width: 32px;
    height: 32px;
    position: absolute;
    right: 16px;
    top: 16px;
    cursor: pointer;
}
.alert-view .close::before {
    content: "";
    width: 32px;
    height: 0px;
    border: 3px solid #000;
    border-radius: 3px;
    transform: translate(-11px, 1px) rotate(-45deg);
    transform-origin: top right;
    position: absolute;
    top: 0;
    left: 0;
}
.alert-view .close::after {
    content: "";
    width: 32px;
    height: 0px;
    border: 3px solid #000;
    border-radius: 3px;
    transform: translate(27px, 32px) rotate(-135deg);
    transform-origin: top left;
    position: absolute;
    top: 0;
    left: 0;
}
</style>