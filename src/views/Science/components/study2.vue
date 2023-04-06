<template>
    <div class="study2">
        <div class="title">
            Study 2: Categorical and dimensional representations
        </div>
        <div class="bg">
            <div class="w1">
                <div class="sub-title" style="text-align: left;">What are the elemental forms of social relationships? </div>
                <div class="content">
                    <p>
                        There is ongoing scholarly debate about whether social relationships are best understood as discrete
                        categories or continuous dimensions. The discrete categories perspective suggests that social
                        relationships can be classified into distinct categories (e.g., acquaintances, family members,
                        friends, and colleagues) and each of these categories has its own unique functions (e.g., kinship
                        for reproduction, friendship for emotional belonging, and business partners for profit exchange).
                        One the other hand, the continuous dimensions perspective suggests that social relationships are not
                        discrete categories, but rather, they exist on a continuum. For example, people often define
                        relationships by spatial proximity (e.g., roommate, neighbors, long-distance lovers) and temporal
                        characteristics (e.g., fiancé, ex-husband, best-friend-forever). Therefore, rather than thinking of
                        friends and acquaintances as distinct categories, they may exist on a continuum of intimacy and
                        trust.
                    </p>
                    <p>
                        Similar debate also exists for other social knowledge, e.g., emotions can be understood either as
                        category-like (e.g., fear, anger, joy) or dimension-like (e.g., valence and arousal), and likewise
                        for personality traits (e.g., ‘big-five dimensions’ vs ‘sixteen Myers-Briggs types’).
                    </p>
                </div>
            </div>
            <div class="w2">
                <div class="what-name-you-like">
                    <div class="cr">
                        <div class="sub-title">Categorical representations</div>
                        <div>
                            <img style="width: 60%;" src="@/assets/img/science/0318.1.png" alt="">
                        </div>
                    </div>
                    <div class="fc">
                        <div class="sub-title">Functional Categories</div>
                        <div class="fc-sub-img">
                            <div>
                                <!-- photo -->
                                <div>
                                    <img src="@/assets/img/science/0318.12.png.png" alt="">
                                </div>
                                <div style="padding: 0 20px;">
                                    <div style="font-weight: 600;">Kinship & Marriage</div>
                                    <div class="thin">（reproduction, nurturing）</div>
                                </div>
                            </div>
                            <div>
                                <!-- photo -->
                                <div>
                                    <img src="@/assets/img/science/0318.11.png.png" alt="">
                                </div>
                                <div style="padding: 0 20px;">
                                    <div style="font-weight: 600;">Workplace/Business</div>
                                    <div class="thin">(labor, economic profit)</div>
                                </div>
                            </div>
                            <div>
                                <!-- photo -->
                                <div>
                                    <img src="@/assets/img/science/0318.9.png.png" alt="">
                                </div>
                                <div style="padding: 0 20px;">
                                    <div style="font-weight: 600;">Friendship</div>
                                    <div class="thin">(trust, support)</div>
                                </div>
                            </div>
                            <div>
                                <!-- photo -->
                                <div>
                                    <img src="@/assets/img/science/0318.10.png.png" alt="">
                                </div>
                                <div style="padding: 0 20px;">
                                    <div style="font-weight: 600;">Enemy & Opponent</div>
                                    <div class="thin">(resource competition)</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="dr">
                        <div class="sub-title">Dimensional representations</div>
                        <div>
                            <img style="width: 80%;" src="@/assets/img/science/0318.2.png" alt="">
                        </div>
                    </div>
                    <div class="fd">
                        <div class="sub-title">Feature <span style="font-size: 1.5rem;
                            font-weight: 600;
                            line-height: 2.25rem;">Dimensions</span></div>
                        <div>
                            <div class="thin"><span>Spatial distance</span>（neighbors, distant relatives）</div>
                            <div class="thin"><span>Temporal label</span>（ex-husband, fiances）</div>
                            <div class="thin"><span>Closeness</span>（stranger, acquaintance, close friends）</div>
                            <div class="thin"><span>Hierarchy</span>(twins, grandparent-grandson)</div>
                            <div>
                                <div style="display: inline-block; width: 50%; text-align: center; font-weight: 600;">Friend
                                    Circle</div>
                                <div style="display: inline-block; width: 50%; text-align: center; font-weight: 600;">Family
                                    Tree</div>
                                <img src="@/assets/img/science/0318.8.png.png" style="width: 100%;" alt="">
                                <div class="thin"
                                    style="display: inline-block; width: 50%; text-align: center; font-weight: 500;">based on
                                    closeness</div>
                                <div class="thin"
                                    style="display: inline-block; width: 50%; text-align: center; font-weight: 500;">based on
                                    hierarchy</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.fd>div:nth-child(2)>div {
    margin: 20px 0;
}

.title {
    font-size: 2rem;
    padding: 25px 0 10px 0;
    background-image: linear-gradient(var(--blue), var(--blue)),
        linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(var(--orange), var(--orange)),
        linear-gradient(var(--lightblue), var(--lightblue)),
        linear-gradient(var(--lightblue), var(--lightblue));
    background-size: 25px 25px, 10px 11px, 18px 19px, 8px 8px, 10px 27px;
    background-position: 0px 0px, 100% 8px, 100% 0px, calc(100% - 18px) 0px, 100% 0px;
    background-repeat: no-repeat;
    font-weight: 600;
    line-height: 3rem;
}

.thin {
    font-size: 0.75rem;
    line-height: 1.25rem;
}

.thin>span {
    font-weight: 600;
}

.bg {
    display: flex;
    justify-content: space-between;
    background-image: linear-gradient(var(--blue), var(--blue)),
        linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(var(--orange), var(--orange)),
        linear-gradient(var(--blue), var(--blue)),
        linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(var(--orange), var(--orange));
    background-size: 10% 10px, 40% 10px, 60% 10px;
    background-position: 100% 0px, 100% 0px, 100% 0px, 0px 100%, 0px 100%, 0px 100%;
    background-repeat: no-repeat;
}

.w1 {
    display: block;
    width: 377px;
}
.w2 {
    display: block;
    width: 759px;
}
.what-name-you-like {
    display: flex;
    padding: 20px 0;
    flex-direction: column;
    justify-content: space-around;
    height: 900px;
    flex-wrap: wrap;
}

.what-name-you-like>div {
    width: 377px;
    overflow: hidden;
}

.what-name-you-like>div img {
    display: block;
    margin: 0 auto;
}

.fc-sub-img>div>div {
    display: inline-block;
    vertical-align: middle;
}

.sub-title {
    margin: 5px 0;
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 2.25rem;
    text-align: center;
}

.content>p {
    opacity: 0.6;
    text-align: left;
    margin: 20px 0 0 0;
    color: var(--font-color-body);
}

@media screen and (max-width: 1200px) {
    .study2 .title {
        margin: 0 20px;
    }
    .bg {
        flex-direction: column;
        align-items: center;
    }
    .w1 {
        display: block;
        width: 80%;
        margin: 20px 0;
    }
}
@media screen and (max-width: 850px) {
    .what-name-you-like {
        height: auto;
        align-items: center;
    }
    .what-name-you-like>div {
        max-width: 300px;
        margin: 20px 0;
    }
    .study2 .title {
        font-size: 1.5rem;
    }
}
</style>