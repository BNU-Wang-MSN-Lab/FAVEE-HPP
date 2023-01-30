<script setup>
import { reactive } from 'vue';

const data = reactive({
    header: [
        { path: "/", name: "Introduction" },
        { path: "#study1", name: "Studys" }
    ]
});

const btnClick = function (e) {
    document.querySelector("div#header").style.height =
        (
            document.querySelector("div#header").style.height == "50px" ||
            document.querySelector("div#header").style.height == ""
        ) ?
            `${50 + 50 * data.header.length}px` : "50px";
}
</script>

<template>
    <div id="header">
        <div class="nav">
            <span><a href="#" class="logo">FAVEE-HPP</a></span>
        </div>
        <div class="btn" @click.stop="btnClick">
            <svg t="1672901242617" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2687"
                xmlns:xlink="http://www.w3.org/1999/xlink" width="40" height="40">
                <path
                    d="M892.928 128q28.672 0 48.64 19.968t19.968 48.64l0 52.224q0 28.672-19.968 48.64t-48.64 19.968l-759.808 0q-28.672 0-48.64-19.968t-19.968-48.64l0-52.224q0-28.672 19.968-48.64t48.64-19.968l759.808 0zM892.928 448.512q28.672 0 48.64 19.968t19.968 48.64l0 52.224q0 28.672-19.968 48.64t-48.64 19.968l-759.808 0q-28.672 0-48.64-19.968t-19.968-48.64l0-52.224q0-28.672 19.968-48.64t48.64-19.968l759.808 0zM892.928 769.024q28.672 0 48.64 19.968t19.968 48.64l0 52.224q0 28.672-19.968 48.64t-48.64 19.968l-759.808 0q-28.672 0-48.64-19.968t-19.968-48.64l0-52.224q0-28.672 19.968-48.64t48.64-19.968l759.808 0z"
                    p-id="2688">
                </path>
            </svg>
        </div>
        <ul>
            <li v-for="i in data.header">
                <router-link :to="i.path">{{ i.name }}</router-link>
                <span v-if="i.path != '/'">
                    <svg width="18" height="15" viewBox="0 0 18 5" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M5 1.5L10 6.5L15 1.5" stroke="#7A7671" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                    </svg>
                </span>
            </li>
        </ul>
    </div>
</template>

<style scoped>
#header {
    position: absolute;
    top: 0;
    left: 0;
    background-color: rgba(255, 255, 255, 0.6);
    width: 100%;
    height: 65px;
    color: black;
    text-align: left;
    user-select: none;
    overflow: hidden;
    border-block-end: 1px solid rgba(0, 0, 0, 0.1);
    box-sizing: border-box;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    z-index: 1;
}

.logo {
    font-size: 40px;
    line-height: 65px;
    margin: 0 0 0 50px;
}

a {
    text-decoration: none;
    color: grey;
    font-size: 16px;
}

a:hover {
    color: grey;
}

.nav {
    display: inline-block;
    height: 65px;
}

ul {
    list-style: none;
    float: right;
    line-height: 65px;
    margin: 0 65px;
}

li {
    float: left;
    padding: 0 30px;
}

li span {
    width: 32px;
    height: 32px;
}

.btn {
    display: none;
    float: right;
    margin-top: 5px;
    border: 0;
    border-radius: 5px;
    width: 40px;
    height: 40px;
    cursor: pointer;
}

.btn svg {
    fill: white;
}

@media screen and (max-width: 768px) {
    #header {
        padding: 10px 5%;
        height: 50px;
        overflow: hidden;
    }

    .logo {
        line-height: 55px;
        font-size: 30px;
    }

    .btn {
        display: block;
    }

    ul {
        margin: 0;
        margin-top: 15px;
        border-top: solid 1px #111;
        width: 100%;
    }

    li {
        float: none;
        padding: 0 10px;
    }
}
</style>