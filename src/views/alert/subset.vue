<script setup>
</script>

<template>
    <div class="abox">
        <div class="c1">
            Subset Analysis
        </div>
        <div class="c2">
            <img style="width: 100%;" src="/assets/fuckfeishu/Study3/更新图/Extended Data Fig. 8.jpg" alt="">
        </div>
        <div class="c3">
            A subset of 40 relationships was good enough to replicate all findings based on 159 relationships. This subset can be used more efficiently for you when collecting data for a larger set of relationships is not feasible and you can download the data here.
        </div>
        <div class="c4">
            Figure a shows high correlation (Pearson’s r > 0.9) between PCA loading scores derived from the full set versus subsets of relationships (n=40). These relationships were shown in Figure b (font size corresponds to relationship familiarity). As shown in figure c, the RDM across global regions of the subsets is relatively similar to that of the full set. The subsets were good enough to capture the cross-cultural variability of relationship representations and replicate the cultural mechanism, which is shown in figure d.
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
}
.c1 {
    grid-area: 2 / 3 / 3 / 9;
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}
.c2 {
    grid-area: 3 / 3 / 7 / 7;
}
.c3 {
    grid-area: 3 / 7 / 5 / 9;
}
.c4 {
    grid-area: 5 / 7 / 7 / 9;
}
</style>