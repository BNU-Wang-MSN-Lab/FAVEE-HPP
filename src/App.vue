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
  <fHeader/>
  <div class="container">
    <RouterView class="cc"></RouterView>
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

.cc:nth-child(odd) {
  background: #fff;
  overflow: hidden auto;
}
.cc:nth-child(even) {
  background: #F5F6F7;
  overflow: hidden auto;
}
</style>
