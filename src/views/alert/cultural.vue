<script setup>
</script>

<template>
    <div class="abox">
        <div class="c1">
            Cultural mechanism
        </div>
        <div class="c2">
            <img style="width: 100%;" src="/assets/fuckfeishu/Study3/更新图/Fig.-3.jpg" alt="">
        </div>
        <div class="c3">
            <p>
                Relationship conceptualization is both universal and culturally variable. 
            </p>
            <p>
                Common underlying structures such as FAVEE dimensions and HPP categories were stably and consistently observed across global regions (shown in figure a). Meanwhile, relationship words could also vary in meaning across cultures. The groupings of representational geometry across global regions identified six sets of groups (shown in figure b). Their variation was found to be tied to religion and modernization differences between regions (shown in c).
            </p>
        </div>
    </div>
</template>

<style scoped>
.abox {
    display: grid;
    width: 100vw;
    min-height: 100vh;
    grid-template-columns: 20px repeat(8, 1fr) 20px;
    grid-template-rows: 20px repeat(5, auto);
    text-align: left;
    align-items: start;
    line-height: 2em;
}
.c1 {
    grid-area: 2 / 3 / 3 / 9;
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}
.c2 {
    grid-area: 3 / 3 / 7 / 6;
}
.c3 {
    grid-area: 3 / 6 / 7 / 8;
}
.c3 p {
    margin: 0 0 40px 0;
}
</style>