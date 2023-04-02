<template>
    <div class="study3-2">
        <div class="content"><span>a, </span>For each region, people’s understanding (conceptual beliefs) of ‘neighbors’ was estimated by interrogating its surrounding relationships in the semantic neighborhood of representational space. Fifteen nearest relationship words were selected based on the smallest Euclidean distance with ‘neighbors’ on 33 evaluative features. We found that a country’s modernization level was positively correlated with the formality score of ‘neighbors’ surrounding relationships, but negatively correlated with the activity intensity score. This suggested that, as a country’s modernization level increases, ‘neighbors’ becomes a more public, impersonal, and superficial relationship.</div>
        <div class="content"><span>b, </span>Taken China (middle modernization), Israel (high modernization) and US (highest modernization) as an example. All 159 relationships were plotted in the 2D t-SNE space, with the nearby 15 relationships zoomed in for better visualization. For China, only informal relationships (in red color) surround the Chinese word ‘neighbor’ (‘邻居’), indicating that ‘neighbors’ is considered as a private and personal relationship. But for Israel and the US, more and more public relationships (in blue color) appear nearby, indicating that ‘neighbors’ is conceptualized as being more formal and impersonal. Together, these results demonstrate that, although translation dictionaries provide corresponding/equivalent words of human relationships in different languages, their conceptual meanings are not always the same. Their variations (at least for the concept ‘neighbors’) were dependent on a country’s level of modernization (e.g., ‘neighbors’ in big cities are often unknown to each other due to greater mobility led by urbanization).</div>
        <div class="img-box">
            <div class="l">
                <img src="@/assets/img/science/33.png" alt="">
                <img src="@/assets/img/science/34.png" alt="">
            </div>
            <div class="r">
                <img src="@/assets/img/science/15.png" alt="">
            </div>
        </div>
    </div>
</template>

<style scoped>
.study3-2 .content {
    text-align: justify;
}
.study3-2 .content>span {
    font-size: 1.5rem;
    font-weight: 700;
    line-height: 2.25rem;
}
.study3-2 .img-box {
    display: flex;
    justify-content: space-around;
    padding: 20px 0 0 0;
}
.study3-2 .img-box>div {
    display: block;
    width: 45%;
    position: relative;
}
.l::after {
    content: "a)";
    display: block;
    top: 0;
    left: 0;
    position: absolute;
    font-weight: 800;
}
.r::after {
    content: "b)";
    display: block;
    top: 0;
    left: 0;
    position: absolute;
    font-weight: 800;
}
.l>img {
    width: 50%;
}
.r>img {
    width: 100%;
}

@media screen and (max-width: 900px) {
    .study3-2 .img-box {
        flex-direction: column;
        align-items: center;
    }
    .study3-2 .img-box>div {
        width: 100%;
    }
}
</style>