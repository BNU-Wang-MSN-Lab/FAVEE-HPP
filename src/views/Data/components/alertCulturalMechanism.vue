<template>
    <div class="alert-cul-me">
        <div class="title">
            Relationship conceptualization is both universal and culturally variable.
        </div>
        <div class="content">
            Common underlying structures such as FAVEE dimensions and HPP categories were stably and consistently observed across global regions (shown in figure a). Meanwhile, relationship words could also vary in meaning across cultures. The groupings of representational geometry across global regions identified six sets of groups (shown in figure b). Their variation was found to be tied to religion and modernization differences between regions (shown in c).
        </div>
        <div class="img" style="width: 80%;"><img :src="img1Src" alt=""></div>
    </div>
</template>
  
<script setup>
import { ref } from "vue";

const img1Src = ref("");
import("@/assets/img/data/424242.png")
    .then(r => r.default)
    .then(r => img1Src.value = r);
</script>
  
<style scoped>
.alert-cul-me .title {
    font-size: 1.5rem;
    line-height: 2.25rem;
    font-weight: 600;
}
.alert-cul-me .content {
    margin: 20px 0;
}

.alert-cul-me .img {
    margin: 0 auto;
}

.alert-cul-me .img>img {
    width: 100%;
}

@media screen and (max-width: 600) {
    .alert-cul-me .title {
        font-size: 1.5rem;
        line-height: 2.25rem;
    }
  }
</style>