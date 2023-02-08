<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue';

const props = defineProps({
    view: {
        type: String,
        default: ""
    }
});
const emits = defineEmits(["alertCancel"]);

const alertTop = ref(0);
onMounted(() => {
    alertTop.value = document.querySelector("html").scrollTop;
    document.querySelector("body").onscroll = (e) => {
        alertTop.value = document.querySelector("html").scrollTop;
    };
});
onBeforeUnmount(() => {
    document.querySelector("body").onscroll = (e) => {};
});
</script>
<template>
    <div class="bg" @click="emits('alertCancel');" :style="'top: ' + alertTop + 'px;'"></div>
    <div class="box" :style="'top: calc(10% + ' + alertTop + 'px);'">
        <div class="cancel" @click="emits('alertCancel');"></div>
        <div class="tt">
            <router-view :name="view"></router-view>
        </div>
    </div>
</template>

<style scoped>
.tt {
    width: 100vw;
    height: 80%;
    margin: 2% 0;
    overflow: hidden scroll;
}
.bg {
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.1);
    position: absolute;
    left: 0;
    z-index: 1;
    overflow: hidden;
}

.box {
    width: 100vw;
    height: 90%;
    background: #fff;
    border-radius: 15px 15px 0 0;
    box-shadow: 0px 2px 13px 0px black;
    position: absolute;
    z-index: 2;
}

.cancel {
    width: 32px;
    height: 32px;
    position: absolute;
    top: 18px;
    right: 18px;
    cursor: pointer;
}

.cancel::before {
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

.cancel::after {
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