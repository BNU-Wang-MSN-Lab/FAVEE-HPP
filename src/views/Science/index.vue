<script setup>
import { defineAsyncComponent, ref } from 'vue';
import study1 from './components/study1.vue';
import study2 from './components/study2.vue';
import study3 from './components/study3.vue';
import study2Middle from './components/study2Middle.vue';
import study2End from './components/study2End.vue';
import study3End from './components/study3End.vue';

const alertView = defineAsyncComponent(() => import("../../components/alertView.vue"));

const study1AlertView1 = defineAsyncComponent(() => import("./alert/study1AlertView1.vue"));
const study1AlertView2 = defineAsyncComponent(() => import("./alert/study1AlertView2.vue"));
const study2AlertView1 = defineAsyncComponent(() => import("./alert/study2AlertView1.vue"));
const study3AlertView1 = defineAsyncComponent(() => import("./alert/study3AlertView1.vue"));
const study3AlertView2 = defineAsyncComponent(() => import("./alert/study3AlertView2.vue"));
const comp = {
    "study1_1": study1AlertView1,
    "study1_2": study1AlertView2,
    "study2_1": study2AlertView1,
    "study3_1": study3AlertView1,
    "study3_2": study3AlertView2
}
const alertPageSelected = ref("");
// 弹窗的显示, 点啥弹啥
const alertViewVisible = ref(false);
const alertViewTopPos = ref(0);
const showAlertView = (e, p) => {
    alertViewVisible.value = true;
    alertViewTopPos.value = p;
    alertPageSelected.value = e;
};
</script>

<template>
    <div class="box">
        <study1 @alertView="showAlertView"></study1>
        <study2></study2>
        <study2-middle></study2-middle>
        <study2-end @alertView="showAlertView"></study2-end>
        <study3 @alertView="showAlertView"></study3>
        <study3-end @alertView="showAlertView"></study3-end>
        <alert-view v-if="alertViewVisible" @alertViewClose="alertViewVisible = false" :topPos="alertViewTopPos">
            <component :is="comp[alertPageSelected]"></component>
        </alert-view>
    </div>
</template>

<style scoped>
.box {
    width: 100%;
    max-width: 1200px;
    margin: 50px auto 0 auto;
    overflow: hidden;
}
</style>