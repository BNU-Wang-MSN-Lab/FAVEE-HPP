<script setup>
import * as d3 from "d3";
import $ from "jquery";
import { inject, onMounted, provide, ref } from "vue";
// import * as topojson from "topojson";

let mapPath = null;
const chooseCountry = inject("chooseCountry");

const emits = defineEmits(["alertOpen"]);

const countries = ["China", "United States"];

const showCoun = ref([]);
showCoun.value = countries;
const input = function (e) {
    if (e.length == 0) {
        showCoun.value = countries;
        return 0;
    }
    showCoun.value = countries.filter(v => v.toLowerCase().search(e.target.value) >= 0)
    if (showCoun.value.length == 1) {
        chosCoun(showCoun.value[0]);
    }
}
const chosCoun = function (e) {
    document.querySelector("#regionChoose").value = e;
    chooseCountry.value = e;
    mapPath
        .transition().duration(100)
        .attr("fill", d => countries.indexOf(d.properties.COUNTRY) >= 0 ? (d.properties.COUNTRY == chooseCountry.value ? "#ff00ff" : "#000000") : "#e3e3e3")
}
onMounted(() => {
    const svgWidth = (document.querySelector("#p6_1").clientWidth - 60) * (6 / 8);
    const svgHeight = document.querySelector("html").clientHeight * 0.8;
    const padding = 10;
    const svg = d3.select(".svg")
        .append("svg")
        .attr("height", svgHeight)
        .attr("width", svgWidth);

    $.ajax({
        url: "./data/world_gen.geojson",
        type: "GET",
        dataType: "json",
        success: (e) => {
            // const data = topojson.feature(e, e.objects.coastline_110m);
            const x0 = padding;
            const y0 = padding;
            const x1 = svgWidth - padding * 2;
            const y1 = svgHeight - padding * 2;
            const projection = d3.geoEqualEarth().fitExtent(
                [
                    [x0, y0],
                    [x1, y1],
                ], e);
            const pathGenerator = d3.geoPath()
                .projection(projection);

            mapPath = svg.append("g")
                .selectAll("path")
                .data(e.features, d => d.properties.COUNTRY)
                .join("path");
            mapPath.attr("d", pathGenerator)
                .attr("stroke-width", 0.5)
                .attr("stroke", "#fff")
                .attr("fill", d => countries.indexOf(d.properties.COUNTRY) >= 0 ? (d.properties.COUNTRY == chooseCountry.value ? "#ff00ff" : "#000000") : "#e3e3e3")
                .on("click", d => {
                    let data = d.target.__data__;
                    if (countries.indexOf(data.properties.COUNTRY) >= 0) {
                        chosCoun(data.properties.COUNTRY);
                    }
                });
        }
    });
});
</script>

<template>
    <div class="box">
        <div class="s1" id="p6_1">
            <p style="font-size: 24px; line-height: 30px;">Explore your region</p>
            <p style="font-size: 16px; line-height: 24px; margin: 20px 0 10px 10px;">You can explore more details in
                your interested region.</p>
        </div>
        <div class="s2">
            <div class="svg">
            </div>
            <div class="button" :class="{ hidden: chooseCountry == null }" @click="emits('alertOpen', 'alertRegion')">
                Check selected region
            </div>
            <div v-if="chooseCountry == null">
                Select your interested region for more details by clicking the black area on the map.
            </div>
        </div>
        <div class="s3">
            <div class="sel">
                <input type="text" id="regionChoose" name="regionChoose" placeholder="Type to search" @input="input" />
                <ul>
                    <li v-for="i in showCoun" @click="chosCoun(i)">{{ i }}</li>
                </ul>
            </div>
        </div>
    </div>
</template>

<style scoped>
.box {
    grid-template-rows: 20px auto auto 40px;
    align-items: center;
}

.s1 {
    grid-area: 2 / 2 / 3 / 10;
    text-align: left;
}

.s2 {
    grid-area: 3 / 4 / 4 / 10;
}

.button {
    width: 200px;
    margin: auto;
    padding: 9px;
    background: var(--theme-color-blue);
    border-radius: 9px;
    color: white;
    z-index: 1;
    cursor: pointer;
    user-select: none;
}

.s3 {
    grid-area: 3 / 2 / 4 / 4;
}

.sel>input {
    width: 100%;
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
    margin: 0 0 200px 0;
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
    right: 5%;
    cursor: pointer;
}

.sel>ul {
    display: none;
    width: 90%;
    max-height: 150px;
    padding: 5px;
    border: 2px solid #ababab;
    border-radius: 14px;
    background: #fff;
    position: absolute;
    top: 20px;
    left: 0px;
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

.hidden {
    display: none;
}
</style>