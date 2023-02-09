<script setup>
</script>

<template>
    <div class="abox">
        <div class="c1">
            <div class="title">Demographics</div>
            <div>
                In total, we collected 19,532 participants, across 19 global regions and 10 international languages, to examine the universality and cultural variability in the way people conceptualize social relationships.
            </div>
            <div>
                <img style="width: 100%;" src="/assets/fuckfeishu/Homepage/Supplementary-Fig.-7.jpg" alt="">
            </div>
        </div>
    </div>
</template>

<style scoped>
.abox {
    display: grid;
    width: 100vw;
    min-height: 100vh;
    grid-template-columns: 20px repeat(8, 1fr) 20px;
    grid-template-rows: 20px 1fr;
    text-align: left;
    align-items: stretch;
}
.c1 {
    grid-area: 2 / 3 / 3 / 7;
}
.title {
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}
</style>