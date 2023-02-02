<script setup>
import Plotly from "plotly.js-dist";
import $ from "jquery";
import { onMounted, ref } from "vue";
import SuperGif from "../../lib/libgif";

const emits = defineEmits(["alertOpen"]);
const alertOpen = function() {
    emits("alertOpen", "alertDemographics");
}
const icon = ref([
    { iconUrl: "./assets/target.png", num: 3, tit: "Studys" },
    { iconUrl: "./assets/meeting.png", num: "19,532", tit: "Participants" },
    { iconUrl: "./assets/team.png", num: 19, tit: "Regions" },
    { iconUrl: "./assets/language-learning.png", num: 10, tit: "Languages" },
]);
const studyInfo = ref([
    { id: 1, tit: "Explore the formation of FAVEE model", content: "5D representational space is referred to as the FAVEE model (abbreviations for Formality, Activeness, Valence, Exchange, and Equality), which is a unified cognitive space." },
    { id: 2, tit: "Explore the formation of HPP model", content: "Categorical model consists of 3 clusters ‘Hostile, Private and Public’ (abbreviated as ‘HPP’ model). Compare relationship categories with dimensions." },
    { id: 3, tit: "Explore universality and cultural variability of FAVEE-HPP model", content: "FAVEE-HPP model is both universal and culturally variable. Within the FAVEE-HPP model, you can explore your interesting relationship in detail." }
]);
function heightToTop(ele){
    //ele为指定跳转到该位置的DOM节点
    let root = document.body;
    let height = 0;
    do{
        height += ele.offsetTop;
        ele = ele.offsetParent;
    }while( ele !== root )
    return height;
}
const stuClick = function(e) {
    $(".container").animate({
        scrollTop: heightToTop($("#study" + e.toString()).get(0))
    }, {
        duration: 500,
        easing: "swing"
    })
}
onMounted(() => {
        // var run = new SuperGif({
        //     gif: document.getElementById("mainGif"),
        //     c_w: 400,
        //     c_h: 400,
        //     max_width: 400
        // });
        // run.load(() => {
        //     run.play();
        // });
});
</script>

<template>
    <div class="box">
        <div class="title">
            <span>O</span>verview
        </div>
        <div class="mid">
            <div class="show" v-for="i in icon">
                <div class="bg" :style="'background: url(' + i.iconUrl + ') center center / 64px 64px no-repeat;'">
                </div>
                <div class="num">{{ i.num }}</div>
                <div class="tit">{{ i.tit }}</div>
            </div>
        </div>
        <div style="line-height: 24px; font-size: 16px; margin: 20px 0;">
            Learn more about <span style="color: var(--theme-color-blue); cursor: pointer;" @click="alertOpen">demographics ></span>
        </div>
        <div class="bottom">
            <div id="main">
                <!-- <img src="/assets/favee-3d.gif" alt="" rel:animated_src="./assets/favee-3d.gif" rel:auto_play="1" width="400" height="400" id="mainGif"> -->
                <video src="/assets/favee-3d.mp4" autoplay="autoplay" loop></video>
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
    </div>
</template>

<style scoped>
.box {
    width: 100%;
    position: relative;
}

.title {
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
    text-align: left;
    margin: 70px 0 0 68px;
}

.title>span {
    color: var(--theme-color-blue);
}

.show {
    display: inline-block;
    margin: 0 calc((100% - 200px * 4) / 8);
}

.show .bg {
    width: 96px;
    height: 96px;
    border: 3px solid var(--theme-color-blue);
    border-radius: 50%;
}

.show .num {
    font-size: 20px;
    letter-spacing: 2px;
    font-weight: 700;
    margin: 30px 0 0 0;
}

.show .tit {
    margin: 10px 0 0 0;
    font-size: 16px;
}
.bottom {
    margin: 0 0 50px 0;
}
.bottom>div {
    vertical-align: middle;
}
.studyBox {
    display: inline-block;
    width: 600px;
    margin: 0 0 0 80px;
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

#main {
    display: inline-block;
    width: 400px;
    height: 400px;
    overflow: hidden;
}
#main video {
    width: 100%;
    height: 100%;
}
</style>