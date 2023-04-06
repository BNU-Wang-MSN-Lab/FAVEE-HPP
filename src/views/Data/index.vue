<template>
    <div class="box">
        <!-- title -->
        <div class="title">World-averaged model</div>
        <!-- 第一页面的选项 -->
        <div>
            <banner-choose title="Interactive maps" name="select your relationship of interest"
                choinput="bannerChooseWordInputData" @chos-event="wordChos">
                <div>
                    Combined with the data in 19 regions, we get the world-averaged FAVEE-HPP model. We also find a subset
                    of relationships that is representative of the whole conceptual space. Besides, we find that the mental
                    representations of some relationships vary across different regions while some relationships are
                    comparably consistent across regions. Our analysis shows that religion and modernization are two
                    important factors that contribute to cultural variation. You can explore the details of your interesting
                    relationship. <span @click="showAlertView"
                        style="display: inline-block; margin: 0 0 0 20px; color: var(--orange); cursor: pointer;">Read more</span>
                </div>
            </banner-choose>
            <div class="nav-button-show">
                <cho-button @click="showAlertView">Subset analysis</cho-button>
                <cho-button @click="showAlertView">Relationship variability</cho-button>
                <cho-button @click="showAlertView">Cultural mechanism</cho-button>
            </div>
            <div class="nav-container">
                <div>
                    <div>
                        <p><strong style="font-weight: 700;">{{ wordChosImgSrc == 'null' ? 'None' : wordChosImgSrc }}</strong> = </p>
                        <p style="text-indent: 1em;">Formality x ({{ wordValue.F }})</p>
                        <p style="text-indent: 1em;">+ Activeness x ({{ wordValue.A }})</p>
                        <p style="text-indent: 1em;">+ Valence x ({{ wordValue.V }})</p>
                        <p style="text-indent: 1em;">+ Exchange x ({{ wordValue.Ex }})</p>
                        <p style="text-indent: 1em;">+ Equality x ({{ wordValue.Eq }})</p>
                    </div>
                    <div>
                        <favee-radar-image :img="wordChosImgSrc"></favee-radar-image>
                    </div>
                </div>
                <div style="max-width: 600px;">
                    <div style="opacity: 0.6;">Hover the mouse over the circle, you can see what relationship it is and its
                        position in FAVEE
                        space.</div>
                    <load-plotly :img-src="imgSrc" v-on:loadPlot="fwaClick" :has-click="fwa_state">
                        <div id="fig-world-average"></div>
                    </load-plotly>
                    <div class="plot-legend">
                        <img src="@/assets/data/study/study3_1.png" alt="">
                        <img src="@/assets/data/study/study3_2.png" alt="">
                    </div>
                </div>
            </div>
        </div>
        <!-- 第二页面 -->
        <div style="margin: 0 0 150px 0;">
            <banner-choose title="Explore your region" name="select your reltionship of interest" choinput="countriesOpts"
                @chos-event="countryChos" :update-input-val="chooseCountry">
                <div>Select your region of interest for more details and data download.</div>
            </banner-choose>
            <geo-world @updateChosOpts="getCountriesOpts" @updateChosOpt="updateChosOpt"></geo-world>
            <div class="nav-button-show">
                <cho-button v-if="chooseCountry" @click="showAlertcView">Check selected region</cho-button>
                <cho-button v-else>Please select region first</cho-button>
            </div>
        </div>
        <!-- 弹窗 -->
        <alert-view v-if="alertViewVisible" @alertViewClose="alertViewVisible = false" :topPos="alertViewTopPos">
            <component :is="comp[alertPageSelected]"></component>
        </alert-view>
        <!-- 第二页的弹窗 -->
        <alertc-view v-if="alertViewcVisible" @alertViewClose="alertViewcVisible = false" :topPos="alertViewTopPos">
            <component :is="alertSelectedRegion" :country="chooseCountry"></component>
        </alertc-view>
    </div>
</template>

<script setup>
import { ref, reactive, provide, defineAsyncComponent } from 'vue';
import { newPlot } from "plotly.js-dist";
import { csvParse } from "d3-dsv";

import bannerChoose from '../../components/bannerChoose.vue';
import choButton from '../../components/choButton.vue';
import loadPlotly from "../../components/loadPlotly.vue";
import faveeRadarImage from '../../components/faveeRadarImage.vue';
import geoWorld from "./components/geoWorld.vue";

const alertView = defineAsyncComponent(() => import("../../components/alertView.vue"));
const alertcView = defineAsyncComponent(() => import("./components/country/alertView.vue"));
const alertMoreDetails = defineAsyncComponent(() => import("./components/alertMoreDetails.vue"));
const alertSubsetAnalysis = defineAsyncComponent(() => import("./components/alertSubsetAnalysis.vue"));
const alertRelationshipVariability = defineAsyncComponent(() => import("./components/alertRelationshipVariability.vue"));
const alertCulturalMechanism = defineAsyncComponent(() => import("./components/alertCulturalMechanism.vue"));
// 弹窗的总页面，以及当前页所选的内容
const comp = {
    "more-details": alertMoreDetails,
    "subset-analysis": alertSubsetAnalysis,
    "relationship-variability": alertRelationshipVariability,
    "cultural-mechanism": alertCulturalMechanism
};
const alertPageSelected = ref("");
// 弹窗的显示, 点啥弹啥
const alertViewVisible = ref(false);
const alertViewTopPos = ref(0);
const showAlertView = (e) => {
    alertViewVisible.value = true;
    alertViewTopPos.value = e.target.offsetTop + e.target.clientHeight * 1.3;
    alertPageSelected.value = e.target.innerText.toLowerCase().split(" ").join("-");
};

// 三维图的静态展示
const imgSrc = ref("");
import("@/assets/data/study/study3.png")
    .then(r => r.default)
    .then(r => imgSrc.value = r)
const fwa_state = ref(0); // 三维图的加载情况, 0为没加载, 1为数据已加载，2为图表已加载
const fwa_data = reactive({ data: null, style: null, args: null });
const fwaClick = () => {
    if (fwa_state.value != 0) return 0;
    if (document.body.clientWidth > 700) {
        import("@/assets/data/study/study3.json")
            .then(r => r.default)
            .then(r => changePlot(r))
    } else {
        import("@/assets/data/study/study3_300.json")
            .then(r => r.default)
            .then(r => changePlot(r))
    }
};

// 单词选项的数据加载
const wordData = reactive({ word: [], detail: [] });
import("@/assets/data/Study3/averaged_world_model/pca_favee.csv?raw")
    .then(r => r.default)
    .then(r => wordData.detail = csvParse(r));
import("@/assets/data/Study3/averaged_world_model/rels_159.csv?raw")
    .then(r => r.default)
    .then(r => wordData.word = csvParse(r));
provide("bannerChooseWordInputData", wordData);

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
    if (e) wordChosImgSrc.value = e;
    // 改变算数的数字
    const data = wordData.detail[i];
    if (data) {
        wordValue.F = formatWord(data["Formality"]);
        wordValue.A = formatWord(data["Activeness"]);
        wordValue.V = formatWord(data["Valence"]);
        wordValue.Ex = formatWord(data["Exchange"]);
        wordValue.Eq = formatWord(data["Equality"]);
    }
    // 改变图的点颜色
    if (e && document.body.clientWidth > 700) {
        import("@/assets/data/study/study3.json")
            .then(r => r.default)
            .then(r => changePlot(r, i))
    } else if (e) {
        import("@/assets/data/study/study3_300.json")
            .then(r => r.default)
            .then(r => changePlot(r, i))
    }
}
// 让计算的数字更好看一些
const formatWord = (w) => {
    return `${Math.ceil(w * 100) / 100}`
}
// 画图
const plot = (domid, data, style, args) => {
    document.querySelector(`#${domid}`).innerHTML = "";
    newPlot(domid, data, style, args)
        .then(r => fwa_state.value = 2);
}
// 记录上一次所选词的信息
const lastDotInfo = {
    i: null,
    op: null,
    color: null
}
// 重新画图
const changePlot = (r, i = null) => {
    fwa_state.value = 1;
    fwa_data.data = r.data;
    fwa_data.style = r.style;
    fwa_data.args = r.args;
    if (lastDotInfo.i != null) {
        fwa_data.data[lastDotInfo.i].marker.color = lastDotInfo.color;
        fwa_data.data[lastDotInfo.i].opacity = lastDotInfo.op;
        lastDotInfo.i = null;
        lastDotInfo.op = null;
        lastDotInfo.color = null;
    }
    if (i != null) {
        lastDotInfo.i = i;
        lastDotInfo.op = fwa_data.data[i].opacity;
        lastDotInfo.color = fwa_data.data[i].marker.color;
        fwa_data.data[i].marker.color = "#ff0000";
        fwa_data.data[i].opacity = 1;
    }
    // const dom = document.querySelector("#fig-world-average");
    const dom = document.createElement("div");
    dom.style.display = "flex";
    dom.style.justifyContent = "center";
    dom.style.alignItems = "center";
    dom.style.height = "300px";
    dom.innerText = "Loading";
    document.querySelector("#fig-world-average").appendChild(dom);
    let start = 0;
    const p = setInterval(() => {
        start++;
        dom.innerHTML = `Loading${"".padStart(start % 9, ".")}`;
    }, 500);
    setTimeout(() => {
        plot("fig-world-average", fwa_data.data, fwa_data.style, fwa_data.args)
            .then(() => {
                clearInterval(p);
                dom.parentElement.removeChild(dom);
            });
    }, 2000);
};

// 国家的坑开始啦
const alertViewcVisible = ref(false);
const showAlertcView = (e) => {
    if (chooseCountry.value == "") {
        e.target.innerText = "Please Select Region First";
        return 0;
    }
    e.target.innerText = "Check selected region";
    alertViewcVisible.value = true;
    alertViewTopPos.value = e.target.offsetTop + e.target.clientHeight * 1.3 - 100;
    alertPageSelected.value = e.target.innerText.toLowerCase().split(" ").join("-");
};
// 相应弹窗内容
const alertSelectedRegion = defineAsyncComponent(() => import("./components/country/alertSelectedRegion.vue"));
const countriesOpts = reactive({ word: [], detail: [] }); // 和上面的那个选项一样，不想改了
const chooseCountry = ref("");
provide("countriesOpts", countriesOpts);
provide("chooseCountry", chooseCountry);
const getCountriesOpts = (e) => {
    e.forEach(v => countriesOpts.word.push({ x: v }));
}
// 图到输入框
const updateChosOpt = (e) => {
    chooseCountry.value = e;
};
// 输入框直接点击
const countryChos = (e) => {
    chooseCountry.value = e;
}
</script>

<style scoped>
.box {
    width: 100%;
    max-width: 1200px;
    margin: 50px auto 0 auto;
}
.box>.title {
    background-image: linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(var(--orange), var(--orange)),
        linear-gradient(var(--lightblue), var(--lightblue)),
        linear-gradient(var(--lightblue), var(--lightblue));
    background-position: 0px 0px, 100% 8px, 100% 0px, calc(100% - 19px) 0px, 100% 0px;
    background-size: 25px 25px, 11px 11px, 19px 19px, 8px 8px, 11px 29px;
    background-repeat: no-repeat;
    box-sizing: content-box;
    padding: 20px 20px;
    font-size: 2rem;
    font-weight: 600;
    letter-spacing: 0;
    line-height: 3rem;
    color: var(--font-color-body);
}

.nav-button-show {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin: 20px 0;
}

.nav-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
}

.nav-container>div:nth-child(1) {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.nav-container>div:nth-child(1)>div:nth-child(1) {
    padding: 0 120px;
    box-sizing: border-box;
}

.plot-legend {
    display: flex;
    justify-content: space-around;
    margin: 50px;
}

.plot-legend>img {
    display: block;
    width: 110px;
}

.load-plotly::before {
    content: "";
    display: block;
    width: 80px;
    height: 100px;
    position: absolute;
    top: calc(50% - 16px);
    right: 0px;
    background-color: transparent;
    background-image: url(@/assets/data/study3/legend/study3_3_1.png);
    background-size: contain;
    background-repeat: no-repeat;
    z-index: 1;
}

@media screen and (max-width: 1100px) {
    .nav-container>div:nth-child(1) {
        flex-direction: row;
        align-items: center;
    }

    .nav-container>div:nth-child(1)>div:nth-child(1) {
        padding: 0;
    }
}

@media screen and (max-width: 900px) {
    .nav-button-show {
        flex-direction: column;
    }

    .nav-container {
        margin: 0 20px;
    }

    .nav-container>div:nth-child(2)>div:nth-child(1) {
        margin: 0 0 20px 0;
    }

    .cho-button {
        width: 80vw;
        margin: 5px;
    }
    .load-plotly::before {
        width: 40px;
        height: 50px;
    }
}
</style>