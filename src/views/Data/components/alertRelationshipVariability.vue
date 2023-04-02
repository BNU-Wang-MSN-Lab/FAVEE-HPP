<template>
    <div class="alert-relation-vari">
        <div class="title">
            Cultural consensus is higher when it comes to private relationships, but there are significant cultural differences when it comes to public relationships.
        </div>
        <div class="content">
            Figure a shows the trend that affiliative and power relationships (left word cloud box) varied more across regions, while familial and romantic relationships (right word cloud box) varied less. The font size of word clouds proportionally reflects the familiarity of the relationships.
        </div>
        <div class="img" style="width: 80%;"><img :src="img2Src" alt=""></div>
        <div class="content">
            Figure b shows that, for three HPP categories, public relationship concepts had more culturally variable meanings than hostile and private relationship concepts.
        </div>
        <div class="img" style="width: 40%;"><img :src="img1Src" alt=""></div>
    </div>
</template>
  
<script setup>
import { ref } from "vue";

const img1Src = ref("");
const img2Src = ref("");
import("@/assets/img/data/1411211441411.png")
    .then(r => r.default)
    .then(r => img1Src.value = r);
import("@/assets/img/data/14142424241411.png")
    .then(r => r.default)
    .then(r => img2Src.value = r);
</script>
  
<style scoped>
.alert-relation-vari .title {
    font-size: 1.5rem;
    line-height: 2.25rem;
    font-weight: 600;
}
.alert-relation-vari .content {
    margin: 20px 0;
}

.alert-relation-vari .img {
    margin: 0 auto;
}

.alert-relation-vari .img>img {
    width: 100%;
}
</style>