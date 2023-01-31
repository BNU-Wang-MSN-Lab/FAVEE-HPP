<script setup>
</script>

<template>
    <div class="box">
        <div class="title">Demographics</div>
        <div class="content">
            <img src="/assets/demographics.png" />
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
    overflow: hidden scroll;
}
.title {
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}
.content {
    width: 1077px;
    font-size: 16px;
    line-height: 24px;
}
.content img {
    width: 100%;
}
</style>