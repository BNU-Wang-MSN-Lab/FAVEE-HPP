<script setup>

</script>

<template>
    <div class="box">
        <div class="title">
            <p style="font-size: 18px; font-weight: 700;">
                3. Do people around the world share the same understanding of social relationships?
            </p>
        </div>
        <div class="left">
            <div style="width: 100%;">
                <img style="display: inline-block; width: calc(100% / 3); vertical-align: middle;" src="/assets/imgs/new/图片17.png" alt="">
                <img style="display: inline-block; width: calc(100% / 3); vertical-align: middle;" src="/assets/imgs/new/图片18.png" alt="">
                <img style="display: inline-block; width: calc(100% / 3); vertical-align: middle;" src="/assets/imgs/new/图片19.png" alt="">
            </div>
            <p>
                All human cultures have rich vocabularies devoted to describing social relationships. Translation dictionaries, for example, suggest that the English word ‘neighbors’ can be equated with the Chinese word ‘邻居’ and the Hebrew word ‘שכנים'. But does this mean that the conceptual meaning of ‘neighbors’ is the same in the US, China, and Israel?
            </p>
            <p>
                Our research suggest that people’s understandings of social relationships vary across places and times, although translation dictionaries provide corresponding/equivalent relationship vocabularies for different languages. We found people around the world hold similar views on familial and romantic relationships (e.g., ‘wife-husband’) but have a different understanding on public relationships (e.g., ‘leader-follower’). Cultural variations in relationship conceptualization are primarily driven by two cultural factors — religion and modernization. For example,  as a country’s modernization level increases, ‘neighbors’ become a more formal and superficial relationship. For traditional countries like Mainland China, ‘neighbors’ is considered as a private, personal and active relationship. But for highly modernized countries like the US, ‘neighbors’ is conceptualized as a more public, impersonal, and passive relationship. 
            </p>
        </div>
        <div class="right">
            <img style="width: 80%;" src="/assets/imgs/new/图片20.png" alt="">
            <img style="width: 80%;" src="/assets/imgs/new/图片21.png" alt="">
        </div>
    </div>
</template>

<style scoped>
div.box {
    min-height: 0px;
    margin: 0 auto;
    position: relative;
    grid-template-rows: 32px auto;
    font-size: 14px;
    line-height: 1.2em;
}
.title {
    grid-area: 1 / 2 / 2 / 10;
    text-align: left;
}
.left {
    grid-area: 2 / 2 / 3 / 7;
    text-align: left;
}

.right {
    grid-area: 2 / 7 / 3 / 10;
}</style>