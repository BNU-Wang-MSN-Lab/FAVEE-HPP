<template>
  <div>
    <div class="title-row">
      <div class="title-tip" :style="`background-color:${tipColor}`"></div>
      <h2 class="title">
        {{ title }}
      </h2>
      <div v-if="tipVisible" class="tip-box" :class="type == 2 ? 'tip2' : ''">
        <tip :type="type"></tip>
      </div>
    </div>
  </div>
</template>
<script setup>
import tip from "./tip.vue";
const prop = defineProps({
  tipColor: {
    default: "rgba(255, 211, 175, 1)",
  },
  title: {
    default: "titl"
  },
  type: {

  },
  tipVisible: {
    type: Boolean,
    default: true
  }
});
</script>
<style lang="scss" scoped>
.title-row {
  position: relative;
  display: flex;
  justify-content: space-between;

  .title {
    font-size: 48px;
    font-weight: bold;
    color: rgba(35, 37, 54, 1);
  }

  .title-tip {
    position: absolute;
    left: 0;
    top: -8px;
    transform: translateY(-101%);
    width: 25px;
    height: 25px;
  }

  .tip2 {
    transform: translateY(-50%);
  }
}

@media screen and (max-width: 600px) {
  .title-row {

    .title {
      font-size: 1.5rem;
    }

    .title-tip {
      width: 20px;
      height: 20px;
    }

  }
}

@media (min-width: 600px) and (max-width: 900px) {
  .title-row {
    .title {
      font-size: 28px;
    }

    .title-tip {
      width: 26px;
      height: 26px;
    }
  }
}

@media (min-width: 900px) and (max-width: 1200px) {
  .title-row {
    .title {
      font-size: 38px;
    }

    .title-tip {
      width: 30px;
      height: 30px;
    }
  }
}
</style>