<script setup>
</script>

<template>
    <div class="abox">
        <div class="title">Model details</div>
        <div class="content">
            <p>The dimensional and categorical models derived from global data in Study 3 (n=17,686).</p>
            <p>FAVEE model (figure b) and HPP model (figure c) derived from large-scale global data replicated the
                results in Study 1 and Study 2.</p>
            <p>Four data-driven metrics consistently indicated the optimal number for PCA was five (figure a).</p>
            <img src="/assets/imgs/fig6.png" alt="">
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
.title {
    grid-area: 2 / 3 / 3 / 8;
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}

.content {
    grid-area: 3 / 3 / 6 / 8;
    font-size: 16px;
    line-height: 24px;
}
.content>img {
    width: 100%;
}
</style>