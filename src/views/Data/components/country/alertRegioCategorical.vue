<template>
    <div>
        <banner-choose name="select your relationship of interest" choinput="coBannerChooseWordInputData"
            @chos-event="wordChos">
            <div style="max-width: 358px;">
                The specific results of categorical model in United States. Select your relationship of interest, and you
                can see its corresponding relationship in FAVEE space, which is shown in the radar plot.
            </div>
        </banner-choose>
        <div class="img-box">
            <div class="plot-a">
                <faveeRadarImage :img="wordChosImgSrc"></faveeRadarImage>
            </div>
            <div class="func">
                <p><strong style="font-weight: 700;">{{ wordChosImgSrc == 'null' ? 'None' : wordChosImgSrc.replace("r-", "") }}</strong> = </p>
                <p style="text-indent: 1em;">Formality x ({{ wordValue.F }})</p>
                <p style="text-indent: 1em;">+ Activeness x ({{ wordValue.A }})</p>
                <p style="text-indent: 1em;">+ Valence x ({{ wordValue.V }})</p>
                <p style="text-indent: 1em;">+ Exchange x ({{ wordValue.Ex }})</p>
                <p style="text-indent: 1em;">+ Equality x ({{ wordValue.Eq }})</p>
            </div>
            <div id="plot-b"></div>
            <div class="explain">
                Hover the mouse over the circle,you can see what relationship it is. Zoom in on an area with the mouse by
                framing it,and double-click on the enlarged area to restore it to its original size.
            </div>
        </div>
    </div>
</template>

<script setup>
import { provide, reactive, ref, inject } from 'vue';
import { csvParse } from 'd3-dsv';
import { newPlot } from 'plotly.js-dist';

import bannerChoose from '../../../../components/bannerChoose.vue';
import faveeRadarImage from '../../../../components/faveeRadarImage.vue';

const country = inject("chooseCountry");
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
const useCountry = ref("");
useCountry.value = counList[country.value];

// 单词选项的数据加载
const wordData = reactive({ word: [], detail: [] });
import(`../../../../assets/data/Study3/${useCountry.value}/categorical/${useCountry.value}_favee.csv?raw`)
    .then(r => r.default)
    .then(r => wordData.detail = csvParse(r));
import('../../../../assets/data/Study3/averaged_world_model/rels_159.csv?raw')
    .then(r => r.default)
    .then(r => wordData.word = csvParse(r));
provide("coBannerChooseWordInputData", wordData);

// plotly的加载
import(`../../../../assets/data/Study3/${useCountry.value}/categorical/${useCountry.value}_hpp.json`)
    .then(r => r.default)
    .then(r => newPlot("plot-b", r));

// 单词选中事件
const wordChosImgSrc = ref("null");
const wordValue = reactive({
    F: "None",
    A: "None",
    V: "None",
    Ex: "None",
    Eq: "None"
});
const wordChos = (e, i) => {
    if (e) wordChosImgSrc.value = `r-${e}`;
    // 改变算数的数字
    const data = wordData.detail[i];
    if (data) {
        wordValue.F = formatWord(data["Formality"]);
        wordValue.A = formatWord(data["Activeness"]);
        wordValue.V = formatWord(data["Valence"]);
        wordValue.Ex = formatWord(data["Exchange"]);
        wordValue.Eq = formatWord(data["Equality"]);
    }
}
// 让计算的数字更好看一些
const formatWord = (w) => {
    return `${Math.ceil(w * 100) / 100}`
}
</script>
 
<style scoped>
.img-box {
    display: flex;
    max-width: 865px;
    margin: 0 auto;
    flex-wrap: wrap;
    justify-content: space-around;
    align-items: center;
}
.plot-a {
    width: 450px;
    position: relative;
}
.plot-a::after {
    content: "";
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    position: absolute;
    background-image: linear-gradient(var(--orange), var(--orange)), linear-gradient(var(--lightorange), var(--lightorange)), linear-gradient(var(--blue1), var(--blue1));
    background-size: 20% 10px, 80% 10px, 100% 10px;
    background-position: 0px 100%;
    background-repeat: no-repeat;
}
.func {
    width: 300px;
    height: 220px;
    transform: scale(1.5);
    transform-origin: top left;
    overflow: hidden;
}
.explain {
    display: block;
    background-color: var(--morelightorange);
    padding: 58px 36px;
    width: 438px;
}
@media screen and (max-width: 800px) {
    .plot-a::after {
        content: "";
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        position: absolute;
        background-image: none;
    }
}
@media screen and (max-width: 600px) {
    .func {
        width: 210px;
        height: 172px;
        transform: scale(1.5);
        transform-origin: top left;
        overflow: hidden;
    }
    #plot-b {
        width: 280px;
        height: 245px;
        transform: scale(0.7);
        transform-origin: top left;
        overflow: hidden;
    }
    .explain {
        padding: 29px 18px;
        width: 300px;
    }
}
</style>
