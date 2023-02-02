<script setup>
import { onMounted } from 'vue';
import * as $ from "jquery";
import Plotly from "plotly.js-dist";

const emits = defineEmits(["alertOpen"]);
onMounted(() => {
    $.ajax({
        url: "./data/study/Formality_Activeness.json",
        type: "GET",
        dataType: "json",
        success: (e) => {
            Plotly.newPlot("img1", e);
        }
    })
    $.ajax({
        url: "./data/study/Valence_Exchange.json",
        type: "GET",
        dataType: "json",
        success: (e) => {
            Plotly.newPlot("img2", e);
        }
    })
});
</script>

<template>
    <div class="box">
        <div class="tit">
            <span class="one" id="study1">Study 1</span>
            <br />
            <span class="two">
                <span style="color: var(--theme-color-blue)">A</span> unified representational space
            </span>
        </div>
        <div class="content">
            <p>We use longitude and latitude to travel across the world. For relationship space, we found there are five
                principal dimensions (formality, activeness, valence, exchange, equality) navigating us.</p>
            <div @click="emits('alertOpen', 'alertStudy1')">More details ></div>
        </div>
        <div class="img">
            <div id="legend"></div>
            <div id="img1"></div>
            <div id="img2"></div>
        </div>
    </div>
</template>

<style scoped>
.box {
    width: 100%;
    position: relative;
}

.tit {
    text-align: left;
    margin: 70px 0 0 50px;
}

.tit .one {
    font-size: 24px;
    line-height: 30px;
}

.tit .two {
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}

.content {
    text-align: left;
    width: 60%;
    margin: 40px 0 0 60px;
}

.content>div {
    color: var(--theme-color-blue);
    cursor: pointer;
}

.img {
    width: 1000px;
    height: 600px;
    margin: 20px auto;
    position: relative;
}

.img>div {
    width: 450px;
    display: inline-block;
    margin: 0 20px;
}
#legend {
    display: block;
    width: 290px;
    height: 65px;
    margin: 0 auto;
    background: url(/assets/legend/study1.png) no-repeat;
    background-size: contain;
    /* position: absolute; */
    /* left: calc(50% - 145px); */
    /* top: 0; */
}
</style>