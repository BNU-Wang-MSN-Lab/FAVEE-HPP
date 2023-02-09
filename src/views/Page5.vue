<script setup>
import { csvParse } from "d3-dsv";
import $ from "jquery";
import { newPlot } from "plotly.js-dist";
import { onMounted, ref } from "vue";
const emits = defineEmits(["alertOpen"]);

const words = csvParse($.ajax({
    url: "./assets/fuckfeishu/Study3/averaged_world_model/rels_159.csv",
    type: "GET",
    async: false
}).responseText).map(v => v.x);

const wordsData = csvParse($.ajax({
    url: "./assets/fuckfeishu/Study3/averaged_world_model/pca_favee.csv",
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
    document.querySelector("#study3Country").value = e;
    document.querySelector("#p5_radar").style.backgroundImage = `url(./assets/fuckfeishu/Study3/averaged_world_model/FAVEE/${e.replaceAll(" ", "\\ ")}.png)`

    const wo = wordsData[words.indexOf(e)];
    choosedWord.value = wo[""];
    showWord.value = `= \n Formality * (${Math.round(wo["Formality"] * 100) / 100
        })\n + Activeness * (${Math.round(wo["Activeness"] * 100) / 100
        })\n + Valence * (${Math.round(wo["Valence"] * 100) / 100
        })\n + Exchange * (${Math.round(wo["Exchange"] * 100) / 100
        })\n + Equality * (${Math.round(wo["Equality"] * 100) / 100
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
        <div class="s1">
            <span id="study3" style="cursor: pointer; font-size: 20px; line-height: 32px;">Study 3</span>
            <br />
            <span style="font-size: 26px; line-height: 1.5em; font-weight: 700;">
                Universality and cultural variability
            </span>
        </div>
        <div class="s2">
            <div style="font-size: 24px; line-height: 1.5em;">
                <strong>{{ choosedWord }}</strong>{{ showWord }}
            </div>
        </div>
        <div class="s3">
            <div class="title">Select your interested relationship</div>
            <div class="sel">
                <input @input="input" type="text" name="country" id="study3Country" placeholder="Type to search" />
                <ul>
                    <li v-for="i in showWords" @click="chosWord(i)">{{ i }}</li>
                </ul>
            </div>
        </div>
        <div class="s4">
            <div id="p5_radar">
                <div v-if="choosedWord != ''">Formality</div>
                <div v-if="choosedWord != ''">Activeness</div>
                <div v-if="choosedWord != ''">Valence</div>
                <div v-if="choosedWord != ''">Exchange</div>
                <div v-if="choosedWord != ''">Equality</div>
            </div>
        </div>
        <div class="s5">
            <p style="font-size: 24px; line-height: 30px; margin: 0;">World-averaged model</p>
            <p style="font-size: 12px; line-height: 18px; margin: 0;">Check the <span
                    @click="emits('alertOpen', 'alertStudy3')"
                    style="color: var(--theme-color-blue); cursor: pointer;">model
                    details ></span></p>
            <p style="font-size: 16px; line-height: 24px;">Combined with the data in 19 regions, we get the
                world-averaged FAVEE-HPP model. We also find a subset of relationships that is representative of the
                whole conceptual space. Besides, we find that the mental representations of some relationships vary
                across different regions while some relationships are comparably consistence across regions. Our
                analysis shows that religion and modernization are two important factors that contribute to cultural
                variation.</p>
            <p style="font-size: 16px; line-height: 24px;">You can explore the details of your interested relationship.</p>
        </div>
        <div class="s6">
            <div @click="emits('alertOpen', 'alertSubset')">Subset analysis</div>
            <div @click="emits('alertOpen', 'alertRelationship')">Relationship variability</div>
            <div @click="emits('alertOpen', 'alertCultural')">Cultural mechanism</div>
        </div>
        <div class="s7">
            <div id="study3Can"></div>
            <div>
                <img src="/assets/fuckfeishu/Study3/图例/study3_1.png" alt="" />
                <img src="/assets/fuckfeishu/Study3/图例/study3_2.png" alt="" />
                <img src="/assets/fuckfeishu/Study3/图例/study3_3.png" alt="" />
            </div>
            <div>Hover the mouse over the circle, you can see what relationship it is and its position in FAVEE space.
            </div>
        </div>
    </div>
</template>

<style scoped>
.box {
    grid-template-rows: 20px auto auto auto 70px auto auto 40px;
    align-items: stretch;
    text-align: left;
}

.s1 {
    grid-area: 2 / 2 / 3 / 10;
}

.s2 {
    display: flex;
    grid-area: 3 / 2 / 5 / 5;
    justify-content: center;
    align-items: center;
    white-space: pre;
}

.s3 {
    grid-area: 5 / 2 / 6 / 5;
    text-align: center;
}

.sel>input {
    width: 70%;
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
    right: 20%;
    cursor: pointer;
}

.sel>ul {
    display: none;
    width: 60%;
    max-height: 150px;
    padding: 5px;
    border: 2px solid #ababab;
    border-radius: 14px;
    background: #fff;
    position: absolute;
    top: 20px;
    left: 15%;
    overflow-y: scroll;
    user-select: none;
    z-index: 1;
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

.s4 {
    grid-area: 6 / 2 / 8 / 5;
}

#p5_radar {
    width: 400px;
    height: 400px;
    background-position: -36px -13px;
    background-size: 450px 450px;
    position: relative;
}

#p5_radar>div {
    display: block;
    position: absolute;
}

#p5_radar>div:nth-child(1) {
    top: 52px;
    left: 168px;
}

#p5_radar>div:nth-child(2) {
    top: 133px;
    left: 46px;
}

#p5_radar>div:nth-child(3) {
    top: 302px;
    left: 83px;
}

#p5_radar>div:nth-child(4) {
    top: 302px;
    left: 264px;
}

#p5_radar>div:nth-child(5) {
    top: 133px;
    left: 292px;
}

.s5 {
    grid-area: 3 / 5 / 4 / 10;
}

.s6 {
    display: grid;
    grid-area: 4 / 5 / 5 / 10;
    grid-template-columns: repeat(3, auto);
    align-items: start;
    justify-content: start;
    grid-column-gap: 20px;
}

.s6>div {
    display: block;
    padding: 5px 10px;
    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 9px;
    cursor: pointer;
}

.s7 {
    grid-area: 5 / 5 / 8 / 10;
    position: relative;
}

.s7>div:nth-child(2) {
    width: 120px;
    position: absolute;
    top: 30px;
    left: 521px;
}

.s7 img {
    width: 100%;
}
</style>