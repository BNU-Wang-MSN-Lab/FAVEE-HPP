<template>
    <div class="geo-world">
        <div class="svg">
        </div>
    </div>
</template>

<script setup>
import { onMounted, inject, watch } from "vue";
import * as d3 from "d3";

const emits = defineEmits(["updateChosOpts", "updateChosOpt"]);

const chooseCountry = inject("chooseCountry");
watch(chooseCountry, (n, o) => {
    mapPath
        .transition().duration(100)
        .attr("fill", d => countries.indexOf(d.properties.COUNTRY) >= 0 ? (d.properties.COUNTRY == n ? "#ff00ff" : "#000000") : "#e3e3e3")
});
const countries = [
    "China",
    'Hong Kong SAR',
    "United States",
    "United Kingdom",
    "Australia",
    "South Africa",
    "Germany",
    "Japan",
    "Israel",
    "France",
    "Russian Federation",
    'Spain', 'Mexico', 'Chile',
    'Portugal', 'Brazil',
    'Egypt', 'Qatar',
    'India'
].sort();

let mapPath = null;
const chosCoun = function (e) {
    emits("updateChosOpt", e);
    mapPath
        .transition().duration(100)
        .attr("fill", d => countries.indexOf(d.properties.COUNTRY) >= 0 ? (d.properties.COUNTRY == chooseCountry.value ? "#ff00ff" : "#000000") : "#e3e3e3")
}
onMounted(() => {
    emits("updateChosOpts", countries);
    const svgWidth = Math.min(document.body.clientWidth * 0.8, 1200 * 0.8);
    const svgHeight = svgWidth * 0.5;
    const padding = 10;
    const svg = d3.select(".svg")
        .append("svg")
        .attr("width", svgWidth)
        .attr("height", svgHeight);

    import("@/assets/data/world_gen.json")
        .then(r => r.default)
        .then(r => {
            const x0 = padding;
            const y0 = padding;
            const x1 = svgWidth - padding * 2;
            const y1 = svgHeight - padding * 2;
            const projection = d3.geoEquirectangular().fitExtent(
                [
                    [x0, y0],
                    [x1, y1],
                ], r);
            
            const pathGenerator = d3.geoPath()
                .projection(projection);

            mapPath = svg.append("g")
                .selectAll("path")
                .data(r.features, d => d.properties.COUNTRY)
                .join("path");
            mapPath.attr("d", pathGenerator)
                .attr("stroke-width", 0.2)
                .attr("stroke", "#fff")
                .style("cursor", d => countries.indexOf(d.properties.COUNTRY) >= 0 ? "pointer" : "#default")
                .attr("fill", d => countries.indexOf(d.properties.COUNTRY) >= 0 ? (d.properties.COUNTRY == chooseCountry.value ? "#ff00ff" : "#000000") : "#e3e3e3")
                .on("click", d => {
                    const data = d.target.__data__;
                    if (countries.indexOf(data.properties.COUNTRY) >= 0) {
                        chosCoun(data.properties.COUNTRY);
                    }
                })
        })
});
</script>

<style scoped>
.svg {
    margin: 50px 0 0 0;
    text-align: center;
}
</style>