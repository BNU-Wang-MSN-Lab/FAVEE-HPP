<template>
    <div class="alert-view" :style="`top: ${topPos}px;`">
        <div style="width: 100%; height: 100%; position: relative;">
            <div class="close" @click="emits('alertViewClose', 0)"></div>
        </div>
        <div style="box-sizing: border-box; padding: 50px 50px;">
            <div>
                <selButton @hook:mounted="ready" @choooseOpt="selButtonEvent" :buttonLabels="buttonLabels">aaass</selButton>
            </div>
            <div style="display:block; width: 25px; height: 25px; background-color: var(--blue);"></div>
            <slot></slot>
        </div>
        <div class="button-box">
            <cho-button-no-bg @click="hrefClick('https://osf.io/nfkmj')" @hook:mounted="ready">Download Data and Survey</cho-button-no-bg>
        </div>
    </div>
    <div
        @click="emits('alertViewClose', 0)" 
        :style="`display: block; position: absolute; top: 0; left: 0; background-color: #d3d3d3; width: 100%; height: ${bodyHeight}px; z-index: 101; background-color: rgba(0, 0, 0, 0.4);`">
    </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref, provide } from 'vue';
import selButton from '../../../../components/selButton.vue';
import choButtonNoBg from '../../../../components/choButtonNoBg.vue';
const buttonLabels = "Dimensional Model-Categorical Model-Demographics";
const currPage = ref(0);
provide("currPage", currPage);
const selButtonEvent = (e) => {
    currPage.value = buttonLabels.split("-").indexOf(e);
}
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

const hrefClick = (e) => {
  let a = document.createElement("a");
  a.href = e;
  a.target = "_blank"
  a.click();
}
</script>

<style scoped>
.alert-view {
    display: block;
    position: absolute;
    width: 100%;
    min-height: 64px;
    max-width: 1200px;
    border-radius: 20px;
    box-shadow: var(--grey) 0px 20px 20px;
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
    border: 3px solid var(--font-color-body);
    background-color: var(--font-color-body);
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
    border: 3px solid var(--font-color-body);
    background-color: var(--font-color-body);
    border-radius: 3px;
    transform: translate(27px, 32px) rotate(-135deg);
    transform-origin: top left;
    position: absolute;
    top: 0;
    left: 0;
}
.button-box {
    display: flex;
    justify-content: center;
    margin: 20px 0;
}
</style>