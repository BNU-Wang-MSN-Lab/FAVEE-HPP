<script setup>
import $ from "jquery";
import { inject, onMounted, ref } from 'vue';
import Plotly from "plotly.js-dist";
import { csvParse } from "d3-dsv";
const counList = {
    "China": "CHN",
    "United States": "USA",
    "": "UK",
    "": "Australia",
    "": "South_africa",
    "": "Germany",
    "": "Japan",
    "": "Israel",
    "": "HK(region)",
    "": "France",
    "": "Spain",
    "": "Mexico",
    "": "Chile",
    "": "Portugal",
    "": "Brazil",
    "": "Russia",
    "": "Egypt",
    "": "Qatar",
    "": "India"
};

const show = ref(2);
const chooseCountry = inject("chooseCountry");

const data = {
    1: {
        texts: [
            "The specific results of dimensional model in [region], including the loading PCA loading (figure a),",
            "relationship score within FAVEE space (figure b), and model comparison analysis (figure c)."
        ]
    },
    2: {
        texts: [
            "The specific results of categorical model in [region].",
            "By clicking one point, you can see its corresponding relationship in FAVEE and 33D space, which is shown in the radar plot."
        ]
    },
    3: {
        texts: [
            "We collected age, gender, education, ethnicity in each region."
        ]
    }
};

const words = $.ajax({
    url: `./data/study/159world.json`,
    type: "GET",
    dataType: "json",
    async: false
}).responseJSON;
const wordsData = csvParse($.ajax({
    url: `./assets/Study3/${counList[chooseCountry.value]}/categorical/${counList[chooseCountry.value]}_favee.csv`,
    type: "GET",
    async: false
}).responseText);
const showWords = ref([]);
showWords.value = words;
const showWord = ref("");
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
    document.querySelector(".img2 .img2Box").style.backgroundImage = `url(./assets/Study3/${counList[chooseCountry.value]}/categorical/radar/${e.replaceAll(" ", "\\ ")}.png)`

    const wo = wordsData[words.indexOf(e)];
    showWord.value = `${wo[""]} = \n Activeness * (${Math.round(wo["Activeness"] * 100) / 100
        })\n + Equality * (${Math.round(wo["Equality"] * 100) / 100
        })\n + Exchange * (${Math.round(wo["Exchange"] * 100) / 100
        })\n + Formality * (${Math.round(wo["Formality"] * 100) / 100
        })\n + Valence * (${Math.round(wo["Valence"] * 100) / 100
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
        url: `./assets/Study3/${counList[chooseCountry.value]}/dimensional/${counList[chooseCountry.value]}_favee1.json`,
        type: "GET",
        dataType: "json",
        success: (e) => {
            Plotly.newPlot("study3AlertImage1-1", e);
        }
    });
    $.ajax({
        url: `./assets/Study3/${counList[chooseCountry.value]}/dimensional/${counList[chooseCountry.value]}_favee2.json`,
        type: "GET",
        dataType: "json",
        success: (e) => {
            Plotly.newPlot("study3AlertImage1-2", e);
        }
    });
    $.ajax({
        url: `./assets/Study3/${counList[chooseCountry.value]}/categorical/${counList[chooseCountry.value]}_hpp.json`,
        type: "GET",
        dataType: "json",
        success: (e) => {
            Plotly.newPlot("img2AlertImage1", e);
        }
    });
});
</script>
<template>
    <div class="box">
        <div class="select">
            <div :class="{ selected: show == 1 }" @click="show = 1">Dimentional</div>
            <div :class="{ selected: show == 2 }" @click="show = 2">Categorical</div>
            <div :class="{ selected: show == 3 }" @click="show = 3">Demographics</div>
        </div>
        <div class="title">{{ chooseCountry }}</div>
        <div class="button">
            <div @click="hrefClick('https://osf.io/nfkmj')">Download Data</div>
            <div @click="hrefClick('https://osf.io/nfkmj')">Download Survey</div>
        </div>
        <div class="content">
            <p v-for="i in data[show].texts">{{ i }}</p>
            <div class="img1" v-show="show == 1">
                <!-- <img alt=""
                    :src="'./assets/Study3/' + counList[chooseCountry] + '/dimensional/' + `${counList[chooseCountry]}_loadings.png`"> -->
                <div class="img"
                    :style="'background-image: url(./assets/Study3/' + counList[chooseCountry] + '/dimensional/' + `${counList[chooseCountry]}_loadings.png);`">
                </div>
                <div class="img2">
                    <img src="/assets/legend/dimensional_b.png" alt="" style="height: 60px;">
                    <div id="study3AlertImage1-1"></div>
                    <div id="study3AlertImage1-2"></div>
                </div>
                <div class="img3box">
                    <div class="tit">
                        <div style="width: 319px;">Adjusted R-Square</div>
                        <div style="width: 200px;">
                            <img src="/assets/legend/dimensional_c1.png" alt="">
                        </div>
                        <div style="width: 300px;">Bayesian Information Criterion(BIC)</div>
                    </div>
                    <div class="img3"
                        :style='`background-image: url(./assets/Study3/${counList[chooseCountry]}/dimensional/${counList[chooseCountry]}_AdjR.png), url(./assets/Study3/${counList[chooseCountry]}/dimensional/${counList[chooseCountry]}_BIC.png);`'>
                    </div>
                    <div class="img3Legend"></div>
                </div>
            </div>
            <div class="img2" v-show="show == 2">
                <div id="img2AlertImage1"></div>
                <div>
                    <div class="tBox">
                        <div>which relationship are you interested in?</div>
                        <div style="position: relative;">
                            <input type="text" id="page4Country" @input="input">
                            <ul>
                                <li v-for="i in showWords" @click="chosWord(i)">{{ i }}</li>
                            </ul>
                        </div>
                        <div>
                            {{ showWord }}
                        </div>
                    </div>
                    <div class="img2Box"></div>
                </div>
            </div>
            <div class="img3" v-show="show == 3">
                <div>
                    <div>Age</div>
                    <div>Gender</div>
                    <div>Ethnicity</div>
                </div>
                <img alt=""
                    :src="'./assets/Study3/' + counList[chooseCountry] + '/demographics/' + `${counList[chooseCountry]}_age.png`">
                <img alt=""
                    :src="'./assets/Study3/' + counList[chooseCountry] + '/demographics/' + `${counList[chooseCountry]}_gender.png`">
                <img alt=""
                    :src="'./assets/Study3/' + counList[chooseCountry] + '/demographics/' + `${counList[chooseCountry]}_ethnicity.png`">
            </div>
        </div>
    </div>
</template>

<style scoped>
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

.box {
    width: 100%;
    height: 90%;
    margin: 10% 0 0 0;
    border: none;
    box-shadow: none;
    overflow: hidden scroll;
}

.select {
    width: 360px;
    margin: auto;
    border: 1px solid var(--theme-color-blue);
    border-radius: 9px;
    cursor: pointer;
}

.select>div {
    width: 120px;
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
    margin: 40px 0;
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
    background-size: 533px 1000px;
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
    background-position: -125px 0px, 310px 0px;
    background-size: 450px 300px, 450px 300px;
    margin: 0 auto;
}

.content>.img1 .img3Legend {
    width: 760px;
    height: 30px;
    background-image: url(/assets/legend/dimensional_c2.png), url(/assets/legend/dimensional_c3.png);
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

.content>.img3>div {
    width: 100%;
    margin: 20px 0 0 0;
}

.content>.img3>div>div {
    display: inline-block;
    width: 30%;
    font-size: 26px;
    line-height: 30px;
    font-weight: 700;
}

.content>.img3>img {
    width: 30%;
    vertical-align: top;
}
</style>