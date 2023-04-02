<script setup>
import { ref } from 'vue';

const emits = defineEmits(["choooseOpt"]);
const props = defineProps({
    buttonLabels: {
        type: String,
        default: "buttonA-buttonB"
    }
});
const buttonChos = props.buttonLabels.split("-");

const selOpt = ref("");
if(buttonChos.length) selOpt.value = buttonChos[0];
const selButtonEvent = (e) => {
    selOpt.value = e.target.innerText;
    emits("choooseOpt", e.target.innerText);
};
</script>

<template>
    <div class="sel-button">
        <div v-for="i in buttonChos" @click="selButtonEvent" :class="{ selected: i == selOpt }">{{ i }}</div>
    </div>
</template>

<style scoped>
.sel-button {
    display: flex;
    margin: 0 0 50px 0;
    justify-content: center;
    color: var(--blue1);
    position: relative;
    cursor: pointer;
}

.sel-button>div {
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-sizing: border-box;
    padding: 30px 50px;
    border: 1px solid var(--grey);
}

.sel-button>div:nth-child(1) {
    background-image: linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(var(--orange), var(--orange)),
        linear-gradient(var(--lightblue), var(--lightblue)),
        linear-gradient(var(--lightblue), var(--lightblue));
    background-position: 7px 0px, 0px 0px, 0px 20px, 0px 0px;
    background-size: 11px 11px, 18px 20px, 8px 8px, 28px 11px;
    background-repeat: no-repeat;
}
.sel-button>div:last-child {
    background-image: linear-gradient(var(--lightorange), var(--lightorange)),
        linear-gradient(var(--orange), var(--orange)),
        linear-gradient(var(--lightblue), var(--lightblue)),
        linear-gradient(var(--lightblue), var(--lightblue));
    background-position: calc(100% - 7px) 100%, 100% 100%, 100% calc(100% - 20px), 100% 100%;
    background-size: 11px 11px, 18px 20px, 8px 8px, 28px 11px;
    background-repeat: no-repeat;
}
.sel-button>div.selected {
    background-color: var(--font-color-link);
    color: var(--font-color-white);
    border: none;
    padding: 31px 51px;
}

.sel-button>div::after {
    content: "";
    display: inline-block;
    margin: 0 0 0 20px;
    width: 20px;
    height: 0px;
    border: 1px solid var(--blue1);
    vertical-align: middle;
}

.sel-button>div.selected::after {
    border: 1px solid var(--font-color-white);
}

@media screen and (max-width: 1000px) {
    .sel-button {
        flex-direction: column;
    }
    .sel-button>div {
        padding: 15px 25px;
    }
    .sel-button>div.selected {
        padding: 16px 26px;
    }
}

.sel-button>div.selected::after {
    border: 1px solid var(--font-color-white);
}</style>
