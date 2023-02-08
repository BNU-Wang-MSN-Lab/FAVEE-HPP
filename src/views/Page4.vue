<script setup>
const emits = defineEmits(["alertOpen"]);
</script>

<template>
    <div class="box">
        <div class="s1">
            <span id="study2" style="cursor: pointer; font-size: 20px; line-height: 32px;">Study 2</span>
            <br />
            <span style="font-size: 26px; line-height: 1.5em; font-weight: 700;">
                Categorial and dimensional representations
            </span>
        </div>
        <div class="s2">
            <strong>the galaxy in the universe, relationships can also be clustered into different categories.</strong>
            Although we
            found a cognitive space in Study 1, categorical thinking is pervasive when people manage relationships in
            daily life, such as arranging messages and phone contacts with labels, assigning seating for wedding guests
            by groups, and buying different travel souvenirs for friends, relatives and work colleagues.
        </div>
        <div class="s3">
            <img src="/assets/fuckfeishu/Study2/study2_example.png" style="width: 100%;" alt="">
        </div>
        <div class="s4">
            Using three behavior tasks, we found the categorical model. The multi-arrangement task and dimensional
            survey (Model 1 and Model 3) both indicated <strong>three core clusters (i.e., hostile, private, and public,
                abbreviated as HPP)</strong> whereas the free sorting task (Model 2) identified <strong>six clusters
                (i.e., hostile, romantic, familial, affiliative, transactional, and power). </strong>
            <br />
            For dimensional models two categorization tasks consistently suggested a 2D space of ‘Valence-Formality’
            (Model 4 and Model 5) whereas the dimensional survey identified the 5D FAVEE space, which replicated the
            results in Study 1 (Model 6).
        </div>
        <div class="s5">
            <img src="/assets/fuckfeishu/Study2/study2_tasks.png" style="width: 100%;" alt="">
            <div @click="emits('alertOpen', 'alertStudy2')" style="font-size: 22px; width: 25%; line-height: 1em; color: var(--theme-color-blue); cursor: pointer;">
                More details>
            </div>
            <div style="font-size: 12px; width: 75%; line-height: 1em;">
                When you hover over the interaction diagram, you'll see the specific relationships, and the specific values of their positions in space.
            </div>
        </div>
    </div>
</template>

<style scoped>
.box {
    grid-template-rows: 20px repeat(4, auto) 40px;
    text-align: left;
    grid-row-gap: 0;
}

.s1 {
    grid-area: 2 / 2 / 3 / 10;
}

.s2 {
    grid-area: 3 / 2 / 4 / 6;
}

.s3 {
    grid-area: 4 / 2 / 5 / 6;
}

.s4 {
    grid-area: 5 / 2 / 6 / 6;
}

.s5 {
    grid-area: 3 / 6 / 6 / 10;
}
.s5>div {
    display: inline-block;
    vertical-align: middle;
}
</style>