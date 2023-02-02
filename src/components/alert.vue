<script setup>
const props = defineProps({
    view: {
        type: String,
        default: ""
    }
});
const emits = defineEmits(["alertCancel"]);

</script>
<template>
    <div class="bg" @click="emits('alertCancel');"></div>
    <div class="box">
        <div class="cancel" @click="emits('alertCancel');"></div>
        <router-view :name="view"></router-view>
    </div>
</template>

<style scoped>
.bg {
    width: 100%;
    max-width: 1440px;
    height: 100%;
    background: rgba(0,0,0,0.1);
    position: absolute;
    left: 0;
    top: 0;
    z-index: 1;
    overflow: hidden scroll;
}
.box {
    width: 100%;
    height: 90%;
    background: #fff;
    border-radius: 15px 15px 0 0;
    box-shadow: 0px 2px 13px 0px black;
    position: absolute;
    bottom: 0;
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