<script setup>
const emits = defineEmits(["alertView"]);
const clickEvent = (e) => {
    emits("alertView", e.target.dataset.alertView, e.target.offsetTop + e.target.clientHeight * 1.3);
}
</script>

<template>
    <div class="study3">
        <div class="title">
            Study 3: Universality and cultural variability of social relationship knowledge
        </div>
        <div class="content">
            As a pre-registration study, we recruited large-scale online participants from 19 global regions with diverse
            ecological (geography, climate, subsistence), biological (genetics, disease) and social-cultural backgrounds
            (language, ethnicity, education, religion, politics, wealth, urbanization). Study 3 aimed to reveal the
            cross-cultural similarity and differences in relationship conceptualization and its underlying cultural
            mechanisms.
            <div class="link" style="text-align: right; color: var(--font-color-link); cursor: pointer;" @click="clickEvent" data-alert-view="study3_1">
                Learn more about demographics 
            </div>
        </div>
        <div class="img">
            <img src="@/assets/img/science/世界地图.png" alt="">
            <img src="@/assets/img/science/relationship_compass.png" alt="">
        </div>
        <div class="sub-tit">
            FAVEE-HPP: A Universal relationship compass across cultures
        </div>
        <div class="content">
            We found that people across the world—Americans, Europeans, Asians, Arabs—all use the same cognitive
            architecture to construct social relationship knowledge, which is the ‘FAVEE-HPP’ framework. This universal
            cognitive map of relationships works as a ‘relationship compass’ to guide and help individuals navigate social
            environments and gives rise to mental models of how people would think, feel and behave in a relationship.
        </div>
        <div class="bottom-img">
            <div class="main">
                <img src="@/assets/img/science/65462.png" alt="">
                United States
            </div>
            <div class="cc">
                <div class="mutil">
                    <div>
                        <img src="@/assets/img/science/Australia.png" alt="">
                        Australia
                    </div>
                    <div>
                        <img src="@/assets/img/science/china.png" alt="">
                        China
                    </div>
                    <div>
                        <img src="@/assets/img/science/France.png" alt="">
                        France
                    </div>
                    <div>
                        <img src="@/assets/img/science/Lsrael.png" alt="">
                        Lsrael
                    </div>
                    <div>
                        <img src="@/assets/img/science/Mexico.png" alt="">
                        Mexico
                    </div>
                    <div>
                        <img src="@/assets/img/science/Portugal.png" alt="">
                        Portugal
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.study3 .content .link::after {
    content: "";
    display: inline-block;
    width: 20px;
    height: 1px;
    background-color: var(--font-color-link);
    vertical-align: middle;
}
.study3 .bottom-img {
    display: flex;
    justify-content: space-around;
    align-items: center;
    color: var(--blue1);
}

.study3 .bottom-img .main {
    display: inline-block;
    width: 350px;
    text-align: center;
}

.study3 .bottom-img .cc {
    display: inline-block;
    width: 700px;
}

.study3 .bottom-img .mutil {
    display: flex;
    flex-wrap: wrap;
}

.study3 .bottom-img .mutil>div {
    width: 200px;
    text-align: center;
}

.study3 .bottom-img img {
    width: 100%;
}

.study3 .title {
    font-size: 2.4rem;
    padding: 25px 0 10px 0;
    background-image: linear-gradient(var(--orange), var(--orange));
    background-size: 25px 25px;
    background-position: 0px 0px;
    background-repeat: no-repeat;
    font-weight: 600;
    line-height: 3rem;
}

.study3 .sub-tit {
    margin: 50px 0 20px 0;
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 2.25rem;
    opacity: 0.87;
    color: var(--font-color-body);
}

.study3 .content {
    text-align: justify;
    opacity: 0.6;
    color: var(--font-color-body);
}

.study3 .img {
    position: relative;
}

.study3 .img>img:nth-child(1) {
    width: 100%;
}

.study3 .img>img:nth-child(2) {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 20%;
}

@media screen and (max-width: 1200px) {

    .study3 .title,
    .study3 .content,
    .study3 .img,
    .study3 .sub-tit {
        margin: 5px 20px;
    }
}

@media screen and (max-width: 1000px) {
    .study3 .bottom-img {
        flex-direction: column;
    }
}

@media screen and (max-width: 800px) {
    .study3 .bottom-img .cc {
        width: 400px;
    }
}

@media screen and (max-width: 600px) {
    .study3 .title {
        font-size: 1.5rem;
        line-height: 2.25rem;
    }

    .study3 .sub-tit {
        font-size: 1.2rem;
    }
    .study3 .bottom-img .mutil {
        justify-content: center;
    }
    .study3 .bottom-img .mutil>div {
        width: 150px;
    }
}</style>