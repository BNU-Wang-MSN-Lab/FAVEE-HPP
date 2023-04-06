<template>
  <div class="alert-more-detail">
    <div>
      The dimensional and categorical models derived from global data in Study 3 (n=17,686). FAVEE model (figure b) and
      HPP model (figure c) derived from large-scale global data replicated the results in Study 1 and Study 2. Four
      data-driven metrics consistently indicated the optimal number for PCA was five (figure a).
    </div>
    <div class="img-container">
      <div class="img"><img :src="imgSrc" alt=""></div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const imgSrc = ref("");
import("@/assets/img/data/1111111.png")
  .then(r => r.default)
  .then(r => imgSrc.value = r);
</script>

<style scoped>
.alert-more-detail .img-container {
  display: flex;
  flex-wrap: wrap-reverse;
  flex-direction: column-reverse;
  margin: 50px 0 0 0;
}
.alert-more-detail .img {
  width: 80%;
  margin: 0 auto;
}
.alert-more-detail .img>img {
  width: 100%;
}
</style>