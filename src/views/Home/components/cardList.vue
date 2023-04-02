
<template>
  <div class="main card-list">
    <hover-card
      v-for="(item, index) in list"
      :key="item"
      :msg="item"
      :img="`src/assets/img/home/card/card_img${index+1}.png`"
      :index="index"
    >
    </hover-card>
  </div>
</template>
<script setup>
import hoverCard from "@/components/hoverCard.vue";
const list = [
  "Close friends",
  "Wife-Husband",
  "Teammates in sports",
  "Parent-Child",
  "Romantic rivals",
  "Brothers-in-arms",
  "Political opponents",
  "Criminal-Police officer",
  "Coworkers",
  "Customer-Businessman",
  "Romantic Lovers",
  "Enemies",
  "Business Partners",
  "Officer and Soldier",
  "Man and His Mistress",
  "Siblings",
  "Leader-Follower",
  "Monarch-Minister",
  "Criminal-Hostage",
  "Guest and Host",
  "Landlord and Housekeeper",
]
</script>
<style lang="scss" scoped>
.card-list {
  width: 100%;
    display: flex;
    flex-wrap: wrap;
}
</style>