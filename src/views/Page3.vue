<script setup>
import { onMounted } from 'vue';
import $ from "jquery";
import Plotly from "plotly.js-dist";

const emits = defineEmits(["alertOpen"]);
onMounted(() => {
    $.ajax({
        url: "./assets/fuckfeishu/Study1/Formality_Activeness.json",
        type: "GET",
        dataType: "json",
        success: (e) => {
            Plotly.newPlot("fig1", e);
        }
    })
    $.ajax({
        url: "./assets/fuckfeishu/Study1/Valence_Exchange.json",
        type: "GET",
        dataType: "json",
        success: (e) => {
            Plotly.newPlot("fig2", e);
        }
    })
});
</script>

<template>
    <div class="box">
        <div class="s1">
            <span id="study1" style="cursor: pointer; font-size: 20px; line-height: 32px;">Study 1</span>
            <br />
            <span style="font-size: 26px; line-height: 1.5em; font-weight: 700;">
                A unified representational space: FAVEE model
            </span>
            <br />
            <span>
                We use longitude and latitude to travel across the world. In our complex social life, there are a bunch
                of evaluative features to construe relationship space.<br />
                Based on literature review, we collected and summarized 30 theoretical features of relationships from 15
                existing theories in social sciences to encompass the entire feature space.<br />
                By a series of dimensionality reduction techniques, we found <strong>there are five principal dimensions
                    (formality, activeness, valence, exchange, equality) navigating us to seek, sustain, repair, judge,
                    and adjust relationships. This dimensional space is unified and representative across different
                    analytic methods and literatures.</strong>
            </span>
            <br />
            <span @click="emits('alertOpen', 'alertStudy1')"
                style="color: var(--theme-color-blue); cursor: pointer; font-size: 20px; line-height: 32px;">
                More details>
            </span>
        </div>
        <div class="s2">
            <div class="legend">
                <img src="/assets/legend/study1.png" style="height: 100%;" alt="">
            </div>
            <div id="fig1"></div>
            <div id="fig2"></div>
            <div class="caption">
                <span>Hover the mouse over the circle, you can see what relationship it is and its position in FAVEE
                    space.</span>
                <br />
                <span>Zoom in on an area with the mouse by framing it, and click on the enlarged area to restore it to
                    its original size.</span>
            </div>
        </div>
    </div>
</template>

<style scoped>
.box {
    grid-template-rows: 20px auto auto 40px;
    align-items: start;
}

.s1 {
    grid-area: 2 / 2 / 3 / 9;
    text-align: left;
    grid-auto-rows: minmax(40px 1fr);
}

.s2 {
    grid-area: 3 / 3 / 4 / 10;
    text-align: center;
}

.legend {
    width: 290px;
    height: 65px;
    margin: 0 auto;
}

#fig1,
#fig2 {
    display: inline-block;
    width: 450px;
    height: 450px;
}

.caption {
    max-width: 800px;
    text-align: left;
    margin: 0 auto;
}
</style>