<template>
  <div class="alert-subset-analysis">
    <div class="content">
      Figure a shows high correlation (Pearson’s r > 0.9) between PCA loading scores derived from the full set versus
      subsets of relationships (n=40). These relationships were shown in figure b (font size corresponds to relationship
      familiarity). As shown in figure c, the RDM across global regions of the subsets is relatively similar to that of
      the full set. The subsets were good enough to capture the cross-cultural variability of relationship representations
      and replicate the cultural mechanism, which is shown in figure d.
    </div>
    <div class="img-container">
      <div class="img"><img :src="imgSrc" alt=""></div>
    </div>
    <div class="fig">
      A subset of 40 relationships was good enough to replicate all findings based on 159 relationships. This subset can
      be used more efficiently for you when collecting data for a larger set of relationships is not feasible and you
      can download the data here.
    </div>
    <div style="display: flex; justify-content: center; margin: 20px 0;">
      <choButton @click="hrefClick(dataSrc)" style="margin: 0 auto;">Download subset</choButton>
    </div>
  </div>
</template>
  
<script setup>
import { ref } from "vue";

import choButton from "../../../components/choButton.vue";

const imgSrc = ref("");
import("@/assets/img/data/45454541.png")
  .then(r => r.default)
  .then(r => imgSrc.value = r);

let dataSrc = "./assets/data/subset.xlsx";
// download
const hrefClick = (e) => {
  let a = document.createElement("a");
  a.href = e;
  a.target = "_blank"
  a.click();
}
</script>
  
<style scoped>
.alert-subset-analysis .img-container {
  display: flex;
  flex-wrap: wrap-reverse;
  flex-direction: column-reverse;
  margin: 50px 0 0 0;
}

.alert-subset-analysis .img {
  width: 80%;
  margin: 0 auto;
}

.alert-subset-analysis .img>img {
  width: 100%;
}

@media screen and (max-width: 600) {
  .alert-subset-analysis .content {
    font-size: 1.5rem;
    line-height: 2.25rem;
  }
}</style>
