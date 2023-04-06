<script setup>
import { inject, ref, watch } from "vue";

const prop = defineProps({
    title: String,
    content: String,
    name: String,
    choinput: {
        type: String,
        default: ""
    },
    alert: {
        type: String,
        default: "Type to search"
    },
    updateInputVal: { // 用于更新input的值
        type: String,
        default: ""
    }
});
const emits = defineEmits(["chosEvent"]);
const choData = inject(prop.choinput);
const showLabel = ref([]);
choData.word.forEach(v => showLabel.value.push(v.x));
watch(choData, (n, o) => {
    showLabel.value = [];
    n.word.forEach(v => showLabel.value.push(v.x));
});

const activate = function(e) {
    e.target.parentElement.childNodes[1].style.display = "block";
}
const deactivate = (e) => {
    const parent = e.target.parentElement;
    const li = parent.querySelector("li:hover");
    if (li) chosWord(li.innerText);
    parent.childNodes[1].style.display = "none"; // 将ul给隐藏
}

const inputVal = ref("");
if (prop.updateInputVal != "") inputVal.value = prop.updateInputVal;
watch(prop, (n, o) => {
    inputVal.value = n.updateInputVal;
});
const inputEvent = (e) => {
    const w = e.target.value.toLowerCase();
    if (!w.length) {
        showLabel.value = [];
        choData.word.forEach(v => showLabel.value.push(v.x));
        return 0;
    }
    showLabel.value = choData.word.filter(v => v.x.toLowerCase().search(w) >= 0).map(v => v.x);
}

const chosWord = (e) => {
    if (e == "") return 0;
    emits("chosEvent", e, choData.word.map(v => v.x).indexOf(e));
    inputVal.value = e;
}

const leftClickEvent = (e) => {
    if (e.target.childNodes.length && e.target.childNodes[0].tagName == "INPUT") e.target.childNodes[0].focus();
}
</script>

<template>
    <div class="banner-choose">
        <div class="right">
            <div class="title">{{ title }}</div>
            <div class="content"><slot /></div>
        </div>
        <div class="left" @click="leftClickEvent">
            <div class="name">{{ name }}</div>
            <div class="input">
                <input type="text" 
                    :placeholder="alert" 
                    @focusin="activate" 
                    @focusout="deactivate"
                    @input="inputEvent"
                    v-model="inputVal" />
                <ul>
                    <li v-for="i in showLabel">{{ i }}</li>
                </ul>
            </div>
        </div>
    </div>
</template>

<style scoped>
.banner-choose {
    display: flex;
    min-height: 333px;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    padding: 36px 65px;
    background-color: var(--blue1);
    color: var(--font-color-white);
    background-image: linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(var(--orange), var(--orange)),
        linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.4)),
        linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.4)),
        linear-gradient(var(--orange), var(--orange)),
        linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(transparent, transparent);
    background-position: 32px 0px, 0px 0px, 20px 0px, 0px 51px, 100% 0%, 100% 20%, 100% 80%;
    background-size: 30px 30px, 62px 51px, 78px 30px, 30px 30px, 24px 20%, 24px 80%, 24px 20%;
    background-repeat: no-repeat;
}

.right,
.left {
    display: block;
    max-width: 579px;
}

.title {
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 2.25rem;
}

.content {
    text-align: left;
}

.name {
    margin: 10px 0px;
    font-weight: 300;
    text-align: center;
}

.input {
    background-color: #fff;
    position: relative;
    cursor: pointer;
}
.input ul {
    display: none;
    position: absolute;
    left: calc(18%);
    width: 64%;
    box-sizing: border-box;
    margin: 10px 0 0 0;
    padding: 10px;
    max-height: 150px;
    overflow-y: scroll;
    background-color: var(--bg2);
    border: 1 solid var(--lightorange);
    border-radius: 10px;
    box-shadow: var(--grey) 0px 5px 10px;
    z-index: 1;
}
.input ul li {
    color: var(--grey);
}

.input ul li:hover {
    color: var(--blue1);
}

input {
    width: 454px;
    height: 64px;
    padding: 20px;
    border: none;
    box-sizing: border-box;
    background-color: #fff;
}

.input::after {
    content: "";
    display: block;
    width: 0px;
    height: 0px;
    background-color: transparent;
    position: absolute;
    bottom: calc(100% / 2 - 16px - 8px);
    right: 16px;
    box-sizing: border-box;
    border: 16px solid transparent;
    border-top: 16px solid rgba(0, 0, 0, 0.2);
}

@media screen and (max-width: 1200px) {
    .banner-choose {
        flex-direction: column;
    }

    .banner-choose .left {
        margin: 50px 0 0 0;
    }
}

@media screen and (max-width: 725px) {
    .banner-choose {
        min-height: 0px;
    }

    input {
        width: 200px;
        height: 32px;
        padding: 10px;
    }

    input::after {
        bottom: 6px;
        right: 16px;
    }

    .banner-choose {
        background-size: 15px 15px, 32px 30px, 50px 15px, 15px 15px, 12px 20%, 12px 80%, 12px 20%;
        background-position: 17px 15px, 0px 0px, 0px 0px, 0px 30px, 100% 0%, 100% 20%, 100% 80%;
    }
}
</style>
