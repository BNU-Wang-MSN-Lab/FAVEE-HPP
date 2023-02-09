<script setup>
import $ from "jquery";
import { onMounted } from "vue";
import { newPlot } from "plotly.js-dist";
const emits = defineEmits(["alertOpen"]);
onMounted(() => {
    $.ajax({
        url: "./assets/fuckfeishu/Study2/Interactive/M1.json",
        type: "GET",
        dataType: "json",
        success: (e) => {
            new newPlot("model1", e.data, e.style, e.resp);
        }
    });
    $.ajax({
        url: "./assets/fuckfeishu/Study2/Interactive/M2.json",
        type: "GET",
        dataType: "json",
        success: (e) => {
            new newPlot("model2", e.data, e.style, e.resp);
        }
    });
    $.ajax({
        url: "./assets/fuckfeishu/Study2/Interactive/M3.json",
        type: "GET",
        dataType: "json",
        success: (e) => {
            new newPlot("model3", e.data, e.style, e.resp);
        }
    });
    $.ajax({
        url: "./assets/fuckfeishu/Study2/Interactive/M4.json",
        type: "GET",
        dataType: "json",
        success: (e) => {
            new newPlot("model4", e);
        }
    });
    $.ajax({
        url: "./assets/fuckfeishu/Study2/Interactive/M5.json",
        type: "GET",
        dataType: "json",
        success: (e) => {
            new newPlot("model5", e);
        }
    });
});
</script>

<template>
    <div class="box">
        <div class="s1">
            <span id="study2" style="cursor: pointer; font-size: 20px; line-height: 32px;">Study 2</span>
            <br />
            <span style="font-size: 26px; line-height: 1.5em; font-weight: 700;">
                Categorial and dimensional representations
            </span>
        </div>
        <div class="s2">
            <strong>The galaxy in the universe, relationships can also be clustered into different categories.</strong>
            Although we
            found a cognitive space in Study 1, categorical thinking is pervasive when people manage relationships in
            daily life, such as arranging messages and phone contacts with labels, assigning seating for wedding guests
            by groups, and buying different travel souvenirs for friends, relatives and work colleagues.
        </div>
        <div class="s3">
            <img src="/assets/fuckfeishu/Study2/study2_example.png" style="width: 100%;" alt="">
        </div>
        <div class="s4">
            Using three behavior tasks, we found the categorical model. The multi-arrangement task and dimensional
            survey (Model 1 and Model 3) both indicated <strong>three core clusters (i.e., hostile, private, and public,
                abbreviated as HPP)</strong> whereas the free sorting task (Model 2) identified <strong>six clusters
                (i.e., hostile, romantic, familial, affiliative, transactional, and power). </strong>
            <br />
            For dimensional models two categorization tasks consistently suggested a 2D space of ‘Valence-Formality’
            (Model 4 and Model 5) whereas the dimensional survey identified the 5D FAVEE space, which replicated the
            results in Study 1 (Model 6).
        </div>
        <div class="s5">
            <div style="width: 600px; height: 600px; position: relative;">
                <div style="width: 600px; height: 600px; background: url(./assets/fuckfeishu/Study2/study2_tasks1.png); background-size: contain; position: absolute; top: 0px; left: 0px;"></div>
                <div id="model1" style="width:450px;height:750px;overflow:hidden;position:absolute;top: 188px;left: 84px;transform-origin: left top;transform: scale(0.27, 0.28);"></div>
                <div id="model2" style="width:450px;height:750px;overflow:hidden;position:absolute;top: 188px;left: 288px;transform-origin: left top;transform: scale(0.27, 0.28);"></div>
                <div id="model3" style="width:450px;height:750px;overflow:hidden;position:absolute;top: 188px;left: 464px;transform-origin: left top;transform: scale(0.27, 0.28);"></div>
                <div id="model4" style="width: 262px;height: 227px;overflow:hidden;position:absolute;top:414px;left:53px;transform-origin: left top;transform:scale(0.55);"></div>
                <div id="model5" style="width: 262px;height: 227px;overflow: hidden;position: absolute;top: 414px;left: 246px;transform-origin: left top;transform: scale(0.55);"></div>

                <div id="i1" style="width: 389px;height: 176px;overflow: hidden;position: absolute;top: 169px;left: 93px;transform-origin: left top;transform: scale(0.18); background: url(./assets/fuckfeishu/Study2/study2_tasks/study2_tasks_02.png);"></div>
                <div id="i2" style="width: 389px;height: 176px;overflow: hidden;position: absolute;top: 169px;left: 275px;transform-origin: left top;transform: scale(0.18); background: url(./assets/fuckfeishu/Study2/study2_tasks/study2_tasks_04.png);"></div>
                <div id="i3" style="width: 389px;height: 176px;overflow: hidden;position: absolute;top: 169px;left: 465px;transform-origin: left top;transform: scale(0.18); background: url(./assets/fuckfeishu/Study2/study2_tasks/study2_tasks_06.png);"></div>
                <div id="i4" style="width: 389px;height: 971px;overflow: hidden;position: absolute;top: 204px;left: 37px;transform-origin: left top;transform: scale(0.18); background: url(./assets/fuckfeishu/Study2/study2_tasks/study2_tasks_07.png);"></div>
                <div id="i5" style="width: 389px;height: 971px;overflow: hidden;position: absolute;top: 204px;left: 234px;transform-origin: left top;transform: scale(0.18); background: url(./assets/fuckfeishu/Study2/study2_tasks/study2_tasks_09.png);"></div>
                <div id="i6" style="width: 306px;height: 971px;overflow: hidden;position: absolute;top: 204px;left: 428px;transform-origin: left top;transform: scale(0.18); background: url(./assets/fuckfeishu/Study2/study2_tasks/study2_tasks_11.png);"></div>
            </div>
            <div @click="emits('alertOpen', 'alertStudy2')" style="font-size: 22px; width: 25%; line-height: 1em; color: var(--theme-color-blue); cursor: pointer;">
                More details>
            </div>
            <div style="font-size: 12px; width: 75%; line-height: 1em;">
                When you hover over the interaction diagram, you'll see the specific relationships.
            </div>
        </div>
    </div>
</template>

<style scoped>
.box {
    grid-template-rows: 20px repeat(4, auto) 40px;
    text-align: left;
    grid-row-gap: 0;
    font-size: 14px;
    line-height: 1.8em;
}

.s1 {
    grid-area: 2 / 2 / 3 / 10;
}

.s2 {
    grid-area: 3 / 2 / 4 / 5;
}

.s3 {
    grid-area: 4 / 2 / 5 / 5;
}

.s4 {
    grid-area: 5 / 2 / 6 / 5;
}

.s5 {
    grid-area: 3 / 5 / 6 / 10;
}
.s5>div {
    display: inline-block;
    vertical-align: middle;
}
</style>