<script setup>
const emits = defineEmits(["alertOpen"]);
</script>

<template>
    <div class="box">
        <div class="tit">
            <span class="one">Study 1</span>
            <br />
            <span class="two">
                <span style="color: var(--theme-color-blue)">A</span> unified representational space
            </span>
        </div>
        <div class="content">
            <p>We use longitude and latitude to travel across the world. For relationship space, we found there are five
                principal dimensions (formality, activeness, valence, exchange, equality) navigating us.</p>
            <div @click="emits('alertOpen', 'study1')">More details ></div>
        </div>
        <div class="img">
            <img src="/assets/Study1.png" />
        </div>
    </div>
</template>

<style scoped>
.box {
    width: 100%;
    position: relative;
}

.tit {
    text-align: left;
    margin: 70px 0 0 50px;
}

.tit .one {
    font-size: 24px;
    line-height: 30px;
}

.tit .two {
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}

.content {
    text-align: left;
    width: 60%;
    margin: 40px 0 0 60px;
}

.content>div {
    color: var(--theme-color-blue);
    cursor: pointer;
}

.img {
    width: 955px;
    height: 455px;
    margin: 20px auto;
    overflow: hidden;
}

.img img {
    width: 100%;
    transform: scale(1.5) translate(-135px, 90px);
}
</style>