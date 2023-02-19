<script setup>
import fHeader from "./components/header.vue";
import fAlert from "./components/alert.vue";
import $ from "jquery";
import { provide, reactive, ref } from "vue";
import { useRouter } from "vue-router";

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
  <fHeader />
  <div class="container">
    <RouterView class="cc"></RouterView>
    <RouterView name="Home1" class="cc"></RouterView>
    <RouterView name="Home4" class="cc"></RouterView>
    <RouterView name="Home2" class="cc"></RouterView>
    <RouterView name="Home3" class="cc"></RouterView>
    <RouterView name="Page1" class="cc"></RouterView>
    <RouterView name="Page2" class="cc" v-on:alertOpen="alertOpen"></RouterView>
    <RouterView name="Page3" class="cc" v-on:alertOpen="alertOpen"></RouterView>
    <RouterView name="Page4" class="cc" v-on:alertOpen="alertOpen"></RouterView>
    <RouterView name="Page7" class="cc" v-on:alertOpen="alertOpen"></RouterView>
    <RouterView name="Page5" class="cc" v-on:alertOpen="alertOpen"></RouterView>
    <RouterView name="Page6" class="cc" v-on:alertOpen="alertOpen"></RouterView>
  </div>
  <fAlert :view="show.name" v-on:alertCancel="alertCancel" v-if="show.alert" />
</template>

<style scoped>
.container {
  width: 100vw;
  background: #F5F6F7;
  background-position: 20px 0px;
  overflow-x: hidden;
}

.box {
  display: grid;
  width: 100vw;
  min-height: 100vh;
  grid-template-columns: 25px repeat(8, 1fr) 25px;
  grid-gap: 20px;
  align-items: center;
  justify-content: center;
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
