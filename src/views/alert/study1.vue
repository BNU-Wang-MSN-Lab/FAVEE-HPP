<script setup>
</script>

<template>
    <div class="box">
        <div class="title">Study 1 details</div>
        <div class="content">
            <p>We used a series of dimensionality reduction techniques (e.g., PCA, ICA, EFA, MDS) to find the five prominent dimensions.</p>
            <p>Further, by using model comparison methods, we found FAVEE model substantially outperformed other 15 existing theories.</p>
        </div>
    </div>
</template>

<style scoped>
.box {
    width: calc(100% - 50px);
    height: 90%;
    margin: 10% 0 0 50px;
    border: none;
    box-shadow: none;
    text-align: left;
}
.title {
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}

.content {
    width: 700px;
    font-size: 16px;
    line-height: 24px;
}
</style>