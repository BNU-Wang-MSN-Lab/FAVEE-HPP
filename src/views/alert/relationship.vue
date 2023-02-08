<script setup>
</script>

<template>
    <div class="abox">
        <div class="c1">
            Relationship variablity
        </div>
        <div class="c2">
            <img style="width: 100%;" src="/assets/fuckfeishu/Study3/更新图/Extended Data Fig. 5.png" alt="">
        </div>
        <div class="c3">
            Cultural consensus is higher when it comes to private relationships, but there are significant cultural differences when it comes to public relationships.
        </div>
        <div class="c4">
            Figure a shows the trend that affiliative and power relationships (left word cloud box) varied more across regions, while familial and romantic relationships (right word cloud box) varied less. The font size of word clouds proportionally reflects the familiarity of the relationships. 
            Figure b shows that, for three HPP categories, public relationship concepts had more culturally variable meanings than hostile and private relationship concepts.
        </div>
    </div>
</template>

<style scoped>
.abox {
    display: grid;
    width: 100vw;
    min-height: 100vh;
    grid-template-columns: 20px repeat(8, 1fr) 20px;
    grid-template-rows: 20px repeat(3, auto);
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
    grid-area: 3 / 3 / 5 / 7;
}
.c3 {
    grid-area: 3 / 7 / 4 / 9;
}
.c4 {
    grid-area: 4 / 7 / 5 / 9;
}
</style>