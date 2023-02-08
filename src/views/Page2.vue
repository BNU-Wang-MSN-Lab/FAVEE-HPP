<script setup>
import $ from "jquery";
import { onMounted, ref } from "vue";

const emits = defineEmits(["alertOpen"]);
const alertOpen = function () {
    emits("alertOpen", "alertDemographics");
}
const icon = ref([
    { iconUrl: "./assets/icon/target.png", num: 3, tit: "Studys" },
    { iconUrl: "./assets/icon/meeting.png", num: "19,532", tit: "Participants" },
    { iconUrl: "./assets/icon/team.png", num: 19, tit: "Regions" },
    { iconUrl: "./assets/icon/language-learning.png", num: 10, tit: "Languages" },
]);
const studyInfo = ref([
    { id: 1, tit: "FAVEE model", content: "5D representational space is referred to as the FAVEE model (abbreviations for Formality, Activeness, Valence, Exchange, and Equality), which is a unified cognitive space." },
    { id: 2, tit: "HPP model", content: "Categorical model consists of 3 clusters ‘Hostile, Private and Public’ (abbreviated as ‘HPP’ model). Compare relationship categories with dimensions." },
    { id: 3, tit: "FAVEE-HPP model and its cultural variation", content: "FAVEE-HPP model is both universal and culturally variable. Within the FAVEE-HPP model, you can explore your interesting relationship in detail." }
]);
function heightToTop(ele) {
    //ele为指定跳转到该位置的DOM节点
    let root = document.body;
    let height = 0;
    do {
        height += ele.offsetTop;
        ele = ele.offsetParent;
    } while (ele !== root)
    return height;
}
const stuClick = function (e) {
    console.log(heightToTop($("#study" + e.toString()).get(0)));
    $("html").animate({
        scrollTop: heightToTop($("#study" + e.toString()).get(0))
    }, {
        duration: 500,
        easing: "swing"
    })
}
</script>
<template>
    <div class="box">
        <div class="title">
            Research Overview
        </div>
        <div class="show">
            <div v-for="i in icon">
                <div class="bg" :style="'background: url(' + i.iconUrl + ') center center / 64px 64px no-repeat;'">
                </div>
                <div class="num">{{ i.num }}</div>
                <div class="tit">{{ i.tit }}</div>
            </div>
        </div>
        <div class="subtitle">
            Learn more about <span style="color: var(--theme-color-blue); cursor: pointer;"
                @click="emits('alertOpen', 'alertDemographics')">demographics ></span>
        </div>
        <div class="img">
            <video style="width:100%;" autoplay="autoplay" loop="loop" src="/assets/video/favee-3d.mp4"></video>
        </div>
        <div class="studyBox">
            <div class="study" v-for="i in studyInfo">
                <div>
                    Study {{ i.id }}:
                </div>
                <div @click="stuClick(i.id)" style="cursor: pointer;">
                    {{ i.tit }}
                </div>
                <div>
                    {{ i.content }}
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.box {
    grid-template-rows: 20px 70px 220px 24px 410px 40px;
    grid-row-gap: 0px;
}

.title {
    grid-area: 2 / 2 / 3 / 10;
    text-align: left;
    font-size: 26px;
    line-height: 1.5em;
    font-weight: 700;
}

.show {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-area: 3 / 2 / 4 / 10;
}

.show>div {
    display: inline-block;
    margin: 0 auto;
}

.show>div .bg {
    width: 96px;
    height: 96px;
    border: 3px solid var(--theme-color-blue);
    border-radius: 50%;
}

.show>div .num {
    font-size: 20px;
    letter-spacing: 2px;
    font-weight: 700;
    margin: 30px 0 0 0;
}

.show>div .tit {
    margin: 10px 0 0 0;
    font-size: 16px;
}

.subtitle {
    grid-area: 4 / 2 / 5 / 10;
}

.img {
    grid-area: 5 / 2 / 7 / 5;
    align-items: center;
}

.studyBox {
    grid-area: 5 / 5 / 7 / 10;
    text-align: left;
}

.study {
    margin: 10px 0;
}

.study>div:nth-child(1) {
    font-size: 16px;
    line-height: 24px;
    font-weight: 700;
}

.study>div:nth-child(2) {
    font-size: 24px;
    line-height: 30px;
    font-weight: 700;
    color: var(--theme-color-blue);
}

.study>div:nth-child(3) {
    font-size: 16px;
    line-height: 24px;
    font-weight: 100;
}
</style>