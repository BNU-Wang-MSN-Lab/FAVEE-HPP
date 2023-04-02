
<template>
  <div>
    <div class="main">
      <!-- card -->
      <div class="block1">
        <div class="card-container">
          <my-title
            class="my-title"
            title="Richness and Diversity of Human Relationships"
          ></my-title>
          <div class="con-desc">
            We build connections with a wide range of people in our families,
            schools, workplaces, neighborhoods, and online communities. How do
            we make sense of such complex systems of social relationships? Can
            you identify the social relationships played in Leonardo DiCaprio’s
            movie world? Hover the mouse over the icon to reveal the answer.
          </div>
        </div>
        <card-list></card-list>
      </div>
      <!-- 模块二 -->
      <div class="block2">
        <my-title
          class="my-title"
          tipColor="rgba(68, 76, 252, 1)"
          title="Scientific Questions To Address"
          type="2"
        ></my-title>
        <div class="container">
          <div class="left">
            <div class="con-title">
              What are the basic building blocks of human relationships?
            </div>
            <div class="con-desc">
              What is the elemental forms of social relationships? Do our mind
              construct social relationship concepts in terms of discrete
              categories (e.g., family, friends, colleagues) or continuous
              dimensions (e.g., intimacy, equality, uniqueness)?
            </div>
          </div>
          <div class="right">
            <img class="right1" src="@/assets/img/home/right1.png" alt="" />
            <img class="right2" src="@/assets/img/home/right2.png" alt="" />
          </div>
        </div>
      </div>
      <!-- 模块三 -->
      <div class="block3">
        <div class="left">
          <img class="left1" src="@/assets/img/home/b_left1.png" alt="" />
          <img class="left2" src="@/assets/img/home/b_left.png" alt="" />
        </div>
        <div class="right">
          <div class="con-title">
            How do we construct complex knowledge about relationships?
          </div>
          <div class="con-desc">
            Social structure in non-human primates is dominated by hierarchy and
            kinship affiliation. Human society, in contrast, is governed by far
            more diverse and complex types of relationships exist (e.g., a
            cousin can also be an enemy). How do we make sense of one another
            and form the general knowledge about interpersonal relatedness?
          </div>
        </div>
        <div class="line">
          <div class="line1"></div>
          <div class="line2"></div>
          <div class="line3"></div>
        </div>
      </div>
    </div>
    <!-- 模块四 -->
    <div class="block4">
      <div class="main">
        <div class="left">
          <div class="con-title">
            Do all people in the world understand social relationships in the
            same way?
          </div>
          <div class="con-desc">
            All human cultures have rich vocabularies devoted to describing
            social relationships. Translation dictionaries, for example, suggest
            that the English word ‘couples’ can be equated with the Chinese word
            ‘夫妻’ and the Hebrew word ‘夫妻’ . But does this mean that the
            conceptual meaning of ‘couple’ is the same in the UK, China, and
            Israel?
          </div>
          <div class="link" @click="visible = true">More details</div>
          <div class="tip-box">
            <tip :type="3"></tip>
          </div>
        </div>
        <div class="dialog-box">
          <my-dialog v-model:visible="visible">
            In different cultures, people interact with each other following
            different traditions. For example, the wedding is an important
            occasion to witness two people tying the knot, and the ceremony
            varies from culture to culture. There is a custom in China where the
            bride and groom, dressed in red gowns, bow three times to honor the
            heaven, parents, and spouse. The parents are important witnesses,
            and the couple is required to offer tea to them, while in the West,
            the priest is an important witness to the two people.
          </my-dialog>
        </div>
        <div class="right">
          <img class="right1" src="@/assets/img/home/banner2.png" alt="" />
          <img class="right1" src="@/assets/img/home/banner1.png" alt="" />
        </div>
      </div>
    </div>
    <!-- 模块5 -->
    <div class="block5">
      <div class="main">
        <my-title
          title="What is the FAVEE-HPP model?"
          :tipVisible="false"
        ></my-title>
        <p class="sub-title">
          The FAVEE-HPP model is a framework that outlines how our mind mentally
          represent and organize social relationship knowledge.
        </p>
        <div class="content">
          <div class="video-box">
            <video
              class="video"
              src="@/assets/video/infovideo.mp4"
              controls
            ></video>
          </div>
          <div class="right-box">
            <div class="item">
              <p class="item-title">
                FAVEE refers to the five basic dimensions of social
                relationships:
              </p>
              <div class="item-content">
                <p class="item-content-row">
                  1）Formality (whether a relationship is formal or informal?)
                </p>
                <p class="item-content-row">
                  2）Activeness (whether a relationship is close or distant?)
                </p>
                <p class="item-content-row">
                  3）Valence (whether a relationship is harmony or full of
                  conflict?)
                </p>
                <p class="item-content-row">
                  4）Exchange (whether to exchange concrete resources like money
                  or symbolic resources like love?)
                </p>
                <p class="item-content-row">
                  5）Equality (whether people is equal or inequal?)
                </p>
              </div>
            </div>
            <div class="item">
              <p class="item-title">
                HPP refers to the three default categories of social
                relationships:
              </p>
              <div class="item-content">
                <p class="item-content-row">1）Hostile relationships</p>
                <p class="item-content-row">2）Public relationships,</p>
                <p class="item-content-row">3）Private relationships.</p>
              </div>
              <div class="item-content-bottom">
                “To travel across the universe, we use longitude and latitude
                for spatial navigation. To appropriately interact with others,
                we use the FAVEE-HPP model for social navigation. “
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 模块6 -->
    <div class="block6">
      <div class="main">
        <my-title title="Theoretical and Empirical Implications"></my-title>
        <div class="img-row">
          <img src="@/assets/img/home/block6_1.png" alt="" class="block6-img" />
          <img src="@/assets/img/home/block6_2.png" alt="" class="block6-img" />
          <img src="@/assets/img/home/block6_3.png" alt="" class="block6-img" />
          <img src="@/assets/img/home/block6_4.png" alt="" class="block6-img" />
        </div>
        <div class="main-content">
          <div class="m-title">Human Sociality and Cognition</div>
          <div class="m-content">
            Socialization is hypothesized to be one of the major drivers behind
            the evolution of human cognition. In primitive society, we were
            primarily dependent on our family, friends, and spouses, as they
            provide us with protection, unique connection, and love. Our
            understanding of these private relationships is deeply shaped by
            traditional inheritance (e.g., religious beliefs and rituals).
          </div>
          <div class="m-content">
            Development of modernization leads to a large scale of human
            community and evolves into new ways of social interaction. We begin
            to leave our core social network and cooperate with strangers. We
            adapt to exchange with others equally or proportionally to satisfy
            our various needs. Today's pluralistic world is composed of various
            stories that are used to build consensus, which maintain the
            stability of public life.
          </div>
        </div>
      </div>
    </div>
    <!-- 模块7 -->
    <div class="block7">
      <div class="main">
        <div class="left">
          <img
            src="@/assets/img/home/block7_left.png"
            alt=""
            class="left-banner"
          />
          <div class="left-bottom">
            <p class="title">Predictive Power</p>
            <img src="@/assets/img/home/arrow.png" alt="" class="right-arrow" />
            <div class="link" @click="visible1 = true">More details</div>
            <p class="left-main-text">
              No man is an island. Human life is a process of seeking,
              sustaining, repairing, judging, adjusting, and sometimes
              dissolving relationships. The quality and quantity of social
              relationships are integral not only to our survival but our
              capacity to thrive. Social isolation and poor relationships affect
              individual’s cognition, behavior, development, and well-being.
            </p>
            <p class="left-main-text">
              The FAVEE-HPP framework establishes an objective and quantitative
              measure of social relationships that can be used to describe and
              explain interpersonal behaviors under each relationship and make
              predictions about their future interaction. For example, we found
              that the FAVEE-HPP model is useful to predict important human
              factors such as well-being, corruption, interpersonal trust, and
              marriage
            </p>
            <div class="line">
              <div class="line1"></div>
              <div class="line2"></div>
              <div class="line3"></div>
            </div>
          </div>
          <div class="pc-hidden">
            The FAVEE-HPP framework set up the link between human sociality and
            cognition and provides implications on how human cognitive processes
            are systematically configured and adaptively operated for different
            interpersonal contexts. It can help us understand why humans can
            form and maintain relationships that extend beyond immediate family
            members and how humans evolved from ‘animal’ (i.e., no cooperation)
            to ‘social animal’ (i.e., small-scale cooperation based on personal
            relationships) and to ‘cultural animal’ (i.e., large-scale
            cooperation based on public relationships).
          </div>
        </div>
        <div class="dialog-box">
          <my-dialog v-model:visible="visible1">
            In addition, from a developmental perspective, humans begin to
            accrue cognitive heuristics and stereotypes about social
            relationships at birth (e.g., stranger danger, respect for elders).
            Our interpersonal experiences will shape our world view. For
            example, people who grow up in a broken family or had chronic peer
            rejection might form negative impressions about familial and
            affiliative relationships. Likewise, people who experienced
            harmonious relationships with current employers, clients or
            coworkers might adopt more positive views on work relationships. The
            FAVEE-HPP framework can be used to develop psychometric tests to
            measure where an individual lies on the spectrum of each of the five
            dimensions (like the ‘big-five’ personality test), and
            quantitatively examine how individual differences in relationship
            representations is linked to interpersonal difficulties in daily
            life.
          </my-dialog>
        </div>
        <div class="right">
          <div class="pc-hidden left-bottom">
            <p class="title">Predictive Power</p>
            <img src="@/assets/img/home/arrow.png" alt="" class="right-arrow" />
            <div class="link" @click="visible1 = true">More details</div>
            <p class="left-main-text">
              No man is an island. Human life is a process of seeking,
              sustaining, repairing, judging, adjusting, and sometimes
              dissolving relationships. The quality and quantity of social
              relationships are integral not only to our survival but our
              capacity to thrive. Social isolation and poor relationships affect
              individual’s cognition, behavior, development, and well-being.
            </p>
            <p class="left-main-text">
              The FAVEE-HPP framework establishes an objective and quantitative
              measure of social relationships that can be used to describe and
              explain interpersonal behaviors under each relationship and make
              predictions about their future interaction. For example, we found
              that the FAVEE-HPP model is useful to predict important human
              factors such as well-being, corruption, interpersonal trust, and
              marriage
            </p>
            <div class="line">
              <div class="line1"></div>
              <div class="line2"></div>
              <div class="line3"></div>
            </div>
          </div>
          <div class="right-main-text">
            The FAVEE-HPP framework set up the link between human sociality and
            cognition and provides implications on how human cognitive processes
            are systematically configured and adaptively operated for different
            interpersonal contexts. It can help us understand why humans can
            form and maintain relationships that extend beyond immediate family
            members and how humans evolved from ‘animal’ (i.e., no cooperation)
            to ‘social animal’ (i.e., small-scale cooperation based on personal
            relationships) and to ‘cultural animal’ (i.e., large-scale
            cooperation based on public relationships).
          </div>
          <img src="@/assets/img/home/arrow.png" alt="" class="right-arrow" />
          <img
            src="@/assets/img/home/block7_right.png"
            alt=""
            class="right-banner"
          />
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import myTitle from "./components/myTitle.vue";
import cardList from "./components/cardList.vue";
import myDialog from "./components/myDialog.vue";
import tip from "./components/tip.vue";
import { ref } from "vue";
const visible = ref(false);
const visible1 = ref(false);
</script>

<style lang="scss" scoped>
.main {
  width: 90%;
  max-width: 1200px;
}

.card-container {
  padding-top: 90px;
  padding-bottom: 80px;

  .my-title {
    margin-bottom: 60px;
  }
}

.con-title {
  font-size: 24px;
  color: #000;
  font-weight: bold;
  line-height: 30px;
  margin-bottom: 10px;
}

.con-desc {
  font-size: 16px;
  color: rgba(35, 37, 54, 0.6);
  text-align: justify;
  line-height: 24px;
}

.block2 {
  padding: 90px 0;

  .container {
    margin-top: 50px;
    display: flex;
    align-items: center;

    .left {
      flex: 1;
      margin-right: 200px;
    }

    .right {
      .right1 {
        width: 216px;
      }

      .right2 {
        width: 218px;
      }
    }
  }
}

.block3 {
  position: relative;
  display: flex;
  align-items: center;
  padding-bottom: 160px;
  padding-top: 170px;

  .left {
    .left1 {
      width: 296px;
      margin-right: 60px;
    }

    .left2 {
      width: 249px;
    }
  }

  .right {
    margin-left: 100px;
    flex: 1;
  }

  .line {
    position: absolute;
    bottom: 90px;
    right: 0;
    height: 8px;
    width: 400px;
    display: flex;
  }

  .line1 {
    width: 25%;
    height: 100%;
    background-color: var(--theme-color-orange);
  }

  .line2 {
    width: 50%;
    height: 100%;
    background-color: rgba(255, 211, 175, 1);
  }

  .line3 {
    width: 25%;
    height: 100%;
    background-color: var(--theme-color-blue);
  }
}

.block4 {
  position: relative;
  height: 500px;
  background-color: rgba(249, 249, 255, 1);

  .dialog-box {
    bottom: 0;
    text-align: left;
    position: absolute;
    width: 100%;
    transform: translateY(60%);
    z-index: 100;
    max-width: 1200px;
  }

  .main {
    display: flex;
    align-items: center;
    height: 100%;
  }

  .left {
    position: relative;
    margin-right: 85px;

    .con-title {
      margin-bottom: 30px;
    }
    .con-desc {
      margin-bottom: 20px;
    }

    .tip-box {
      position: absolute;
      right: 0;
      // transform: rotate(180deg);
    }
  }

  .right {
    display: flex;
  }

  .right1 {
    width: 200px;
    height: 150px;
    margin-right: 30px;
    border: 4px solid var(--theme-color-orange);
  }
}

.block5 {
  padding: 70px 0;
  background-color: #fff;

  .sub-title {
    font-size: 24px;
    font-weight: bold;
    color: rgba(35, 37, 54, 1);
    line-height: 34px;
    margin: 30px 0;
  }

  .content {
    display: flex;
    height: 470px;

    .video-box {
      width: 45%;

      .video {
        width: 100%;
        height: 100%;
      }
    }

    .right-box {
      width: 50%;
      margin-left: 100px;
      height: 100%;
      display: flex;
      flex-direction: column;

      .item {
        flex: 1;

        .item-title {
          font-size: 16px;
          font-weight: bold;
          margin-bottom: 4px;
        }

        .item-content-row {
          font-size: 16px;
          color: rgba(35, 37, 54, 1);
          opacity: 0.6;
          line-height: 26px;
        }

        .item-content-bottom {
          margin-top: 90px;
          font-size: 16px;
          color: rgba(35, 37, 54, 1);
          opacity: 0.6;
          line-height: 26px;
        }
      }
    }
  }
}

.block6 {
  padding: 80px 0;
  background-color: rgba(249, 249, 255, 1);

  .img-row {
    margin: 34px auto 62px;
    margin-left: -140px;
    display: flex;

    .block6-img {
      width: 350px;
      margin-right: 50px;
    }
  }

  .main-content {
    .m-title {
      font-size: 24px;
      font-weight: bold;
    }

    .m-content {
      opacity: 0.6;
      font-size: 16px;
      margin-top: 12px;
    }
  }
}

.block7 {
  padding-top: 50px;
  padding-bottom: 80px;
  background-color: #fff;
  position: relative;
  padding-bottom: 330px;

  .main {
    display: flex;
    .line {
      position: absolute;
      bottom: 0;
      left: 0;
      transform: translateY(100%);
      height: 16px;
      width: 300px;
      display: flex;

      .line1 {
        height: 100%;
        width: 26%;
        background-color: var(--theme-color-orange);
      }

      .line2 {
        height: 100%;
        width: 55%;
        background-color: rgba(255, 211, 175, 1);
      }

      .line3 {
        height: 100%;
        width: 19%;
        background-color: var(--theme-color-blue);
      }
    }
    .left {
      flex: 1;
      margin-right: 50px;

      .left-banner {
        width: 100%;
      }

      .left-bottom {
        position: relative;
        margin-top: 48px;
        padding-top: 10px;
        text-align: right;
        padding-bottom: 20px;

        .title {
          text-align: left;
          font-size: 24px;
          font-weight: bold;
        }

        .right-arrow {
          width: 26px;
          height: 26px;
          transform: rotate(180deg);
          margin-bottom: 10px;
        }

        .left-main-text {
          color: rgba(35, 37, 54, 0.6);
          font-size: 16px;
          line-height: 26px;
          margin-bottom: 30px;
          text-align: left;
          text-align: justify;
        }

        .link {
          position: absolute;
          bottom: 0px;
          right: 100px;
        }
      }
    }

    .right {
      flex: 1;

      .right-main-text {
        color: rgba(35, 37, 54, 0.6);
        font-size: 16px;
        line-height: 26px;
        margin-bottom: 30px;
        text-align: left;
        text-align: justify;
      }

      .right-arrow {
        padding-bottom: 50px;
      }

      .right-banner {
        width: 100%;
      }
    }

    .dialog-box {
      bottom: 100px;
      position: absolute;
      width: 100%;
      max-width: 1200px;
    }
  }
}

.link {
  cursor: pointer;
  display: inline-block;
  position: relative;
  color: var(--theme-color-blue);
}

.link::after {
  position: absolute;
  right: 0;
  top: 50%;
  transform: translate(140%, -50%);
  display: flex;
  content: "";
  width: 24px;
  height: 1px;
  background-color: #000;
  margin-left: 10px;
}
.pc-hidden {
  color: rgba(35, 37, 54, 0.6);
  display: none;
}

@media screen and (max-width: 600px) {
  .block1 {
    .card-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;

      .my-title {
        margin-bottom: 30px;
      }

      .card-list {
        display: flex;
        flex-direction: column;
        flex-wrap: nowrap;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
      }
    }
  }

  .con-title {
    font-size: 1.5rem;
    color: #000;
    font-weight: bold;
    line-height: 1.7rem;
    margin-bottom: 20px;
  }

  .con-desc {
    font-size: 1rem;
    color: rgba(35, 37, 54, 0.6);
    text-align: justify;
    line-height: 18px;
  }

  .block1 {
    width: 90%;
    margin: 0 auto;
  }

  .block2 {
    width: 90%;
    padding: 30px 0;
    margin: 0 auto;

    .container {
      flex-direction: column;

      .left {
        margin-right: 0;
      }

      .right {
        width: 100%;
        margin-top: 20px;

        .right1 {
          flex: 1;
          width: 46%;
          margin-right: 4%;
        }

        .right2 {
          flex: 1;
          width: 46%;
        }
      }
    }
  }

  .block3 {
    width: 90%;
    margin: 0 auto;
    padding-top: 10px;
    padding-bottom: 60px;
    justify-content: flex-start;
    align-items: flex-end;
    flex-direction: column-reverse;

    .line {
      max-width: 400px;
      width: 50%;
      bottom: 20px;
    }

    .left {
      margin-top: 20px;

      .left1 {
        width: 50%;
        margin-right: 10%;
      }

      .left2 {
        width: 40%;
      }
    }

    .right {
      margin: 0;
    }
  }

  .block4 {
    width: 100%;
    margin: 0 auto;
    height: auto;

    .main {
      width: 90%;
      padding-top: 40px;
      display: flex;
      flex-direction: column;

      .left {
        margin-right: 0;
      }

      .right {
        margin-top: 40px;
        width: 100%;
        display: flex;

        .right1 {
          width: 48%;
          height: auto;
        }

        .right2 {
          width: 48%;
          height: auto;
        }
      }
    }
  }

  .block5 {
    width: 90%;
    margin: 0 auto;
    padding: 70px 0 20px;

    .sub-title {
      font-size: 1.4rem;
      line-height: 1.6rem;
      margin: 30px 0;
    }

    .content {
      flex-direction: column;
      height: auto;

      .video-box {
        width: 100%;
        margin-bottom: 30px;
        .video {
          width: 100%;
          height: 100%;
        }
      }

      .right-box {
        width: 100%;
        margin-left: 0;

        .item {
          margin-bottom: 20px;

          .item-title {
            font-size: 1.4rem;
          }

          .item-content-row {
            font-size: 1.3rem;
            line-height: 1.5rem;
          }

          .item-content-bottom {
            font-size: 1.3rem;
            line-height: 1.5rem;
            margin-top: 20px;
          }
        }
      }
    }
  }

  .block6 {
    width: 90%;
    margin: 0 auto;

    .img-row {
      margin: 34px auto 62px;
      display: flex;
      flex-wrap: wrap;

      .block6-img {
        width: 90%;
        margin: 0 auto 20px;
      }
    }

    .main-content {
      .m-title {
        font-size: 1.5rem;
        font-weight: bold;
      }

      .m-content {
        opacity: 0.6;
        font-size: 1.3rem;
        margin-top: 20px;
      }
    }
  }

  .block7 {
    width: 90%;
    display: flex;
    margin: 0 auto;
    flex-direction: column;

    .main {
      display: flex;
      flex-direction: column;

      .left {
        margin-right: 0;

        .left-bottom {
          display: none;
          .title {
            font-size: 1.5rem;
            margin-bottom: 10px;
          }
          .left-main-text {
            font-size: 1.3rem;
            line-height: 1.5rem;
          }
          .line {
            max-width: 300%;
            height: 8px;
            width: 50%;
            bottom: 25px;
          }

          .link {
            right: 20px;
            bottom: 30px;
          }
        }
        .pc-hidden {
          display: block;
          font-size: 1.3rem;
          line-height: 1.5rem;
          margin-top: 10px;
        }
      }
      .right {
        .left-bottom {
          position: relative;
          display: block;
          padding-bottom: 60px;
          padding-top: 30px;
          .title {
            color: #000;
            font-weight: bold;
            font-size: 1.5rem;
            margin-bottom: 10px;
          }
          .left-main-text {
            font-size: 1.3rem;
            line-height: 1.5rem;
          }
          .line {
            max-width: 300%;
            height: 8px;
            width: 50%;
            bottom: 25px;
          }

          .link {
            position: absolute;
            right: 20px;
            bottom: 30px;
          }
        }
        .right-main-text {
          display: none;
          font-size: 1.3rem;
          line-height: 1.5rem;
        }
      }
      .right-arrow {
        display: none;
      }

      .dialog-box {
        bottom: 1000px;
        position: absolute;
        width: 100%;
        max-width: 1200px;
        z-index: 100;
      }
    }
  }
}

@media (min-width: 600px) and (max-width: 900px) {
  .block1 {
    .card-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;

      .my-title {
        margin-bottom: 30px;
      }

      .card-list {
        display: flex;
        flex-direction: column;
        flex-wrap: nowrap;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
      }
    }
  }

  .con-title {
    font-size: 1.5rem;
    color: #000;
    font-weight: bold;
    line-height: 30px;
    margin-bottom: 30px;
  }

  .con-desc {
    font-size: 22px;
    color: rgba(35, 37, 54, 0.6);
    text-align: justify;
    line-height: 26px;
  }

  .block1 {
    width: 90%;
    margin: 0 auto;
  }

  .block2 {
    width: 90%;
    padding: 30px 0;
    margin: 0 auto;

    .container {
      flex-direction: column;

      .left {
        margin-right: 0;
      }

      .right {
        width: 100%;
        margin-top: 20px;

        .right1 {
          flex: 1;
          width: 46%;
          margin-right: 4%;
        }

        .right2 {
          flex: 1;
          width: 46%;
        }
      }
    }
  }

  .block3 {
    width: 90%;
    margin: 0 auto;
    padding-top: 10px;
    padding-bottom: 60px;
    justify-content: flex-start;
    align-items: flex-end;
    flex-direction: column-reverse;

    .line {
      max-width: 400px;
      width: 50%;
      bottom: 20px;
    }

    .left {
      width: 100%;
      margin-top: 20px;

      .left1 {
        width: 50%;
        margin-right: 10%;
      }

      .left2 {
        width: 40%;
      }
    }

    .right {
      margin: 0;
    }
  }

  .block4 {
    width: 100%;
    margin: 0 auto;
    height: auto;

    .dialog-box {
      transform: translateY(0);

      .dialog-content {
        padding-top: 20px;
      }
    }

    .main {
      width: 90%;
      padding-top: 40px;
      display: flex;
      flex-direction: column;

      .left {
        margin-right: 0;

        .link {
          font-size: 20px;
        }

        .con-title {
          margin-bottom: 50px;
        }
      }

      .right {
        margin-top: 40px;
        width: 100%;
        display: flex;

        .right1 {
          width: 48%;
          height: auto;
        }

        .right2 {
          width: 48%;
          height: auto;
        }
      }
    }
  }

  .block5 {
    width: 90%;
    margin: 0 auto;
    padding: 70px 0 20px;

    .sub-title {
      font-size: 20px;
      line-height: 24px;
      margin: 30px 0;
    }

    .content {
      flex-direction: column;
      height: auto;
      .video-box {
        width: 100%;
        margin-bottom: 40px;
      }
      .right-box {
        width: 100%;
        margin-left: 0;

        .item {
          margin-bottom: 20px;

          .item-title {
            font-size: 16px;
          }

          .item-content-row {
            font-size: 16px;
            line-height: 19px;
          }

          .item-content-bottom {
            font-size: 16px;
            line-height: 19px;
            margin-top: 40px;
          }
        }
      }
    }
  }

  .block6 {
    width: 90%;
    margin: 0 auto;

    .img-row {
      margin: 34px auto 62px;
      display: flex;
      flex-wrap: wrap;

      .block6-img {
        width: 90%;
        margin: 0 auto 20px;
      }
    }

    .main-content {
      .m-title {
        font-size: 20px;
        font-weight: bold;
      }

      .m-content {
        opacity: 0.6;
        font-size: 16px;
        margin-top: 20px;
      }
    }
  }

  .block7 {
    width: 90%;
    display: flex;
    margin: 0 auto;
    flex-direction: column;

    .main {
      display: flex;
      flex-direction: column;

      .left {
        margin-right: 0;

        .left-bottom {
          display: none;
          .line {
            max-width: 300%;
            height: 8px;
            width: 50%;
            bottom: 30px;
          }

          .link {
            right: 20px;
            bottom: 40px;
          }
        }
        .pc-hidden {
          display: block;
          margin-top: 10px;
        }
      }
      .right {
        .left-bottom {
          position: relative;
          display: block;
          padding-bottom: 60px;
          padding-top: 30px;
          .title {
            color: #000;
            font-weight: bold;
            margin-bottom: 10px;
          }
          .left-main-text {
          }
          .line {
            max-width: 300%;
            height: 8px;
            width: 50%;
            bottom: 25px;
          }

          .link {
            position: absolute;
            right: 20px;
            bottom: 30px;
          }
        }
        .right-main-text {
          display: none;
        }
      }

      .right-arrow {
        display: none;
      }

      .dialog-box {
        bottom: 1200px;
        position: absolute;
        width: 100%;
        max-width: 1200px;
      }
    }
  }
}

@media (min-width: 900px) and (max-width: 1200px) {
  .block2 {
    .container {
      .left {
        margin-right: 20px;
      }
    }
  }

  .block3 {
    padding-top: 20px;
    flex-direction: column-reverse;

    .left {
      margin-top: 50px;
      width: 100%;
      display: flex;
      justify-content: space-around;

      .left1 {
        width: 39%;
        margin-right: 30px;
      }

      .left2 {
        width: 34%;
      }
    }

    .right {
      margin-left: 0;
    }
  }

  .block4 {
    .link {
      font-size: 22px;
    }
  }

  .block5 {
    .content {
      height: auto;
      display: flex;
      flex-direction: column;
      .video-box {
        width: 100%;
        margin-bottom: 40px;
      }
      .right-box {
        width: 100%;
        margin-left: 0;
        .item {
          margin-bottom: 20px;
        }
      }
    }
  }

  .block6 {
    .img-row {
      width: 100%;
      display: flex;
      margin: 30px auto;

      .block6-img {
        flex: 1;
        width: 23%;
        margin-right: 2%;
      }
    }
  }

  .block7 {
    .main {
      .left {
        .left-bottom {
          .link {
            font-size: 20px;
            bottom: 10px;
            right: 40px;
          }
        }
      }
    }
  }
}
</style>
