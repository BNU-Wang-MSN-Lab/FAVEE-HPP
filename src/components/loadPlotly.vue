<template>
    <div class="load-plotly" :class="{ noclick: hasClick == 0 }"
        :style="`width: ${cWid}px; height: ${cHei}px; ${hasClick ? '' : 'background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url(' + imgSrc + '); background-size: contain;'}`"
        @click.once="loadClick">
        <slot />
    </div>
</template>

<script setup>
const emits = defineEmits(["loadPlot"]);
const props = defineProps({
    imgSrc: String,
    width: {
        type: Number,
        default: 600
    },
    height: {
        type: Number,
        default: 500
    },
    hasClick: {
        type: Number,
        default: 0
    }
});
const cWid = document.body.clientWidth > 650 ? props.width : props.width / 2;
const cHei = document.body.clientWidth > 650 ? props.height : props.height / 2;
const loadClick = () => {
    emits("loadPlot", "start");
};
</script>

<style scoped>
.load-plotly {
    display: block;
    margin: 0 auto;
    overflow: hidden;
    position: relative;
}

.load-plotly.noclick::after {
    content: "click here to load";
    display: block;
    position: absolute;
    top: calc(50% - 12px);
    left: calc(50% - 68px);
    color: var(--font-color-white);
}</style>