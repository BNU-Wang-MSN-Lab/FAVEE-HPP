<script setup>
import { inject, onMounted, ref } from 'vue';

const show = ref(1);
const chooseCountry = inject("chooseCountry");
</script>
<template>
    <div class="box">
        <div class="select">
            <div :class="{selected: show == 1}" @click="show = 1">Dimentional</div>
            <div :class="{selected: show == 2}" @click="show = 2">Categorical</div>
            <div :class="{selected: show == 3}" @click="show = 3">Demographics</div>
        </div>
        <div class="title">{{ chooseCountry }}</div>
        <div class="button">
            <div>Download Data</div>
            <div>Download Survey</div>
        </div>
        <div class="content">
            <p>The specific results of dimensional model in [region], including the loading PCA loading (figure a),</p>
            <p>relationship score within FAVEE space (figure b), and model comparison analysis (figure c).</p>
        </div>
    </div>
</template>

<style scoped>
.box {
    width: 100%;
    height: 90%;
    margin: 10% 0 0 0;
    border: none;
    box-shadow: none;
}
.select {
    width: 360px;
    margin: auto;
    border: 1px solid var(--theme-color-blue);
    border-radius: 9px;
    cursor: pointer;
}
.select>div {
    width: 120px;
    display: inline-block;
    line-height: 2em;
}
.select>.selected {
    background: var(--theme-color-blue);
    border-radius: 8px;
    color: white;
}
.title {
    font-size: 32px;
    font-weight: 500;
    margin: 40px 0;
}
.button>div {
    display: inline-block;
    padding: 5px 10px;
    margin: 10px 30px;
    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 9px;
    cursor: pointer;
}
.content {
    font-size: 16px;
    line-height: 24px;
}
.content>p {
    margin: 0;
}
</style>