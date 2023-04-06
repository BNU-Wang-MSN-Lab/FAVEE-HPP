<script setup>
const emits = defineEmits(["alertView"]);
const clickEvent = (e) => {
    emits("alertView", e.target.dataset.alertView, e.target.offsetTop + e.target.clientHeight * 1.3);
}
</script>

<template>
    <div class="study2-end">
        <div class="txt">
            Computational modelling suggests that social relationship concepts can be represented either as continuous
            dimensions or discrete categories. These two forms can co-exist in the same representational space and organized
            in a systematic way. Specifically, all relationship concepts emerge from a multidimensional feature space that
            can be reduced to five fundamental components (FAVEE), and the conceptual similarity between each relationship
            can be represented as the distance in the FAVEE space. Once the spatial proximity among relationships is close
            enough along certain featural dimensions, they can be self-clustered into discrete categories (e.g., three
            implicit categories or six explicit categories). In other words, HPP categories emerge from FAVEE dimensions,
            and relationship taxonomies can be understood as discrete sets of categories living in a continuous dimensional
            space .
            <div @click="clickEvent" data-alert-view="study2_1">Read more</div>
        </div>
        <div class="img">
            <img src="@/assets/img/science/Extended_Data_Fig._5.png" alt="">
        </div>
    </div>
</template>

<style scoped>
.study2-end {
    display: flex;
    padding: 50px 0 17px 0;
    margin: 40px 0;
    justify-content: space-around;
    background-repeat: no-repeat;
    background-image: linear-gradient(var(--orange), var(--orange)),
        linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(var(--blue), var(--blue)),
        linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(var(--orange), var(--orange)),
        linear-gradient(var(--lightblue), var(--lightblue)),
        linear-gradient(var(--lightblue), var(--lightblue));
    background-size: 10% 17px, 25% 17px, 33% 17px, 14px 14px, 24px 24px, 10px 10px, 14px 37px;
    background-position: 0px 100%, 0px 100%, 0px 100%, 100% calc(100% - 10px), 100% 100%, calc(100% - 24px) 100%, 100% 100%;
}

.study2-end .txt {
    display: inline-block;
    width: 45%;
    text-align: left;
    opacity: 0.6;
    color: var(--font-color-body);
}

.study2-end .txt>div {
    margin: 20px 0 20px 120px;
    opacity: 0.87;
    text-align: left;
    font-weight: 500;
    color: var(--font-color-link);
    cursor: pointer;
    vertical-align: middle;
}

.study2-end .txt>div::after {
    content: "";
    display: inline-block;
    width: 20px;
    height: 1px;
    margin: 0 5px;
    background-color: var(--font-color-link);
    vertical-align: middle;
}

.study2-end .img {
    display: inline-block;
    width: 45%;
}

.study2-end .img>img {
    width: 100%;
}

@media screen and (max-width: 1200px) {
    .study2-end {
        flex-direction: column;
        align-items: center;
    }
    .study2-end .txt {
        width: 80%;
    }
    .study2-end .txt>div {
        margin: 20px 0 20px 65%;
    }
}

@media screen and (max-width: 600px) {
    .study2-end {
        margin: 0 0 40px 0;
    }
}
</style>