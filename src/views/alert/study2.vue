<script setup>
</script>

<template>
    <div class="abox">
        <div class="c1">
            Study 2 details
        </div>
        <div class="c2">
            <img style="width: 100%;" src="/assets/fuckfeishu/Study2/study2_details_2.png" alt="" />
        </div>
        <div class="c3">
            <img style="width: 100%;" src="/assets/fuckfeishu/Study2/study2_details_3.png" alt="" />
        </div>
        <div class="c4">
            <img style="width: 100%;" src="/assets/fuckfeishu/Study2/study2_details_1.png" alt="" />
        </div>
        <div class="c5">
            <span>
                To further clarify the associations between categorical and dimensional models, a dimension-category hybrid model (Model 7) was evaluated where clustering techniques were applied on the relationships in the FAVEE space.
            </span>
            <br/>
            <br/>
            <span>
                <strong>Model comparison analysis</strong> suggested that models 3 (HPP), 6 (FAVEE) and 7 (FAVEE-HPP) had the highest cross-subject reliability, despite no difference between three of them.
            </span>
        </div>
        <div class="c6">
            <span style="font-size: 32px; line-height: 40px; font-weight: 700;">
                Conclusion
            </span>
            <br/>
            <span>
                Relationship concepts can be reliably represented either as continuous dimensions (FAVEE) or discrete categories (HPP), and most importantly, these two representational geometries can be compatibly integrated in the same framework (FAVEE-HPP model)
            </span>
        </div>
        <div class="c7">
            <span>
                The flow chart illustrates how people conceptualize human relationships via the joint framework of dimensions and categories. Each principal dimension of the FAVEE space functions as a classifier: as all relationships (indicated by word clouds) go through them stepwise, it firstly generates three implicit clusters of HPP (in light blue) and then six explicit clusters (in purple).
            </span>
        </div>
    </div>
</template>

<style scoped>
.abox {
    display: grid;
    width: 100vw;
    min-height: 100vh;
    grid-template-columns: 20px repeat(8, 1fr) 20px;
    grid-template-rows: 20px repeat(5, auto);
    text-align: left;
    align-items: stretch;
}
.c1 {
    grid-area: 2 / 2 / 3 / 10;
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}
.c2 {
    grid-area: 3 / 2 / 5 / 4;
}
.c3 {
    grid-area: 3 / 4 / 5 / 6;
}
.c4 {
    grid-area: 5 / 2 / 6 / 6;
}
.c5 {
    grid-area: 3 / 6 / 4 / 10;
}
.c6 {
    padding: 20px;
    margin: 20px 0;
    background-color: #E7E6E6;
    border-radius: 9px;
    grid-area: 4 / 6 / 5 / 10;
}
.c7 {
    grid-area: 5 / 6 / 6 / 10;
}
</style>