<script setup>
import * as d3 from "d3";
import $ from "jquery";
import { inject, onMounted, provide, ref } from "vue";
// import * as topojson from "topojson";
const chooseCountry = inject("chooseCountry");

const emits = defineEmits(["alertOpen"]);
onMounted(() => {
    const countries = ["China", "United States"];
    const svgWidth = 1280;
    const svgHeight = 600;
    const padding = 30;
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

            const mapPath = svg.append("g")
                .style("transform", "translate(-65px, 0px)")
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
                        chooseCountry.value = data.properties.COUNTRY;
                        mapPath
                            .transition().duration(500)
                            .attr("fill", d => countries.indexOf(d.properties.COUNTRY) >= 0 ? (d.properties.COUNTRY == chooseCountry.value ? "#ff00ff" : "#000000") : "#e3e3e3")
                    }
                });
        }
    });
});
</script>

<template>
    <div class="box">
        <div class="content">
            <p style="font-size: 24px; line-height: 30px; margin: 65px 0 0 0;">Explore your region</p>
            <p style="font-size: 16px; line-height: 24px; margin: 20px 0 10px 10px;">You can explore more details in
                your interested region.</p>
        </div>
        <div class="iBox">
            <div class="svg">
                <div class="button" :class="{ hidden: chooseCountry == null }" @click="emits('alertOpen', 'alertRegion')">
                    Check selected region
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.box {
    width: 100%;
    position: relative;
    overflow: hidden;
}

.content {
    text-align: left;
    width: 70%;
    margin: 40px 0 0 60px;
}

.iBox {
    width: 1280px;
    height: 700px;
}

.iBox>.svg {
    width: 100%;
    height: 600px;
    position: relative;
    overflow: hidden;
}

.button {
    position: absolute;
    bottom: 0;
    left: calc(50% - 109px);
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

.hidden {
    display: none;
}
</style>