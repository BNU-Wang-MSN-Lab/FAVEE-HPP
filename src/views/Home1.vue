<script setup>

</script>

<template>
    <div class="box">
        <div class="text">
            <p style="font-size: 24px; font-weight: 700;">Scientific Questions</p>
            <p style="font-size: 18px; font-weight: 700;">
                1. What are the basic building blocks of human relationships?
            </p>
            <p>
                Cognitive science suggests that human mind organizes conceptual knowledge primarily in two way: dimensions
                and categories. For example, emotions can be either category-like (e.g., fear, anger, joy) or dimension-like
                (e.g., valence and arousal).
            </p>
            <p>
                Categorical thinking is pervasive when people manage relationships in daily life. We arrange phone contacts
                with categorical labels, assign seating for wedding guests by groups, and buying different travel souvenirs
                for friends, relatives, and work colleagues.
            </p>
            <p>
                Social relationships can also be understood via numerous featural dimensions. For example, people describe
                relationships by spatial distance (e.g., neighbors, long-distance lovers), temporal order (e.g., fiancé,
                ex-husband), and activeness (e.g., strangers, casual acquaintances, close friends).
            </p>
            <p>
                Our research identified the basic building blocks of social relationship concepts. They are <strong>five
                    principal dimensions:</strong>
            </p>
            <p style="font-size: 11px; margin: 0 0 0 2em;">
                1) <span style="text-decoration: underline;">F</span>ormality (whether a relationship is formal or informal?)<br/>
                2) <span style="text-decoration: underline;">A</span>ctiveness (whether a relationship is close or distant?)<br/>
                3) <span style="text-decoration: underline;">V</span>alence (whether a relationship is harmony or full of conflict?)<br/>
                4) <span style="text-decoration: underline;">E</span>xchange (whether to exchange concrete resources like money or symbolic resources like love?)<br/>
                5) <span style="text-decoration: underline;">E</span>quality (whether people is equal or inequal?)
            </p>
            <p>
                and <strong>three core categories</strong>: <span style="font-size: 11px;"><span style="text-decoration: underline;">H</span>ostile relationships, <span style="text-decoration: underline;">P</span>ublic relationships, and <span style="text-decoration: underline;">P</span>rivate relationships.</span>
            </p>
            <p>
                This is called the ‘<strong>FAVEE-HPP</strong>’ model of human relationships.
            </p>
        </div>
        <div class="img">
            <div class="box1">
                <img style="width: 50%;" src="/assets/imgs/new/图片2.png" alt="">
                <img style="width: 50%;" src="/assets/imgs/new/图片3.png" alt="">
            </div>
            <img style="width: 100%;" src="/assets/imgs/new/图片4.png" alt="">
        </div>
    </div>
</template>

<style scoped>
div.box {
    margin: 0 auto;
    position: relative;
    font-size: 14px;
    line-height: 1em;
}

.text {
    grid-area: 1 / 2 / 2 / 7;
    text-align: left;
}

.img {
    grid-area: 1 / 7 / 2 / 10;
}

.img img {
    width: 100%;
    vertical-align: middle;
}

.img .box1 img {
    display: inline-block;
    width: 50%;
    vertical-align: middle;
}
</style>