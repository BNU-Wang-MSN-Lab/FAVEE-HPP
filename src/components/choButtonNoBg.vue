<template>
    <div class="cho-button-no-bg">
        <slot />
    </div>
</template>

<style scoped>
.cho-button-no-bg {
    display: inline-block;
    padding: 20px 57px 20px 32px;
    background-repeat: no-repeat;
    border: 1px solid var(--font-color-blue);
    color: var(--font-color-blue);
    position: relative;
    cursor: pointer;
}

.cho-button-no-bg::after {
    content: "";
    display: block;
    width: 20px;
    height: 0px;
    border: 1px solid var(--font-color-blue);
    position: absolute;
    top: calc(100% / 2 - 1px);
    right: calc(57px / 2 - 10px);
}
</style>
