<template>
    <div class="w">{{ country }}</div>
    <component :is="alertViews[currPage]"></component>
</template>

<script setup>
import { inject, defineAsyncComponent } from 'vue';

const alertRegioCategorical = defineAsyncComponent(() => import("./alertRegioCategorical.vue"));
const alertRegioDimensional = defineAsyncComponent(() => import("./alertRegioDimensional.vue"));
const alertRegioDemographics = defineAsyncComponent(() => import("./alertRegioDemographics.vue"));
const alertViews = [alertRegioDimensional, alertRegioCategorical, alertRegioDemographics];
const props = defineProps({
    country: String
});
const currPage = inject("currPage");
</script>

<style scoped>
.w {
    font-size: 1.5rem; 
    font-weight: 600; 
    line-height: 2.25rem;
}
</style>