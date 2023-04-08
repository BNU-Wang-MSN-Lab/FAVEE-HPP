<template>
    <div class="favee-radar-image" :style="`background-image: url(${imgSrc}); width: ${width}px; height: ${height}px;`">
        <div v-for="v in data" :style="`top: ${v.y}px; left: ${v.x}px`">{{ v.name }}</div>
    </div>
</template>

<script setup>
import { ref, onMounted, watch, inject } from "vue";
const prop = defineProps({
    img: String,
    width: {
        type: Number,
        default: 450
    },
    height: {
        type: Number,
        default: 450
    }
});
const country = inject("chooseCountry");
const counList = {
    "China(mainland)": "CHN",
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

const imgSrc = ref("");
onMounted(() => {
    if (prop.img.indexOf("r-") < 0) {
        import(`@/assets/data/Study3/averaged_world_model/FAVEE/${prop.img}.png`)
            .then(r => imgSrc.value = encodeURI(r.default));
    } else {
        import(`@/assets/data/Study3/${useCountry.value}/categorical/radar/${prop.img.replace("r-", "")}.png`)
            .then(r => imgSrc.value = encodeURI(r.default));
    }
});
watch(prop, (n, o) => {
    if (n.img.indexOf("r-") != 0) {
        import(`@/assets/data/Study3/averaged_world_model/FAVEE/${prop.img}.png`)
            .then(r => imgSrc.value = encodeURI(r.default));
    } else {
        import(`@/assets/data/Study3/${useCountry.value}/categorical/radar/${prop.img.replace("r-", "")}.png`)
            .then(r => imgSrc.value = encodeURI(r.default));
    }
});
// 计算坐标
const data = [
    { name: "Formality" },
    { name: "Equality" },
    { name: "Exchange" },
    { name: "Valence" },
    { name: "Activeness" }
];
let width, height;
if (document.body.clientWidth < 600) {
    width = prop.width / 2;
    height = prop.height / 2;
} else {
    width = prop.width;
    height = prop.height;
}
const cx = width * (225 / 450);
const cy = height * (225 / 450);
const r = width * (150 / 450);
data.forEach((v, i) => {
    v.x = cx + r * Math.cos((-90 + (360 / data.length) * i) * (Math.PI / 180)) - (v.name.length / 2) * 4;
    v.y = cy + r * Math.sin((-90 + (360 / data.length) * i) * (Math.PI / 180));
});
</script>

<style scoped>
.favee-radar-image {
    display: block;
    margin: 0 auto;
    background-size: contain;
    background-position: 0px 17px;
    position: relative;
}

.favee-radar-image>div {
    display: block;
    position: absolute;
}
</style>