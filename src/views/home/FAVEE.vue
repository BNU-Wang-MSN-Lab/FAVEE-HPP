<script setup>

</script>

<template>
    <div class="box">
        <div class="img"></div>
        <div class="content">
            <div class="title">
                <span>T</span>he FAVEE-HPP model
            </div>
            <div>
                <p>
                    During our growth, we connect with lots of people. Families provide us with a sense of safety, where our parents protect us. We find identity in friendship and find a unique connection with our true love. We are primarily dependent on our family, friends, and romantic partners in a traditional society, which constitutes our private life. Our understanding of relationships is deeply shaped by traditional inheritance (e.g., religious beliefs and rituals). Development of modernization leads to a large scale of human community, and evolves into new ways of social interaction. We begin to leave our core social network and cooperate with strangers. In contrast to our private lives, we adapt to exchange with others equally or proportionally to satisfy our various needs, ranging from eating to spiritual fulfillment. The pluralistic world of today is composed of a variety of stories that are used to build consensus, which maintain the stability of public life.
                </p>
                <p>
                    Through direct experience and indirect observation in different cultural backgrounds, we form our typical knowledge of people's relationships, which we call the FAVEE-HPP model. We use the model to describe and explain behaviors under specific relationships and make predictions about their future interaction. The framework provides implications on how human cognitive processes (e.g., actions, affects, motives, languages, decisions) are systematically configured and adaptively operated for interpersonal contexts.
                </p>
            </div>
        </div>
    </div>
</template>

<style scoped>
.box {
    width: 100%;
    height: 100%;
    position: relative;
}
.content {
    width: 42%;
    position: absolute;
    left: 0;
    top: 65px;
    text-align: left;
    margin: 0 0 0 68px;
    word-break: keep-all;
}
.content p {
    font-size: 16px;
    line-height: 24px;
}
.title {
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}
.title>span {
    color: var(--theme-color-blue);
}
.img {
    width: 50%;
    height: 100%;
    background: url(/assets/favee.png) no-repeat;
    background-size: contain;
    background-position: bottom;
    position: absolute;
    right: 5%;
}
</style>