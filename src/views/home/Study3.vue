<script setup>
const emits = defineEmits(["alertOpen"]);
</script>

<template>
    <div class="box">
        <div class="tit">
            <span class="one">Study 3</span>
            <br />
            <span class="two">
                <span style="color: var(--theme-color-blue)">U</span>niversality and cultural variability
            </span>
        </div>
        <div class="content">
            <p style="font-size: 24px; line-height: 30px; margin: 0;">World-averaged model</p>
            <p style="font-size: 12px; line-height: 18px; margin: 0;">Check the <span
                    @click="emits('alertOpen', 'alert3D')"
                    style="color: var(--theme-color-blue); cursor: pointer;">model
                    details ></span></p>
            <p style="font-size: 16px; line-height: 24px;">Combined with the data in 19 regions, we get the
                world-averaged model.</p>
            <p style="font-size: 16px; line-height: 24px;">You can explore your interested relationship!</p>
        </div>
        <div class="button">
            <div @click="emits('alertOpen', 'alertSubset')">Subset analysis</div>
            <div @click="emits('alertOpen', 'alertRelationship')">Relationship variability</div>
            <div @click="emits('alertOpen', 'alertCultural')">Cultural mechanism</div>
        </div>
        <div class="iBox">
            <div class="canvas"></div>
            <div class="choose">
                <div class="title">whick relationship are you interested in?</div>
                <div class="sel">
                    <select name="q1" id="q1">
                        <option value="">China</option>
                    </select>
                    <select name="q2" id="q2">
                        <option value="">USA</option>
                    </select>
                </div>
                <div class="view">
                    <div class="chos">
                        <div class="selected">FAVEE</div>
                        <div>33D</div>
                    </div>
                    <div class="img"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.box {
    width: 100%;
    position: relative;
    background: #f5f6f7;
    overflow: hidden;
}

.tit {
    text-align: left;
    margin: 70px 0 0 50px;
}

.tit .one {
    font-size: 24px;
    line-height: 30px;
}

.tit .two {
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
}

.content {
    text-align: left;
    width: 70%;
    margin: 40px 0 0 60px;
}
.button {
    text-align: left;
    margin: 0 0 0 50px;
}
.button>div {
    display: inline-block;
    padding: 5px 10px;
    margin: 10px 20px;
    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 9px;
    cursor: pointer;
}
.iBox {
    width: 1280px;
    height: 600px;
}
.iBox>div {
    vertical-align: middle;
}
.iBox .canvas {
    display: inline-block;
    width: 600px;
    height: 500px;
    background: #000;
}
.iBox .choose {
    display: inline-block;
    width: 500px;
    height: 500px;
    margin: 0 0 0 100px;
}
.choose .view {
    margin: 50px 0 0 0;
}
.choose .view .chos {
    width: 240px;
    margin: auto;
    border: 1px solid grey;
    border-radius: 9px;
    cursor: pointer;
}
.choose .view .chos>div {
    width: 120px;
    display: inline-block;
    line-height: 2em;
}
.choose .view .chos>.selected {
    background: grey;
    border-radius: 8px;
    color: white;
}
.choose .view .img {
    width: 300px;
    height: 300px;
    margin: auto;
    background: url(/assets/Study3/CHN/categorical/radar/radar_5d.png) no-repeat;
    background-size: contain;
}
</style>