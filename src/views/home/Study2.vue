<script setup>
const emits = defineEmits(["alertOpen"]);
</script>

<template>
    <div class="box">
        <div class="tit">
            <span class="one" id="study2">Study 2</span>
            <br />
            <span class="two">
                <span style="color: var(--theme-color-blue)">C</span>ategorial and dimensional representations
            </span>
        </div>
        <div class="content">
            <p>Like the galaxy in the universe, relationships can also be clustered into different categories. Although we found a cognitive space in Study 1, categorical thinking is pervasive when people manage relationships in daily life, such as arranging messages and phone contacts with labels, assigning seating for wedding guests by groups, and buying different travel souvenirs for friends, relatives and work colleagues.</p>
            <p>Using three behavior tasks, we found the categorical model. The multi-arrangement task and dimensional survey (model 1 and 3) both indicated three core clusters (i.e., hostile, private, and public, abbreviated as HPP) whereas the free sorting task (model 2) identified six clusters (i.e., hostile, romantic, familial, affiliative, transactional, and power).</p>
            <p>Model comparison analysis suggested that models 3 (HPP), 6 (FAVEE) and 7 (FAVEE-HPP) had the highest cross-subject reliability, despite no difference between three of them.</p>
            <div @click="emits('alertOpen', 'alertStudy2')">More details ></div>
        </div>
        <div class="imgBox">
            <div class="img1">
            </div>
            <div class="img2">
                <div style="background-size: 1775px; background-position: -925px top;"></div>
                <div style="background-size: 1775px; background-position: top right;"></div>
            </div>
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
    width: 70%;
    margin: 40px 0 0 60px;
}

.content>div {
    color: var(--theme-color-blue);
    cursor: pointer;
}
.imgBox {
    width: 100%;
    margin: 0 auto 50px auto;
}
.imgBox .img1 {
    display: inline-block;
    width: 696px;
    height: 822px;
    background: url(/assets/Study2.png) no-repeat;
    background-size: 1344px;
    vertical-align: middle;
    overflow: hidden;
}
.imgBox .img2 {
    display: inline-block;
    width: 430px;
    height: 828px;
    vertical-align: middle;
    overflow: hidden;
}
.imgBox .img2>div {
    display: block;
    width: 430px;
    height: 414px;
    background: url(/assets/Study2.png) no-repeat;
}
</style>