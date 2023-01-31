<script setup>
</script>

<template>
    <div class="box">
        <div class="title">Model details</div>
        <div class="content">
            <p>The dimensional and categorical models derived from global data in Study 3 (n=17,686).</p>
            <p>FAVEE model (figure b) and HPP model (figure c) derived from large-scale global data replicated the
                results in Study 1 and Study 2.</p>
            <p>Four data-driven metrics consistently indicated the optimal number for PCA was five (figure a).</p>
            <img src="/assets/fig/fig6.png" alt="">
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
    overflow: scroll;
}
.title {
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}

.content {
    width: 100%;
    font-size: 16px;
    line-height: 24px;
}
.content>p {
    width: 700px;
}
.content>img {
    width: 75%;
}
</style>