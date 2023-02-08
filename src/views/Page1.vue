<template>
    <div class="box">
        <div class="title">
            <span>T</span>he FAVEE-HPP model
        </div>
        <div class="img">
            <img src="/assets/imgs/favee.png" style="width: 100%;" alt="">
        </div>
        <div class="content1">
            <div>Significance</div>
            <p>The FAVEE-HPP model is a conceptual framework that <strong>represents how we mentally organize the relationship
                knowledge.</strong> We use the model to <strong>describe and explain behaviors</strong> under specific relationships and <strong>make
                predictions</strong> about their future interaction. This framework provides implications on how human cognitive
                processes are systematically configured and adaptively operated for interpersonal contexts.</p>
        </div>
        <div class="content2">
            <p>In a traditional society, we are primarily dependent on our family, friends, and romantic partners, as
                they provide us with protection, unique connection, and love. Our understanding of these private
                relationships is deeply shaped by traditional inheritance (e.g., religious beliefs and rituals). </p>

            <p>Development of modernization leads to a large scale of human community, and evolves into new ways of
                social interaction. We begin to leave our core social network and cooperate with strangers. We adapt to
                exchange with others equally or proportionally to satisfy our various needs. Today's pluralistic world
                is composed of various stories that are used to build consensus, which maintain the stability of public
                life.</p>
        </div>
    </div>
</template>

<style scoped>
.box {
    grid-template-rows: 20px 40px repeat(4, 1fr) 40px;
    grid-row-gap: 0px;
}

.title {
    grid-area: 2 / 2 / 3 / 10;
    text-align: left;
    font-size: 26px;
    line-height: 1.5em;
    font-weight: 700;
}

.img {
    grid-area: 3 / 2 / 7 / 6;
}

.content1 {
    grid-area: 3 / 6 / 5 / 10;
    background: #E7E6E6;
    padding: 5px 30px;
    text-align: left;
    border-radius: 15px;
}
.content1>div {
    font-size: 24px;
    line-height: 1.5em;
    font-weight: 700;
}
.content1>p {
    font-size: 20px;
}

.content2 {
    grid-area: 5 / 6 / 7 / 10;
    text-align: left;
}
</style>