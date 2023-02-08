<script setup>
</script>

<template>
    <div class="abox">
        <div class="c1">
            Study 1 details
        </div>
        <div class="c2">
            <img style="width: 100%;" src="/assets/fuckfeishu/Study1/Supplementary Fig. 1.jpg" alt="" />
        </div>
        <div class="c3">
            <span>
                In complementary to the PCA, we used a series of dimensionality reduction techniques (e.g., ICA, EFA,
                MDS, and network analysis) corresponding to figure a-c, e, and also found the five prominent dimensions
                (i.e., FAVEE). Figure d showed that <strong>FAVEE model seems to be very stable and generalizable across
                    analytical techniques.</strong>
            </span>
        </div>
        <div class="c4">
            <img style="width: 100%;" src="/assets/fuckfeishu/Study1/study1_model_comparison.png" alt="" />
        </div>
        <div class="c5">
            <span>
                Further, by using model comparison methods, we found <strong>FAVEE model substantially outperformed other 15 existing theories.</strong>
            </span>
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
    align-items: stretch;
}

.c1 {
    grid-area: 2 / 3 / 3 / 6;
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}

.c2 {
    grid-area: 3 / 3 / 7 / 6;
}

.c3 {
    grid-area: 3 / 6 / 4 / 9;
}

.c4 {
    grid-area: 4 / 6 / 5 / 9;
}

.c5 {
    grid-area: 5 / 6 / 6 / 9;
}
</style>