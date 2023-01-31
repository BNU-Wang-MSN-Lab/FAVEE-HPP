<script setup>
import fHeader from "./components/header.vue";
import fAlert from "./components/alert.vue";
import { provide, reactive, ref } from "vue";

const chooseCountry = ref(null);
provide("chooseCountry", chooseCountry);

const show = reactive({
  alert: false,
  name: ""
});

const alertOpen = function (i) {
  show.alert = true;
  show.name = i;
}
const alertCancel = () => {
  show.alert = false;
}
</script>

<template>
  <fHeader @click="show.alert = false;" />
  <div class="container">
    <RouterView></RouterView>
    <RouterView name="Favee"></RouterView>
    <RouterView name="f3d" v-on:alertOpen="alertOpen" class="cc"></RouterView>
    <RouterView name="Study1" v-on:alertOpen="alertOpen" class="cc"></RouterView>
    <RouterView name="Study2" v-on:alertOpen="alertOpen" class="cc"></RouterView>
    <RouterView name="Study3" v-on:alertOpen="alertOpen" class="cc"></RouterView>
    <RouterView name="region" v-on:alertOpen="alertOpen" class="cc"></RouterView>
  </div>
  <fAlert :hidden="!show.alert" :view="show.name" v-on:alertCancel="alertCancel" />
</template>

<style scoped>
.header a.logo {
  float: left;
  font-weight: bold;
  font-size: 39px;
  line-height: 50px;
}

.header div.nav {
  height: 50px;
}

.header ul.nav-bar {
  list-style: none;
  float: right;
  line-height: 50px;
}

.header ul.nav-bar li {
  float: left;
  padding: 0 10px;
}

.btn {
  display: none;
  float: right;
  margin-top: 5px;
  border: 0;
  border-radius: 5px;
  width: 40px;
  height: 40px;
}

.container {
  width: 100%;
  height: 100%;
  background: #F5F6F7 repeating-linear-gradient(90deg, transparent 0px, transparent 30px, rgba(0, 0, 255, 0.04) 30px, rgba(0, 0, 255, 0.04) 300px);
  background-position: 20px 0px;
  overflow-y: scroll;
}

.cc:nth-child(odd) {
  background: #fff;
  overflow: auto;
}
.cc:nth-child(even) {
  background: #F5F6F7;
  overflow: auto;
}

@media screen and (max-width: 768px) {
  .header {
    padding: 10px 5%;
    height: 50px;
    overflow: hidden;
  }

  .header a.logo {
    line-height: 55px;
    font-size: 30px;
  }

  .btn {
    display: block;
  }

  .header ul.nav-bar {
    margin-top: 15px;
    border-top: solid 1px #111;
    width: 100%;
  }

  .header ul.nav-bar li {
    float: none;
    padding: 0 10px;
  }
}
</style>
