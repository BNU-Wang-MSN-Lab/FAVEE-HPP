<script setup>
</script>

<template>
    <div class="box">
        <div class="title">Study 2 details</div>
        <div class="content">
            <p>The flow chart illustrates how people conceptualize human relationships via the joint framework of dimensions and categories. Each principal dimension of the FAVEE space functions as a classifier: as all relationships (indicated by word clouds) go through them stepwise, it firstly generates three implicit clusters of HPP (in light blue) and then six explicit clusters (in purple).</p>
            <div class="img"></div>
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
.img {
    width: 100%;
    height: 728px;
    background: url(/assets/Study2.png) no-repeat;
    background-position: bottom right;
    background-size: 2386px 1220px;
}
</style>