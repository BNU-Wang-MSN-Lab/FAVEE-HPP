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
  <div class="container">
    <RouterView></RouterView>
    <RouterView name="Favee"></RouterView>
    <RouterView name="f3d" v-on:alertOpen="alertOpen" class="cc"></RouterView>
    <RouterView name="Study1" v-on:alertOpen="alertOpen" class="cc"></RouterView>
    <RouterView name="Study2" v-on:alertOpen="alertOpen" class="cc"></RouterView>
    <RouterView name="Study3" v-on:alertOpen="alertOpen" class="cc"></RouterView>
    <RouterView name="region" v-on:alertOpen="alertOpen" class="cc"></RouterView>
  </div>
  <fAlert :view="show.name" v-on:alertCancel="alertCancel" v-if="show.alert" />
</template>

<style scoped>
.container {
  width: 100%;
  height: 100%;
  background: #F5F6F7 repeating-linear-gradient(90deg, transparent 0px, transparent 30px, rgba(0, 0, 255, 0.04) 30px, rgba(0, 0, 255, 0.04) 300px);
  background-position: 20px 0px;
  overflow-y: scroll;
}

.cc:nth-child(odd) {
  background: #fff;
  overflow: hidden auto;
}
.cc:nth-child(even) {
  background: #F5F6F7;
  overflow: hidden auto;
}
</style>
