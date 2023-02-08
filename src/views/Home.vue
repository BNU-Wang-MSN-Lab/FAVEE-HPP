<script setup>
import { reactive } from 'vue';

const data = reactive({
    href: [
        { name: "GitHub", url: "https://github.com/BNU-Wang-MSN-Lab/FAVEE-HPP" },
        { name: "WangLab Website", url: "http://mirrorneuronwang.com/" },
        { name: "Contacts", url: "https://brain.bnu.edu.cn/English/Faculty/CurrentFaculty/Wzz/72f0d1f123b044e1a6f416a02a249fe1.htm" }
    ]
});

const hrefClick = (e) => {
    const url = e.target.dataset.href;
    let a = document.createElement("a");
    a.href = url;
    a.target = "_blank"
    a.click();
}
</script>

<template>
    <div class="box">
        <div>
            <div class="content">
                <div class="title">
                    Human Relationships
                </div>
                <div style="font-size: 24px; line-height: 30px;">
                    <p>
                        Such an enrich social life we are involved in! Image each relationship is a star in the sky, our
                        human relationship in total is a vast universe. Is there a cognitive map in our mind that guides
                        us to explore this universe?
                    </p>
                    <p>
                        By collecting data across diverse populations in the world, we found the FAVEE-HPP model. Not
                        only it is a unified representational space across disciplines, but it also adapted to various
                        cultures.
                    </p>
                </div>
                <div>
                    <div v-for="i in data.href" class="button" :data-href="i.url" @click="hrefClick">{{ i.name }}</div>
                </div>
            </div>
            <div class="logo">
                <div></div>
                <div></div>
            </div>
        </div>
    </div>
</template>

<style scoped>
div.box {
    margin: 0 auto;
    background-repeat: no-repeat !important;
    background-image: linear-gradient(90deg, white, transparent), url("./assets/imgs/拼图@2x.png") !important;
    background-size: 533px 813px !important;
    background-position: right !important;
    position: relative;
}
.box>div {
    grid-column: 2 / span 6;
}
.content {
    text-align: left;
}

.title {
    color: var(--theme-color-blue);
    font-size: 64px;
    line-height: 76px;
}

.button {
    display: inline-block;
    margin: 0 40px 0 0;
    padding: 8px 10px;
    border: 1px solid var(--theme-color-blue);
    border-radius: 5px;
    color: var(--theme-color-blue);
    cursor: pointer;
}

.logo {
    margin: 30px 0 0 0;
    text-align: left;
}

.logo>div {
    display: inline-block;
    width: 72px;
    height: 72px;
    margin: 10px;
}

.logo>div:nth-child(1) {
    background: url(./assets/icon/Beijing_Normal_University_logo.svg.png) no-repeat;
    background-size: contain;
}

.logo>div:nth-child(2) {
    background: url(./assets/icon/temple-logo-t-box.svg) no-repeat;
    background-size: contain;
}
</style>
