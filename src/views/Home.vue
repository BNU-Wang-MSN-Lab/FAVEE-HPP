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
                <div style="font-size: 18px; line-height: 25px;">
                    <p>
                        A defining characteristic of Homo sapiens is the richness and complexity of our social
                        relationships. In the last 50 years, both social sciences and biological sciences have sought to
                        understand the nature of social relationships. Different theoretical models and taxonomies have been
                        developed by psychologists, sociologists, anthropologists, linguists, economists, biologists, and
                        communication researchers, but no consensus has been reached.
                    </p>
                    <p>
                        To address this long-standing question, we collected large-scale behavioral data across diverse
                        populations in the world to investigate how social relationship are represented and organized in the
                        human mind. We revealed the universality and cultural variability in the ways that people
                        conceptualize social relationships and elucidated the cognitive structures and cultural principles
                        underlying social relationship knowledge.
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
    background-image: linear-gradient(90deg, white, transparent), url("/assets/imgs/拼图@2x.png") !important;
    background-size: 35vw 100vh !important;
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
    font-size: 60px;
    line-height: 60px;
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
    background: url(/assets/icon/Beijing_Normal_University_logo.svg.png) no-repeat;
    background-size: contain;
}

.logo>div:nth-child(2) {
    background: url(/assets/icon/temple-logo-t-box.svg) no-repeat;
    background-size: contain;
}</style>
