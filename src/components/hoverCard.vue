<script setup>
import { ref, computed } from "vue";

const prop = defineProps({
  msg: String,
  img: String,
  index: Number,
});
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
    :style="`background: url(${img}) center/cover no-repeat`"
  >
    <div class="hover-bottom">
      <div class="answer">
        <p class="answer-text">
          {{ msg }}
        </p>
      </div>
      <div class="see">
        <img class="see-icon" src="@/assets/img/home/see.png" alt="" />
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
  font-size: 12px;
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
    width: 100%;
    margin-right: 0px;
    margin-bottom: 20px;
    padding: 20px;
    height: 160px;
    transition: all 0.2s;
    transform-origin: center center;
  }
  .hover-card:hover {
    z-index: 1000;
    transform: scale(1.2, 1.2);
    border: 4px solid #fff;
  }
  .answer-text {
    font-size: 16px;
  }
  .hover-bottom {
    height: 40px;
  }

  .see {
    width: 60px;
  }

  .see-icon {
    width: 40px;
    height: 26px;
  }
}
@media (min-width:600px) and (max-width: 900px) {
  .hover-card {
    position: relative;
    box-sizing: border-box;
    width: 70%;
    margin-right: 0px;
    margin-bottom: 20px;
    padding: 20px;
    height: 220px;
    transition: all 0.2s;
    transform-origin: center center;
  }
  .hover-card:hover {
    z-index: 1000;
    transform: scale(1.2, 1.2);
    border: 4px solid #fff;
  }
  .hover-bottom {
    height: 60px;
    font-size: 30px;
  }
  .answer-text {
    font-size: 30px;
  }

  .see {
    width: 80px;
  }

  .see-icon {
    width: 40px;
    height: 26px;
  }
}
</style>
