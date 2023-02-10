<script setup>
import $ from "jquery";
import { inject, onMounted, ref } from 'vue';
import Plotly from "plotly.js-dist";
import { csvParse } from "d3-dsv";
const counList = {
    "China": "CHN",
    "United States": "USA",
    "United Kingdom": "UK",
    "Australia": "Australia",
    "South Africa": "South_africa",
    "Germany": "Germany",
    "Japan": "Japan",
    "Israel": "Israel",
    "Hong Kong SAR": "HK",
    "France": "France",
    "Spain": "Spain",
    "Mexico": "Mexico",
    "Chile": "Chile",
    "Portugal": "Portugal",
    "Brazil": "Brazil",
    "Russian Federation": "Russia",
    "Egypt": "Egypt",
    "Qatar": "Qatar",
    "India": "India"
};

const show = ref(2);
const chooseCountry = inject("chooseCountry");
const onstalled = [
    "India",
    "Russian Federation",
    "Qatar",
    "Egypt"
]
const data = {
    1: {
        texts: onstalled.indexOf(chooseCountry.value) >= 0 ? [
            "The specific results of dimensional model in [region], including the loading PCA loading (figure a),".replaceAll("[region]", chooseCountry.value),
            "relationship score within FAVEE space (figure b), and model comparison analysis (figure c).",
            '"Equality" was relatively ambiguous, more details can be seen in the published paper.'
        ] : [
            "The specific results of dimensional model in [region], including the loading PCA loading (figure a),".replaceAll("[region]", chooseCountry.value),
            "relationship score within FAVEE space (figure b), and model comparison analysis (figure c)."
        ]
    },
    2: {
        texts: onstalled.indexOf(chooseCountry.value) >= 0 ? [
            "The specific results of categorical model in [region].".replaceAll("[region]", chooseCountry.value),
            "Select your relationship of interest, and you can see its corresponding relationship in FAVEE space, which is shown in the radar plot.",
            '"Equality" was relatively ambiguous, more details can be seen in the published paper.'
        ] : [
            "The specific results of categorical model in [region].".replaceAll("[region]", chooseCountry.value),
            "Select your relationship of interest, and you can see its corresponding relationship in FAVEE space, which is shown in the radar plot."
        ]
    },
    3: {
        texts: [
            "We collected age, gender, education, ethnicity in each region."
        ]
    }
};

const words = csvParse($.ajax({
    url: "./assets/fuckfeishu/Study3/averaged_world_model/rels_159.csv",
    type: "GET",
    async: false
}).responseText).map(v => v.x);

const wordsData = csvParse($.ajax({
    url: `./assets/fuckfeishu/Study3/${counList[chooseCountry.value]}/categorical/${counList[chooseCountry.value]}_favee.csv`,
    type: "GET",
    async: false
}).responseText);
const showWords = ref([]);
showWords.value = words;
const showWord = ref("");
const choosedWord = ref("");
const input = function (e) {
    if (e.length == 0) {
        showWords.value = words;
        return 0;
    }
    showWords.value = words.filter(v => v.toLowerCase().search(e.target.value) >= 0)
    if (showWords.value.length == 1) {
        chosWord(showWords.value[0]);
    }
}
const chosWord = function (e) {
    document.querySelector("#page4Country").value = e;
    document.querySelector(".img2 .img2Box").style.backgroundImage = `url(./assets/fuckfeishu/Study3/${counList[chooseCountry.value]}/categorical/radar/${e.replaceAll(" ", "\\ ")}.png)`

    const wo = wordsData[words.indexOf(e)];
    choosedWord.value = wo[""];
    showWord.value = `= \n Formality × (${Math.round(wo["Formality"] * 100) / 100
        }) + \n Activeness × (${Math.round(wo["Activeness"] * 100) / 100
        }) + \n Valence × (${Math.round(wo["Valence"] * 100) / 100
        }) + \n Exchange × (${Math.round(wo["Exchange"] * 100) / 100
        }) + \n Equality × (${Math.round(wo["Equality"] * 100) / 100
        })`
}

const hrefClick = (e) => {
    let a = document.createElement("a");
    a.href = e;
    a.target = "_blank"
    a.click();
}
onMounted(() => {
    $.ajax({
        url: `./assets/fuckfeishu/Study3/${counList[chooseCountry.value]}/dimensional/${counList[chooseCountry.value]}_favee1.json`,
        type: "GET",
        dataType: "json",
        success: (e) => {
            Plotly.newPlot("study3AlertImage1-1", e);
        }
    });
    $.ajax({
        url: `./assets/fuckfeishu/Study3/${counList[chooseCountry.value]}/dimensional/${counList[chooseCountry.value]}_favee2.json`,
        type: "GET",
        dataType: "json",
        success: (e) => {
            Plotly.newPlot("study3AlertImage1-2", e);
        }
    });
    $.ajax({
        url: `./assets/fuckfeishu/Study3/${counList[chooseCountry.value]}/categorical/${counList[chooseCountry.value]}_hpp.json`,
        type: "GET",
        dataType: "json",
        success: (e) => {
            Plotly.newPlot("img2AlertImage1", e);
        }
    });
});
</script>
<template>
    <div class="abox">
        <div class="select">
            <div :class="{ selected: show == 1 }" @click="show = 1">Dimentional Model</div>
            <div :class="{ selected: show == 2 }" @click="show = 2">Categorical Model</div>
            <div :class="{ selected: show == 3 }" @click="show = 3">Demographics Model</div>
        </div>
        <div class="title">{{ chooseCountry }}</div>
        <div class="button">
            <div @click="hrefClick('https://osf.io/nfkmj')">Download Data and Survey</div>
        </div>
        <div class="content">
            <p v-for="i in data[show].texts">{{ i }}</p>
            <div class="img1" v-show="show == 1">
                <!-- <img alt=""
                    :src="'./assets/Study3/' + counList[chooseCountry] + '/dimensional/' + `${counList[chooseCountry]}_loadings.png`"> -->
                <div class="img"
                    :style="'position: relative; background-image: url(./assets/fuckfeishu/Study3/' + counList[chooseCountry] + '/dimensional/' + `${counList[chooseCountry]}_loadings.png);`">
                    <div style="position: absolute; top: 0; left: 0; font-size: 46px; font-weight: 700;">a</div>
                </div>
                <div class="img2" style="position: relative;">
                    <img src="/assets/fuckfeishu/Study3/图例/dimensional_b.png" alt="" style="height: 60px;">
                    <div id="study3AlertImage1-1"></div>
                    <div id="study3AlertImage1-2"></div>
                    <div style="width: 410px; text-align: left; font-size: 10px; line-height: 1em; margin: 0 0 0 50px;">
                        Hover the mouse over the circle, you can see what relationship it is and its position in FAVEE
                        space.
                        Zoom in on an area with the mouse by framing it, and click on the enlarged area to restore it to
                        its original size.
                    </div>
                    <div style="position: absolute; top: 0; left: 0; font-size: 46px; font-weight: 700;">b</div>
                </div>
                <div class="img3box" style="position: relative;">
                    <div class="tit">
                        <div style="width: 319px;">Adjusted R-Square</div>
                        <div style="width: 200px;">
                            <img src="/assets/fuckfeishu/Study3/图例/dimensional_c1.png" alt="">
                        </div>
                        <div style="width: 300px;">Bayesian Information Criterion(BIC)</div>
                    </div>
                    <div class="img3"
                        :style='`background-image: url(./assets/fuckfeishu/Study3/${counList[chooseCountry]}/dimensional/${counList[chooseCountry]}_AdjR.png), url(./assets/fuckfeishu/Study3/${counList[chooseCountry]}/dimensional/${counList[chooseCountry]}_BIC.png);`'>
                    </div>
                    <div class="img3Legend"></div>
                    <div
                        style="position: absolute; top: 0px; left: calc(50% - 450px); font-size: 46px; font-weight: 700;">
                        c</div>
                </div>
            </div>
            <div class="img2" v-show="show == 2">
                <div id="img2AlertImage1">
                    <div style="font-size: 10px; line-height: 1em; text-align: left;">
                        Hover the mouse over the circle,you can see what relationship it is.
                    </div>
                    <div style="font-size: 10px; line-height: 1em; text-align: left;">
                        Zoom in on an area with the mouse by framing it,and double-click on the enlarged area to restore
                        it to its original size.
                    </div>
                </div>
                <div>
                    <div class="tBox">
                        <div>Select your relationship of interest</div>
                        <div style="position: relative;">
                            <input type="text" id="page4Country" @input="input">
                            <ul>
                                <li v-for="i in showWords" @click="chosWord(i)">{{ i }}</li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <div class="img2Box" style="display: inline-block; vertical-align: middle; position: relative;">
                            <div v-if="choosedWord != ''">Formality</div>
                            <div v-if="choosedWord != ''">Activeness</div>
                            <div v-if="choosedWord != ''">Valence</div>
                            <div v-if="choosedWord != ''">Exchange</div>
                            <div v-if="choosedWord != ''">Equality</div>
                        </div>
                        <div style="display: inline-block; white-space: pre; vertical-align: middle;">
                            <div>
                                <strong>{{ choosedWord }}</strong>{{ showWord }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="img3" v-show="show == 3">
                <div style="grid-area: 1 / 2 / 2 / 4;">
                    <div>Age</div>
                    <img style="width: 45%;" alt=""
                        :src="'./assets/fuckfeishu/Study3/' + counList[chooseCountry] + '/demographics/' + `${counList[chooseCountry]}_age.png`">
                    <img style="width: 25%;" alt=""
                        src="/assets/fuckfeishu/Study3/图例/study3_details_demographics_age.png">
                </div>
                <div style="grid-area: 1 / 4 / 2 / 6;">
                    <div>Gender</div>
                    <img style="width: 45%;" alt=""
                        :src="'./assets/fuckfeishu/Study3/' + counList[chooseCountry] + '/demographics/' + `${counList[chooseCountry]}_gender.png`">
                    <img style="width: 25%;transform: scale(1.2);" alt=""
                        src="/assets/fuckfeishu/Study3/图例/study3_details_demographics_gender.png">
                </div>
                <div style="grid-area: 1 / 6 / 2 / 8;">
                    <div>Education</div>
                    <img style="width: 45%;" alt=""
                        :src="'./assets/fuckfeishu/Study3/' + counList[chooseCountry] + '/demographics/' + `${counList[chooseCountry]}_education.png`">
                    <img style="width: 25%;transform: scale(1.4);" alt=""
                        src="/assets/fuckfeishu/Study3/图例/study3_details_demographics_education.png">
                </div>
                <div style="grid-area: 1 / 8 / 2 / 10;">
                    <div>Ethnicity</div>
                    <img style="width: 100%;" alt=""
                        :src="'./assets/fuckfeishu/Study3/' + counList[chooseCountry] + '/demographics/' + `${counList[chooseCountry]}_ethnicity.png`">
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.img2 .img2Box>div {
    display: block;
    position: absolute;
}

.img2 .img2Box>div:nth-child(1) {
    top: 31px;
    left: 125px;
}

.img2 .img2Box>div:nth-child(2) {
    top: 85px;
    left: 40px;
}

.img2 .img2Box>div:nth-child(3) {
    top: 210px;
    left: 65px;
}

.img2 .img2Box>div:nth-child(4) {
    top: 210px;
    left: 185px;
}

.img2 .img2Box>div:nth-child(5) {
    top: 85px;
    left: 220px;
}

.tBox {
    margin: 20px 0 0 0;
}

.tBox>div:nth-child(1) {
    font-size: 20px;
    font-weight: 700;
    line-height: 30px;
}

.tBox>div:nth-child(2)>input {
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

.tBox>div:nth-child(2)::after {
    content: '';
    display: block;
    width: 0px;
    height: 0px;
    border: 9px solid;
    border-color: black transparent transparent transparent;
    position: absolute;
    top: 14px;
    right: 124px;
    cursor: pointer;
}

.tBox>div:nth-child(2)>ul {
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
    z-index: 2;
}

.tBox>div:nth-child(2)>ul li {
    color: grey;
    list-style: none;
    text-align: left;
}

.tBox>div:nth-child(2)>ul li:hover {
    color: black
}

.tBox>div:nth-child(2):hover>ul {
    display: block;
}

.content>.img2 .img2Box {
    width: 300px;
    height: 300px;
    margin: 10px auto 0;
    background-repeat: no-repeat;
    background-size: contain;
}

.content>.img2 {
    width: 1000px;
    height: 500px;
    margin: 0 auto;
}

.content>.img2>div {
    display: inline-block;
    width: 500px;
    height: 500px;
    vertical-align: middle;
}

.abox {
    width: 100%;
    height: 100%;
    margin: 5% 0 0 0;
}

.select {
    width: 495px;
    margin: auto;
    border: 1px solid var(--theme-color-blue);
    border-radius: 9px;
    cursor: pointer;
}

.select>div {
    width: 165px;
    display: inline-block;
    line-height: 2em;
}

.select>.selected {
    background: var(--theme-color-blue);
    border-radius: 8px;
    color: white;
}

.title {
    font-size: 32px;
    font-weight: 500;
    margin: 25px 0;
}

.button>div {
    display: inline-block;
    padding: 5px 10px;
    margin: 10px 30px;
    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 9px;
    cursor: pointer;
}

.content {
    font-size: 16px;
    line-height: 24px;
}

.content>p {
    margin: 0;
}

.content>.img1>.img {
    display: inline-block;
    width: 450px;
    height: 1000px;
    background-repeat: no-repeat;
    background-position: right;
    vertical-align: top;
}

.content>.img1>.img2 {
    display: inline-block;
    margin: 20px 0 0 0;
}

.content>.img1>.img3box {
    margin: 20px auto;
}

.img3box .tit {
    width: 850px;
    margin: 0 auto;
}

.img3box .tit>div {
    display: inline-block;
    font-size: 16px;
    line-height: 24px;
    font-weight: 700;
    vertical-align: bottom;
}

.img3box .tit img {
    width: 128px;
}

.content>.img1 .img3 {
    display: block;
    width: 760px;
    height: 284px;
    background: #fff no-repeat;
    background-position: -131px 0px, 299px 0px;
    background-size: 450px 300px, 450px 300px;
    margin: 0 auto;
}

.content>.img1 .img3Legend {
    width: 760px;
    height: 30px;
    background-image: url(/assets/fuckfeishu/Study3/图例/dimensional_c2.png), url(/assets/fuckfeishu/Study3/图例/dimensional_c3.png);
    background-position: left, right;
    background-size: 152px 30px;
    background-repeat: no-repeat;
    margin: 0 auto;
}

#study3AlertImage1-1,
#study3AlertImage1-2 {
    width: 450px;
    height: 450px;
    background: grey;
    vertical-align: top;
}

.content>.img3 {
    display: grid;
    grid-template-columns: 20px repeat(8, 1fr) 20px;
    margin: 40px 0 0 0;
}

.content>.img3 img {
    display: inline-block;
    vertical-align: middle;
}

.content>.img3>div>div {
    font-size: 26px;
    line-height: 30px;
    font-weight: 700;
}
</style>