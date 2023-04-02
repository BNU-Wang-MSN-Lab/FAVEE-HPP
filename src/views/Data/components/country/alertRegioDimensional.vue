<script setup>
import { inject, reactive, ref } from 'vue';
import { newPlot } from 'plotly.js-dist';

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
const imgSrc = reactive({ a: "", b: "", c: "" });
import(`../../../../assets/data/Study3/${useCountry.value}/dimensional/${useCountry.value}_loadings.png`)
    .then(r => r.default)
    .then(r => imgSrc.a = r);
import(`../../../../assets/data/Study3/${useCountry.value}/dimensional/${useCountry.value}_favee1.json`)
    .then(r => r.default)
    .then(r => newPlot("aR-plot1", r));
import(`../../../../assets/data/Study3/${useCountry.value}/dimensional/${useCountry.value}_favee2.json`)
    .then(r => r.default)
    .then(r => newPlot("aR-plot2", r));
import(`../../../../assets/data/Study3/${useCountry.value}/dimensional/${useCountry.value}_AdjR.png`)
    .then(r => r.default)
    .then(r => imgSrc.b = r);
import(`../../../../assets/data/Study3/${useCountry.value}/dimensional/${useCountry.value}_BIC.png`)
    .then(r => r.default)
    .then(r => imgSrc.c = r);
</script>

<template>
    <div>
        <div class="content">
            The specific results of dimensional model in United States, including the loading PCA loading (figure a),
            relationship score within FAVEE space (figure b), and model comparison analysis (figure c).
        </div>
        <div class="img-box">
            <div class="plot-a"><img :src="imgSrc.a" alt=""></div>
            <div class="plot-b">
                <div class="legend"><img src="@/assets/data/Study3/legend/dimensional_b.png" alt=""></div>
                <div id="aR-plot1"></div>
                <div id="aR-plot2"></div>
            </div>
            <div class="plot-c">
                <div class="tit">
                    <div style="width: 155px;">Adjusted R-Square</div>
                    <div style="width: 126px;">
                        <img style="width: 100%;" src="@/assets/data/Study3/legend/dimensional_c1.png" alt="">
                    </div>
                    <div style="width: 300px;">Bayesian Information Criterion(BIC)</div>
                </div>
                <div class="merge-plot"
                    :style="`background-image: url(${imgSrc.b}), url(${imgSrc.c});`">
                </div>
            </div>
            <div class="explain">
                Hover the mouse over the circle, you can see what relationship it is and its position in FAVEE space. Zoom in on an area with the mouse by framing it, and click on the enlarged area to restore it to its original size.
            </div>
        </div>
    </div>
</template>

<style scoped>
.img-box {
    display: flex;
    height: 600px;
    justify-content: space-around;
    flex-direction: column;
    flex-wrap: wrap;
}
.explain {
    display: block;
    background-color: var(--morelightorange);
    padding: 58px 36px;
    width: 438px;
}
.plot-a {
    width: 300px;
    height: 600px;
    overflow: hidden;
    position: relative;
}
.plot-a::before {
    content: "a";
    position: absolute;
    top: 14px;
    left: 14px;
    font-weight: 700;
    font-size: 1.5rem;
}
.plot-a img {
    width: 100%;
}
.plot-b {
    width: 270px;
    height: 600px;
    transform: scale(0.6);
    transform-origin: top left;
    position: relative;
}
.plot-b::before {
    content: "b";
    position: absolute;
    top: 14px;
    left: 14px;
    font-weight: 700;
    font-size: 2.5rem;
}
.plot-b .legend {
    width: 450px;
}
.plot-b .legend img {
    display: block;
    width: 70%;
    margin: 0 auto;
}
.plot-c {
    width: 500px;
    height: 245px;
    transform-origin: top left;
    transform: scale(0.65);
    position: relative;
}
.plot-c::before {
    content: "c";
    position: absolute;
    top: 0px;
    left: 14px;
    font-weight: 700;
    font-size: 2.4rem;
}
.plot-c .merge-plot {
    display: block;
    width: 760px;
    height: 284px;
    background: #fff no-repeat;
    background-position: -131px 0px, 299px 0px;
    background-size: 450px 300px, 450px 300px;
    margin: 0 auto;
}
.plot-c .tit {
    display: block;
    height: 60px;
    width: 760px;
    margin: 0 auto;
    position: relative;
}

.plot-c .tit>div {
    position: absolute;
}
.plot-c .tit>div:nth-child(1) {
    top: calc(60px - 24px);
}
.plot-c .tit>div:nth-child(2) {
    top: 10px;
    left: calc(50% - 63px);
}
.plot-c .tit>div:nth-child(3) {
    top: calc(60px - 24px);
    right: 0;
}
@media screen and (max-width: 1100px) {
    .img-box {
        height: auto;
        flex-direction: row;
    }
    .plot-a {
        order: 1;
    }
    .plot-b {
        order: 2;
    }
    .plot-c {
        margin: 20px 0 0 0;
        order: 4;
    }
    .explain {
        order: 3;
    }
}
@media screen and (max-width: 600px) {
    .plot-c {
        width: 304px;
        height: 150px;
        transform-origin: top left;
        transform: scale(0.4);
    }
    .plot-a {
        order: 1;
    }
    .plot-b {
        order: 2;
    }
    .plot-c {
        order: 4;
    }
    .explain {
        order: 3;
    }
}
</style>