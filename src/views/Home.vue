<script setup>
import { reactive } from 'vue';

const data = reactive({
    href: [
        { name: "GitHub", url: "https://github.com/BNU-Wang-MSN-Lab/FAVEE-HPP" },
        { name: "WangLab Website", url: "http://mirrorneuronwang.com/" },
        { name: "Contacts", url: "#" }
    ]
});

const hrefClick = (e) => {
    const url = e.target.dataset.href;
    let a = document.createElement("a");
    a.href = url;
    a.target = "_blank"
    a.click();
}
</script>

<template>
    <div class="box">
        <div class="bg"></div>
        <div class="content">
            <div class="title">
                Lorem ipsum
            </div>
            <div>
                <p>
                    For our survive and thrive, we build connections with a variety of people in the family, school, workplace, neighborhood, organizations, and online communities. How do we make sense of such complex systems of social relationships?
                </p>
                <p>
                    Here, by using natural language processing, online survey, lab behavioral experiment, and computational modelling on diverse populations across the world (total n= 19,532), and unifying theories across disciplines, we uncovered relationship concepts can be reliably represented either as continuous dimensions (‘FAVEE’ model) or discrete categories (‘HPP’ model), as well as being compatibly integrated in the same framework (FAVEE-HPP model).
                </p>
                <p>
                    There is also rich cultural variation in relationship conceptualization, with religion and modernization jointly shaping the culturally specific conceptual beliefs about relationships.
                </p>
            </div>
            <div>
                <div v-for="i in data.href" class="button" :data-href="i.url" @click="hrefClick">{{ i.name }}</div>
            </div>
        </div>
    </div>
</template>

<style scoped>
div.box {
    display: block;
    width: 100%;
    height: 100%;
    background: #fff repeating-linear-gradient(90deg, transparent 0px, transparent 30px, rgba(0,0,255, 0.04) 30px, rgba(0,0,255, 0.04) 300px);
    background-position: 20px 0px;
    position: relative;
}
.bg {
    width: 40%;
    height: 100%;
    background: url("/assets/拼图@2x.png") no-repeat;
    background-size: cover;
    background-position: center;
    position: absolute;
    right: 0;
}
.bg::after {
    content: '';
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, white, transparent);
    position: absolute;
    right: 0;
}

.content {
    width: 60%;
    position: absolute;
    left: 0;
    top: calc(50% - 190px);
    text-align: left;
    margin: 0 0 0 68px;
}
.title {
    color: var(--theme-color-blue);
    font-size: 64px;
    line-height: 76px;
}

.button {
    display: inline-block;
    margin: 0 40px 0 0;
    padding: 8px 10px;
    border: 1px solid var(--theme-color-blue);
    border-radius: 5px;
    color: var(--theme-color-blue);
    cursor: pointer;
}
</style>
