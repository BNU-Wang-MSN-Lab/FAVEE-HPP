<script setup>
import { ref, computed } from "vue";

const prop = defineProps({
  msg: String,
  img: Number,
  index: Number,
});
const ii = prop.img + 1;
const imgSrc = ref("");
import(`../assets/img/home/card/card_img${ii}.png`)
  .then(r => r.default)
  .then(r => imgSrc.value = r);

let sumOrigin = computed(() => {
  if (prop.index == 0) return "right-bottom";
  if (prop.index > 0 && prop.index < 6) return "center-bottom";
  if (prop.index == 6) return "left-bottom";
  if (prop.index == 13) return "left-center";
  if (prop.index == 7) return "right-center";
  if (prop.index == 14) return "right-top";
  if (prop.index > 14 && prop.index < 20) return "center-top";
  if (prop.index == 20) return "left-top";
});
</script>

<template>
  <div
    class="hover-card"
    :class="sumOrigin"
    :style="`background: url(${imgSrc}) center/cover no-repeat`"
  >
    <div class="hover-bottom">
      <div class="answer">
        <p class="answer-text">
          {{ msg }}
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hover-card {
  position: relative;
  box-sizing: border-box;
  width: 12.7%;
  margin-right: 1.5%;
  margin-bottom: 20px;
  padding: 20px;
  height: 90px;
  transition: all 0.2s;
}

.hover-card:hover {
  z-index: 1000;
  transform: scale(2, 2);
  border: 4px solid #fff;
}

.right-bottom {
  transform-origin: left top;
}

.center-bottom {
  transform-origin: center top;
}

.left-bottom {
  transform-origin: right top;
}

.right-center {
  transform-origin: left center;
}

.left-center {
  transform-origin: right center;
}

.right-top {
  transform-origin: left bottom;
}

.center-top {
  transform-origin: center bottom;
}

.left-top {
  transform-origin: right bottom;
}

.hover-card:hover .hover-bottom {
  display: flex;
}

.hover-bottom {
  display: none;
  /* display: flex; */
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 20px;
  justify-content: space-between;
  align-items: center;
  color: #fff;
  background-color: rgba(0, 0, 0, 0.5);
}

.answer {
  flex: 1;
  color: rgba(84, 38, 0, 1);
  background-color: rgba(255, 161, 85, 1);
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.answer-text {
  position: absolute;
  font-size: 0.75rem;
  transform: scale(.5,.5);
  white-space: nowrap;
  transform-origin: center center;
}

.see {
  width: 40px;
  height: 100%;
  background-color: var(--theme-color-blue);
  display: flex;
  justify-content: center;
  align-items: center;
}

.see-icon {
  transform: scale(0.5, 0.5);
  width: 26px;
  height: 18px;
}

.read-the-docs {
  color: #888;
}

@media screen and (max-width: 600px) {
  .hover-card {
    position: relative;
    box-sizing: border-box;
    width: 31%;
    margin-right: 2%;
    margin-bottom: 20px;
    padding: 20px;
    height: 70px;
    transition: all 0.2s;
    transform-origin: center center;
  }
  .hover-card:hover {
    z-index: 1000;
    transform: scale(1.2, 1.2);
    border: 4px solid #fff;
  }
  .answer-text {
    font-size: 0.75rem;
  }
  .hover-bottom {
    height: 20px;
  }

  .see {
    width: 20px;
  }

  .see-icon {
    width: 16px;
    height: 10px;
  }
}
@media (min-width:600px) and (max-width: 900px) {
  .hover-card {
    position: relative;
    box-sizing: border-box;
    width: 30%;
    margin-right: 3%;
    margin-bottom: 20px;
    padding: 20px;
    height: 120px;
    transition: all 0.2s;
    transform-origin: center center;
  }
  .hover-card:hover {
    z-index: 1000;
    transform: scale(1.2, 1.2);
    border: 4px solid #fff;
  }
  .hover-bottom {
    height: 30px;
    font-size: 1rem;
  }
  .answer-text {
    font-size: 1.2rem;
  }

  .see {
    width: 30px;
  }

  .see-icon {
    width: 26px;
    height: 16px;
  }
}
</style>
