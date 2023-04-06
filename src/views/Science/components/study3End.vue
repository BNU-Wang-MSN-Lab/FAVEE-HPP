<script setup>
const emits = defineEmits(["alertView"]);
const clickEvent = (e) => {
    emits("alertView", e.target.dataset.alertView, e.target.offsetTop + e.target.clientHeight * 1.3);
}
</script>
<template>
    <div class="study3-end">
        <div class="title">
        </div>
        <div class="container">
            <div style="margin: 0 0 40px 0">
                However, we also found that people’s understandings of certain social relationships could vary across times
                and places. People tend to hold similar views on familial and romantic relationships (e.g., ‘wife-husband’)
                but have a different understanding on public relationships (e.g., ‘leader-follower’). Cultural variations in
                relationship conceptualization are primarily driven by two cultural factors — religion and modernization. We
                found, for example, as a country’s modernization level increases, ‘neighbors’ become a more formal and
                superficial relationship. For traditional countries like Mainland China, ‘neighbors’ is considered as a
                private, personal and active relationship. But for highly modernized countries like the US, ‘neighbors’ is
                conceptualized as a more public, impersonal, and passive relationship.
            </div>
            <div class="o">
                <img src="@/assets/img/science/2.png" alt="">
            </div>
            <div class="t">
                <img src="@/assets/img/science/19.png" alt="" style="
                    width: 40%;
                    margin: 0 5% 0 0;
                ">
                <img src="@/assets/img/science/18.png" alt="">
            </div>
            <div class="txt">
                <div>Conclusion:</div>
                <div>
                    We provided empirical evidence that relationship knowledge is both universal and culturally variable:
                    the coarse-grained architecture (backbone) of relationship knowledge system is universally shared (i.e.,
                    the FAVEE-HPP framework), but fine-grained contents could be different across cultures. This cultural
                    variability is substantial but predictable: people’s understanding of social relationship concepts is a
                    combined product of traditional inheritance (e.g., religious beliefs and rituals) and contemporary
                    changes (e.g., urbanization, globalization).
                </div>
                <div class="link" style="text-align: right; color: var(--font-color-link); cursor: pointer;" @click="clickEvent" data-alert-view="study3_2">
                    Read more
                </div>
            </div>
            <div class="t">
                <img src="@/assets/img/science/33.png" alt="">
                <img src="@/assets/img/science/34.png" alt="">
            </div>
            <div class="o">
                <img src="@/assets/img/science/15.png" alt="">
            </div>
        </div>
    </div>
</template>

<style scoped>
.study3-end {
    margin: 80px 0;
}

.study3-end .txt .link::after {
    content: "";
    display: inline-block;
    width: 20px;
    height: 1px;
    background-color: var(--font-color-link);
    vertical-align: middle;
}
.study3-end .container {
    display: flex;
    height: 1000px;
    flex-wrap: wrap;
    flex-direction: column;
    justify-content: space-between;
    text-align: left;
}

.study3-end .container .txt {
    padding: 60px 70px;
    box-sizing: border-box;
    background-color: var(--morelightorange);
}

.study3-end .container .txt>div:nth-child(1) {
    margin: 0 0 20px 0;
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 2.25rem;
}

.study3-end .container>div {
    width: 550px;
}

.study3-end .container>div.o>img {
    width: 100%;
}

.study3-end .container>div.t>img {
    vertical-align: middle;
    width: 45%;
}

.study3-end .title {
    font-size: 2.4rem;
    padding: 25px 0 10px 0;
    background-image: linear-gradient(var(--orange), var(--orange));
    background-size: 25px 25px;
    background-position: 0px 0px;
    background-repeat: no-repeat;
    font-weight: 600;
    line-height: 2rem;
}

@media screen and (max-width: 1200px) {
    .study3-end {
        margin: 80px 20px;
    }
    .study3-end .container {
        height: 1024px;
    }
    .study3-end .container>div {
        width: 450px;
    }
}

@media screen and (max-width: 1000px) {
    .study3-end .container>div {
        width: 80%;
    }
    .study3-end .container {
        height: auto;
        justify-content: space-around;
        align-items: center;
    }
    .study3-end .container .t {
        display: flex;
        margin: 20px 0;
        justify-content: space-around;
    }
    .study3-end .container .txt {
        padding: 30px 30px;
    }
}
</style>