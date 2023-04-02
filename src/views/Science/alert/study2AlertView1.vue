<template>
    <div class="study2-1">
        <img src="@/assets/img/science/89.png" alt="">
        <!-- 华丽丽的分隔符 -->
        <div style="display: block; width: 25px; height: 25px; background-color: var(--orange );"></div>
        <div class="flex">
            <div>
                To further clarify the associations between categorical and dimensional models, a dimension-category hybrid model was evaluated where clustering techniques were applied on the relationships in the FAVEE space (Model 7). Model comparison analysis suggested that models 3 (HPP), 6 (FAVEE) and 7 (FAVEE-HPP) had the highest cross-subject reliability, despite no difference between three of them.
            </div>
            <div>
                <img src="@/assets/img/science/65462.png.png" alt="">
            </div>
            <div>
                <img src="@/assets/img/science/54654. 2.png" alt="">
            </div>
            <div>
                <div class="tit">Conclusion:</div>
                <div>Social relationship concepts can be reliably represented either as discrete categories (HPP) or continuous dimensions (FAVEE), and both models work equally well. More importantly, two structures can co-exist in the same representational space, and category might be a higher order structure that can be emerged from dimensions (FAVEE-HPP model)</div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.study2-1 {
    text-align: justify;
}
.study2-1 .tit {
    margin: 0 0 20px 0;
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 2.25rem;
}
.study2-1 img {
    width: 100%;
}
.study2-1 .flex {
    display: flex;
    height: 810px;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
}

.study2-1 .flex>div {
    max-width: 450px;
}
.study2-1 .flex>div:nth-child(4) {
    display: block;
    box-sizing: border-box;
    padding: 20px 40px 50px 40px;
    background-color: var(--morelightorange);
    background-image: linear-gradient(var(--lightorange), var(--lightorange));
    background-repeat: no-repeat;
}

@media screen and (max-width: 1000px) {
    .study2-1 .flex {
        height: auto;
    }
    .study2-1 .flex>div:nth-child(1) {
        width: 90%;
        max-width: none;
    }
}
</style>