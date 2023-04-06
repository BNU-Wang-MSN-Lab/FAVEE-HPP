<script setup>
import { reactive, provide } from 'vue';
import { csvParse } from 'd3-dsv';
import bannerChoose from '../../../components/bannerChoose.vue';
import { newPlot } from 'plotly.js-dist';

// 单词选项的数据加载
const wordData = reactive({ word: [] });
import("@/assets/data/Study3/averaged_world_model/rels_159.csv?raw")
    .then(r => r.default)
    .then(r => wordData.word = csvParse(r));
provide("bannerChooseWordInputData", wordData);

let plotFA = {};
import("@/assets/data/Study1/Formality_Activeness_only_green.json")
    .then(r => r.default)
    .then(r => {
        newPlot("plot-a", r);
        plotFA = r;
    });

let plotVE = {};
import("@/assets/data/Study1/Valence_Exchange_only_green.json")
    .then(r => r.default)
    .then(r => {
        newPlot("plot-b", r);
        plotVE = r;
    });

const wordChos = (e, i) => {
    if (Object.keys(plotFA).length == 0) return 0; // 加载没完成
    // 移动词到最后一个位置，防止后面乱掉
    wordData.word.push(wordData.word.splice(i, 1)[0])
    // 先复原
    plotFA["data"][0].marker.color[158] = "rgba(218,253,89,1)";
    plotFA["data"][0].marker.line.color[158] = "rgba(218,253,89,1)";
    // 一步到位，把数据移到开头
    plotFA["data"][0].marker.size.push(plotFA["data"][0].marker.size.splice(i, 1)[0]);
    plotFA["data"][0].marker.color.push((plotFA["data"][0].marker.color.splice(i, 1)[0], "rgba(255, 0, 0, 1)"));
    plotFA["data"][0].marker.line.color.push((plotFA["data"][0].marker.line.color.splice(i, 1)[0], "rgba(255, 0, 0, 1)"));
    plotFA["data"][0].y.push(plotFA["data"][0].y.splice(i, 1)[0]);
    plotFA["data"][0].x.push(plotFA["data"][0].x.splice(i, 1)[0]);
    plotFA["data"][0].text.push(plotFA["data"][0].text.splice(i, 1)[0]);
    // 画图
    newPlot("plot-a", plotFA);

    // 先复原
    plotVE["data"][0].marker.color[158] = "rgba(218,253,89,1)";
    plotVE["data"][0].marker.line.color[158] = "rgba(218,253,89,1)";
    // 一步到位，把数据移到开头
    plotVE["data"][0].marker.size.push(plotVE["data"][0].marker.size.splice(i, 1)[0]);
    plotVE["data"][0].marker.color.push((plotVE["data"][0].marker.color.splice(i, 1)[0], "rgba(255, 0, 0, 1)"));
    plotVE["data"][0].marker.line.color.push((plotVE["data"][0].marker.line.color.splice(i, 1)[0], "rgba(255, 0, 0, 1)"));
    plotVE["data"][0].y.push(plotVE["data"][0].y.splice(i, 1)[0]);
    plotVE["data"][0].x.push(plotVE["data"][0].x.splice(i, 1)[0]);
    plotVE["data"][0].text.push(plotVE["data"][0].text.splice(i, 1)[0]);
    // 画图
    newPlot("plot-b", plotVE);
}

const emits = defineEmits(["alertView"]);
const clickEvent = (e) => {
    emits("alertView", e.target.dataset.alertView, e.target.offsetTop + e.target.clientHeight * 1.3);
}
</script>

<template>
    <div class="study1">
        <div class="title">
            Study 1: A Unified Representational Space
        </div>
        <div class="study1-text">
            <div class="content">
                Understanding the nature of social relationships is at the heart of social sciences. A wave of enthusiasm
                from multiple disciplines in the 1970s-1990s explored the elemental forms of human relationships. Different
                theories and taxonomies were developed by psychologists, anthropologists, sociologists, linguists,
                economists, and communication researchers, but no consensus has been reached.
                <div @click="clickEvent" data-alert-view="study1_1">
                    Read more
                </div>
            </div>
            <div class="content">
                In study 1, we created a generalized framework that refined and unified existing theories across multiple
                disciplines. Based on a series of dimensionality reduction techniques, we discovered five fundamental
                dimensions (i.e., FAVEE) that scaffold conceptual space of social relationships: Formality, Activeness,
                Valence, Exchange, Equality.
                <div @click="clickEvent" data-alert-view="study1_2">
                    Read more
                </div>
            </div>
        </div>
        <bannerChoose title="Interactive plot" name="select your relationship of interest"
            choinput="bannerChooseWordInputData" @chos-event="wordChos">
            <div>
                Hover the mouse over the circle to explore all 159 relationships and their positions in the FAVEE space.
                Zoom in on an area with the mouse by framing it (and double click the enlarged area to restore to the
                original size).
            </div>
        </bannerChoose>
        <div style="">
            <img style="display: block; width: 50%; max-width: 300px; margin: 20px auto 0 auto;" src="@/assets/img/science/study1.png" alt="">
        </div>
        <div class="plot">
            <div id="plot-a"></div>
            <div id="plot-b"></div>
        </div>
    </div>
</template>

<style scoped>
.title {
    font-size: 2rem;
    padding: 25px 0 10px 0;
    background-image: linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(var(--orange), var(--orange)),
        linear-gradient(var(--lightblue), var(--lightblue)),
        linear-gradient(var(--lightblue), var(--lightblue));
    background-size: 25px 25px, 10px 11px, 18px 19px, 8px 8px, 10px 27px;
    background-position: 0px 0px, 100% 8px, 100% 0px, calc(100% - 18px) 0px, 100% 0px;
    background-repeat: no-repeat;
    font-weight: 600;
    line-height: 3rem;
}

.plot {
    display: flex;
    margin: 20px 0 40px 0;
    justify-content: space-around;
}

.study1-text {
    display: flex;
    justify-content: space-between;
    margin: 0 0 40px 0;
}

.study1-text .content {
    display: inline-block;
    width: 560px;
    opacity: 0.6;
    color: var(--font-color-body);
    text-align: left;
    vertical-align: top;
}

.study1-text .content>div {
    margin: 20px 0;
    opacity: 0.87;
    text-align: right;
    font-weight: 500;
    color: var(--font-color-link);
    cursor: pointer;
    vertical-align: middle;
}

.study1-text .content>div::after {
    content: "";
    display: inline-block;
    width: 20px;
    height: 1px;
    margin: 0 5px;
    background-color: var(--font-color-link);
    vertical-align: middle;
}

@media screen and (max-width: 1200px) {
    .title {
        margin: 0 20px;
    }

    .study1-text {
        flex-direction: column;
        align-items: center;
    }

    .study1-text .content {
        width: 80%;
    }

    .plot {
        flex-wrap: wrap;
    }
}

@media screen and (max-width: 600px) {
    .plot {
        height: 650px;
        transform-origin: top center;
        transform: scale(0.7);
    }

    .title {
        font-size: 1.5rem;
    }
}
</style>