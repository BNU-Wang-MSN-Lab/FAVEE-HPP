<script setup>
import { csvParse } from "d3-dsv";
import $ from "jquery";
import { newPlot } from "plotly.js-dist";
import { onMounted, ref } from "vue";
const emits = defineEmits(["alertOpen"]);

const words = $.ajax({
    url: "./data/study/159world.json",
    type: "GET",
    dataType: "json",
    async: false
}).responseJSON;

const wordsData = csvParse($.ajax({
    url: "./data/study/pca_favee.csv",
    type: "GET",
    async: false
}).responseText);

const showWords = ref([]);
showWords.value = words;

const showWord = ref("");

const input = function(e) {
    if (e.length == 0) {
        showWords.value = words;
        return 0;
    }
    showWords.value = words.filter(v => v.toLowerCase().search(e.target.value) >= 0)
    if (showWords.value.length == 1) {
        chosWord(showWords.value[0]);
    }
}
const chosWord = function(e) {
    document.querySelector("#study3Country").value = e;
    document.querySelector(".choose>.view>.img").style.backgroundImage = `url(./assets/study3Word/${e.replaceAll(" ", "\\ ")}.png)`

    const wo = wordsData[words.indexOf(e)];
    showWord.value = `${wo[""]} = \n Activeness * (${
            Math.round(wo["Activeness"] * 100) / 100
        })\n + Equality * (${
            Math.round(wo["Equality"] * 100) / 100
        })\n + Exchange * (${
            Math.round(wo["Exchange"] * 100) / 100
        })\n + Formality * (${
            Math.round(wo["Formality"] * 100) / 100
        })\n + Valence * (${
            Math.round(wo["Valence"] * 100) / 100
        })`
}
onMounted(() => {
    $.ajax({
        url: "./data/study/study3.json",
        type: "GET",
        dataType: "json",
        success: (e) => {
            new newPlot("study3Can", e.data, e.style, e.args)
        }
    });
});
</script>

<template>
    <div class="box">
        <div class="tit">
            <span class="one" id="study3">Study 3</span>
            <br />
            <span class="two">
                <span style="color: var(--theme-color-blue)">U</span>niversality and cultural variability
            </span>
        </div>
        <div class="content">
            <p style="font-size: 24px; line-height: 30px; margin: 0;">World-averaged model</p>
            <p style="font-size: 12px; line-height: 18px; margin: 0;">Check the <span
                    @click="emits('alertOpen', 'alert3D')"
                    style="color: var(--theme-color-blue); cursor: pointer;">model
                    details ></span></p>
            <p style="font-size: 16px; line-height: 24px;">Combined with the data in 19 regions, we get the
                world-averaged model.</p>
            <p style="font-size: 16px; line-height: 24px;">You can explore your interested relationship!</p>
        </div>
        <div class="button">
            <div @click="emits('alertOpen', 'alertSubset')">Subset analysis</div>
            <div @click="emits('alertOpen', 'alertRelationship')">Relationship variability</div>
            <div @click="emits('alertOpen', 'alertCultural')">Cultural mechanism</div>
        </div>
        <div class="iBox">
            <div class="canvas">
                <div id="study3Can"></div>
                <div>
                    <img src="/assets/legend/study3_1.png" alt="" />
                    <img src="/assets/legend/study3_2.png" alt="" />
                </div>
            </div>
            <div class="choose">
                <div class="formula">{{ showWord }}</div>
                <div class="title">which relationship are you interested in?</div>
                <div class="sel">
                    <input type="text" name="country" id="study3Country" placeholder="Type to search" @input="input" />
                    <ul>
                        <li v-for="i in showWords" @click="chosWord(i)">{{ i }}</li>
                    </ul>
                </div>
                <div class="view">
                    <!-- <div class="chos">
                        <div class="selected">FAVEE</div>
                        <div>33D</div>
                    </div> -->
                    <div class="img"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.sel>input {
    width: 284px;
    height: 36px;
    background: #fff;
    padding: 6px 14px;
    box-sizing: border-box;
    border: 1px solid #4d4a47;
    border-radius: 14px;
    font-size: 16px;
    line-height: 30em;
    color: black;
}

.sel {
    margin: 10px 0;
    position: relative;
}

.sel::after {
    content: '';
    display: block;
    width: 0px;
    height: 0px;
    border: 9px solid;
    border-color: black transparent transparent transparent;
    position: absolute;
    top: 14px;
    right: 68px;
    cursor: pointer;
}
.sel>ul {
    display: none;
    width: 269px;
    max-height: 150px;
    padding: 5px;
    border: 2px solid #ababab;
    border-radius: 14px;
    background: #fff;
    position: absolute;
    top: 20px;
    left: calc(50% - 140px);
    overflow-y: scroll;
    user-select: none;
}
.sel>ul li {
    color: grey;
    list-style: none;
    text-align: left;
}
.sel>ul li:hover {
    color: black
}
.sel:hover>ul {
    display: block;
}
.box {
    width: 100%;
    position: relative;
    background: #f5f6f7;
    overflow: hidden;
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
    width: 70%;
    margin: 40px 0 0 60px;
}

.button {
    text-align: left;
    margin: 0 0 0 50px;
}

.button>div {
    display: inline-block;
    padding: 5px 10px;
    margin: 10px 20px;
    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 9px;
    cursor: pointer;
}

.iBox {
    width: 100%;
    margin: 10px 0;
}

.iBox>div {
    vertical-align: middle;
}

.iBox .canvas {
    display: inline-block;
    width: 600px;
    height: 500px;
    background: transparent;
    overflow: scroll;
    position: relative;
}

.iBox .canvas img {
    width: 120px;
}

.iBox .canvas>div:nth-child(2) {
    width: 120px;
    position: absolute;
    top: 30px;
    right: 0;
}

.iBox .choose {
    display: inline-block;
    width: 400px;
    height: 500px;
    margin: 0 0 0 100px;
    position: relative;
}
.choose .formula {
    display: block;
    width: 200px;
    position: absolute;
    top: -205px;
    left: 70px;
    white-space: pre-line;
    text-align: left;
    text-align-last: end;
}
.choose .view {
    margin: 50px 0 0 0;
}

.choose .view .chos {
    width: 240px;
    margin: auto;
    border: 1px solid grey;
    border-radius: 9px;
    cursor: pointer;
}

.choose .view .chos>div {
    width: 120px;
    display: inline-block;
    line-height: 2em;
}

.choose .view .chos>.selected {
    background: grey;
    border-radius: 8px;
    color: white;
}

.choose .view .img {
    width: 300px;
    height: 300px;
    margin: auto;
    background: #fff no-repeat;
    background-size: contain;
}
</style>