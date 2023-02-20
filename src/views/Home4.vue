<script setup>
import { reactive, ref } from 'vue';

const data = reactive({
    imgs: [
    ]
});
for(let i = 22; i<46; i++) {
    data.imgs.push(`图片${i}.jpg`);
}
</script>

<template>
    <div class="box">
        <div class="text">
            <p style="font-size: 18px; font-weight: 700;">
                Diversity of Social Relationships
            </p>
            <p>
                We build connections with a wide range of people in our families, schools, workplaces, neighborhoods, and online communities. How do we make sense of such complex systems of social relationships?  Can you identify those social relationships played in Leonardo DiCaprio’s movie world?  Hover the mouse over the icon to reveal the answer. 
            </p>
        </div>
        <div class="img">
            <div v-for="i in data.imgs">
                <img style="width: 100%;" :src="`/assets/imgs/new/${i}`" alt="">
            </div>
        </div>
    </div>
</template>

<style scoped>
div.box {
    min-height: 0px;
    grid-template-rows: auto auto;
    margin: 0 auto;
    position: relative;
    font-size: 14px;
    line-height: 1em;
}

.text {
    grid-area: 1 / 2 / 2 / 10;
    text-align: left;
}

.img {
    display: flex;
    flex-flow: row wrap;
    margin: 0 auto;
    max-width: 972px;
    align-items: end;
    grid-area: 2 / 2 / 3 / 10;
}
.img>div {
    flex: 0 0 calc(100% / 8);
}
.img>div:nth-child(odd) {
    height: calc(200px);
}
.img img {
    border-radius: 50% 50%;
}
</style>