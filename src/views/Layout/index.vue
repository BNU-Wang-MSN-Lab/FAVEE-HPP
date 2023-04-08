<template>
  <div class="layout-container">
    <!-- header -->
    <header class="header" style="width: 100%; position: fixed; z-index: 200;">
      <div class="main">
        <router-link to="/" class="logo"> Mapping Relationships </router-link>
        <nav class="nav">
          <li
            class="nav-item"
            v-for="(item, index) in menuList"
            :key="index"
            @click="onGo(item.path)"
            :class="route.path == item.path ? 'nav-active' : ''"
          >
            {{ item.title }}
          </li>
        </nav>
        <div class="h-menu">
          <img src="@/assets/img/home/mobile_menu.png" @click="mobileMenuState=!mobileMenuState" class="mobile_menu" alt="" />
          <div class="h-menu-list" v-show="mobileMenuState">
            <li
              class="h-menu-item"
              v-for="(item, index) in menuList"
              :key="index"
              @click="onGo(item.path)"
              :class="route.path == item.path ? 'h-menu-active' : ''"
            >
              {{ item.title }}
            </li>
          </div>
        </div>
      </div>
    </header>
    <div class="header"></div>
    <!-- banner -->
    <div class="banner" v-if="route.path == '/layout/home'">
      <div class="mainbox">
        <h2 class="main-title">Human Relationships</h2>
        <p class="main-content" v-for="(item, index) in mainList" :key="index" v-html="item">
        </p>
      </div>
      <div class="main-bottom">
        <cho-button @click="hrefClick('https://github.com/BNU-Wang-MSN-Lab/FAVEE-HPP')">GitHub</cho-button>
        <cho-button @click="hrefClick('http://mirrorneuronwang.com/')">WangLab WebSite</cho-button>
        <div class="img-box">
          <img
            src="../../assets/img/home/Beijing_Normal_University_logo.svg.png"
            style="background-color: #fff; border-radius: 50%"
            alt=""
          />
          <img src="../../assets/img/home/temple-logo-t-box.svg" alt="" />
        </div>
      </div>
    </div>
    <!-- datarow -->
    <div class="data-row" v-if="route.path == '/layout/home'">
      <div v-for="i in icon">
        <div
          class="bg"
          :style="
            'background: url(' +
            i.iconUrl +
            ') center ' +
            (i.num == 3 ? '8px' : 'center') +
            ' / 64% 64% no-repeat;'
          "
        ></div>
        <div class="num">{{ i.num }}</div>
        <div class="tit">{{ i.tit }}</div>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import choButton from "../../components/choButton.vue";
const router = useRouter();
const route = useRoute();
const mobileMenuState = ref(false);

const hrefClick = (e) => {
  let a = document.createElement("a");
  a.href = e;
  a.target = "_blank"
  a.click();
}

const icon = ref([
  { iconUrl: "./assets/icon/target.png", num: 3, tit: "Studies" },
  { iconUrl: "./assets/icon/meeting.png", num: "19,532", tit: "Participants" },
  { iconUrl: "./assets/icon/team.png", num: 19, tit: "Regions" },
  { iconUrl: "./assets/icon/language-learning.png", num: 10, tit: "Languages" },
]);
const menuList = [
  { title: "Introduction", path: "/layout/home" },
  { title: "Science behind it", path: "/layout/science" },
  { title: "Maps and Data", path: "/layout/data" },
];
const mainList = [
  "A defining characteristic of " + (document.body.clientWidth < 600 ? "<span style='font-size: 1.6rem; line-height: 2rem; font-style: italic;'>Homo sapiens</span>" : "<span style='font-style: italic;'>Homo sapiens</span>") + " is the richness and complexity of our social relationships. Social relationships provide us with a sense of connection, purpose, support and, ultimately, overall better health and longevity. How does the human mind organize and operate such complex system of social relationships?",
  `In the last 50 years, both social and biological scientists have sought to understand the nature of social relationships. Different theoretical models and taxonomies have been developed by psychologists, sociologists, anthropologists, linguists, economists, biologists, and communication researchers, but little consensus has been reached.`,
  `To address this long-standing question, we collected large-scale behavioral data across diverse populations in the world (n = 19,532). Our project aimed to examine universality and cultural variability in the ways that people understand social relationships and elucidated the cognitive structures and cultural principles underlying social relationship knowledge. 
  In support of open science, all data in the project are available to download (see Maps and Data Section). `,
];
const onGo = (path) => {
  router.push(path);
  mobileMenuState.value = false;
};
</script>
<style lang="scss" scoped>
.h-menu {
  display: none;
}
// header部分
.header {
  background-color: rgba(35, 37, 54, 1);
  height: 80px;
  padding: 0 30px;
  display: flex;
  align-items: center;
  min-height: 60px;

  .main {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 100%;

    .logo {
      font-size: 26px;
      color: #fff;
      font-weight: bold;
    }

    .nav {
      display: flex;
      align-items: center;
      color: #fff;
      height: 100%;
    }

    .nav-item {
      cursor: pointer;
      position: relative;
      padding: 0 20px;
      opacity: 0.6;
      font-size: 20px;
      height: 100%;
      display: flex;
      align-items: center;
    }

    .nav-item:hover,
    .nav-active {
      opacity: 1;
    }

    .nav-active::after {
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      bottom: 14px;
      content: "";
      display: block;
      width: 50px;
      height: 3px;
      background: rgba(68, 76, 252, 1);
    }
  }
}

// banner
.banner {
  padding-bottom: 210px;
  background-color: rgb(56, 56, 56, 1);
  background-image: linear-gradient(rgb(56, 56, 56, 0.7), rgb(56, 56, 56, 0.7)),
    url(@/assets/img/home/home.png);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: 50% 0px;

  .mainbox {
    // min-width: 624px;
    width: 624px;
    margin: 0 auto;
  }
  .img-box {
    display: flex;
    align-items: center;
    img {
      margin-right: 20px;
    }
  }
  .main-title {
    padding-top: 67px;
    padding-bottom: 22px;
    font-size: 56px;
    font-weight: 600;
    line-height: 80px;
    color: var(--orange);
  }

  .main-content {
    color: #fff;
    letter-spacing: 0px;
    line-height: 26px;
    text-align: justify;
    margin-bottom: 20px;
    font-size: 16px;
  }
  .main-bottom {
    display: flex;
    justify-content: space-between;
        align-items: center;
    width: 624px;
    margin: 0 auto;
    img {
      height: 64px;
    }
  }
}

// datarow
.data-row {
  display: flex;
  justify-content: space-around;
  align-items: center;
  position: relative;
  background-color: #fff;
  margin: 0 auto;
  transform: translateY(-50%);
  width: 90%;
  max-width: 1200px;
  height: 227px;
  z-index: 100;
  border-radius: 10px;
  box-shadow: 50px 50px 100px 0px rgba(0, 0, 0, 0.15);
  .bg {
    width: 96px;
    height: 96px;
    margin: 0 auto;
    background-position: center;
    border-radius: 50%;
    border: 3px solid var(--blue);
  }
  .num {
    font-size: 20px;
    line-height: 26px;
    font-weight: 500;
    text-align: center;
  }
  .tit {
    font-size: 16px;
    line-height: 26px;
    font-weight: 500;
    text-align: center;
  }
}
@media screen and (max-width: 600px) {
  .header {
    .main {
      .h-menu{
        display: flex;
        flex-direction: column;
        position: relative;
        justify-content: center;
        align-items: center;
        margin-right: 20px;
        .mobile_menu {
          width: 30px;
          height: 30px;
        }
        .h-menu-list {
          position: absolute;
          width: 120px;
          bottom: 0;
          transform: translateY(100%);
          background-color: rgb(35, 37, 54);
          color: #fff;
          padding: 10px 0;
          .h-menu-item {
            position: relative;
            padding: 12px 8px;
            text-align: center;
          }
          .h-menu-active::before {
            content: "";
            display: block;
            width: 50%;
            height: 2px;
            position: absolute;
            bottom: 3px;
            left: 50%;
            background: rgba(68, 76, 252, 1);
            transform: translateX(-50%);
          }
        }
      }
      .nav {
        display: none;
      }
      .logo {
        font-size: 1.8rem;
      }
      .nav-item {
        font-size: 1rem;
      }
    }
  }
  .banner {
    padding-bottom: 100px;
    .mainbox {
      width: 90%;
      .main-title {
        padding-top: 20px;
        padding-bottom: 14px;
        font-size: 3.5rem;
        line-height: 4.5rem;
      }
      .main-content {
        line-height: 2rem;
        font-size: 1.6rem;
        margin-bottom: 10px;
      }
    }
    .main-bottom {
      width: 90%;
      margin: 0 auto;
      flex-direction: column;
      align-items: center;
      .cho-button {
        width: 100%;
        margin-bottom: 14px;
      }
      img {
        margin-bottom: 14px;
        width: 64px;
        height: 64px;
      }
    }
  }
  .data-row {
    width: 90%;
    margin: 0 auto;
    height: 160px;
    .bg {
      width: 58px;
      height: 58px;
    }
    .num {
      font-size: 10px;
      line-height: 13px;
      font-weight: 500;
      text-align: center;
    }
    .tit {
      font-size: 8px;
      line-height: 13px;
      font-weight: 500;
      text-align: center;
    }
  }
}
@media (min-width: 600px) and (max-width: 900px) {
  .header {
    .main {
      .logo {
        font-size: 18px;
      }
      .nav-item {
        font-size: 14px;
      }
    }
  }
  .banner {
    padding-bottom: 180px;
    .mainbox {
      width: 90%;
      .main-title {
        padding-top: 30px;
        line-height: 40px;
        font-size: 30px;
      }
    }
    .main-bottom {
      width: 90%;
      margin: 0 auto;
      flex-direction: column;
      align-items: center;
      .cho-button {
        width: 100%;
        margin-bottom: 14px;
      }
      img {
        margin-bottom: 14px;
        width: 64px;
        height: 64px;
      }
    }
  }
  .data-row {
    width: 90%;
    margin: 0 auto;
    height: 170px;
    .bg {
      width: 70px;
      height: 70px;
    }
  }
}
@media (min-width: 900px) and (max-width: 1200px) {
  .header {
    .main {
      .logo {
        font-size: 24px;
      }
      .nav-item {
        font-size: 18px;
      }
    }
  }
}
</style>