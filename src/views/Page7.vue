<template>
    <div class="box">
        <div class="s1">
            <span style="cursor: pointer; font-size: 20px; line-height: 32px;">Study 3</span>
            <br />
            <span style="font-size: 26px; line-height: 1.5em; font-weight: 700;">
                Universality and cultural variability
            </span>
        </div>
        <div class="s2">
            <img style="width: 100%;" src="/assets/fuckfeishu/Study3/更新图/china.jpg" alt="">
        </div>
        <div class="s3">
            <img style="width: 100%;" src="/assets/fuckfeishu/Study3/更新图/uk.jpg" alt="">
        </div>
        <div class="s4">
            <span>
                In different cultures, people interact with each other following different traditions. For example, the wedding is an important occasion to witness two people tying the knot, and the ceremony varies from culture to culture. 
            </span>
            <br/>
            <br/>
            <span>
                There is a custom in China where the bride and groom, dressed in red gowns, bow three times to honor the heaven, parents, and spouse. The parents are important witnesses, and the couple is required to offer tea to them, while in the West, the priest is an important witness to the two people.
            </span>
        </div>
        <div class="s5">
            <span>
                All human cultures have rich vocabularies devoted to describing social relationships.Translation dictionaries, for example, suggest that the English word ‘neighbors’ can be equated with the Chinese word ‘邻居’ and the Hebrew word ‘שכנים’. 
            </span>
            <br />
            <br />
            <span>
                But the concept of ‘neighbors’ is not the same in the US, China, and Israel. We found the more modern a region is, the concept of “Neighbors” in this region is more formal and distant.
            </span>
        </div>
        <div class="s6">
            <img style="width: 100%;" src="/assets/fuckfeishu/Study3/更新图/Extended-Data-Fig.-9.png" alt="">
        </div>
    </div>
</template>

<style scoped>
.box {
    grid-template-rows: 20px repeat(5, auto) 40px;
    text-align: left;
    grid-row-gap: 0px;
    line-height: 1.8em;
}
.s1 {
    grid-area: 2 / 2 / 3 / 6;
}
.s2 {
    grid-area: 3 / 2 / 6 / 4;
}
.s3 {
    grid-area: 3 / 4 / 6 / 6;
}
.s4 {
    grid-area: 6 / 2 / 7 / 6;
}
.s5 {
    grid-area: 2 / 6 / 4 / 10;
}
.s6 {
    grid-area: 4 / 6 / 7 / 10;
}
</style>