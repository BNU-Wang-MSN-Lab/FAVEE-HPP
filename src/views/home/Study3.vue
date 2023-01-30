<script setup>
import * as THREE from "three";
import { onMounted } from "vue";
const emits = defineEmits(["alertOpen"]);

onMounted(() => {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setClearColor(0xf5f6f7, 1.0);
    document.querySelector(".canvas").appendChild(renderer.domElement);

    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshBasicMaterial({ color: 0xffff00 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    camera.position.z = 5;

    function animate() {
        requestAnimationFrame(animate);
        cube.rotation.x += 0.05;
        cube.rotation.y += 0.05;
        renderer.render(scene, camera);
    }
    animate();
});
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
                    @click="emits('alertOpen', 'study3')" style="color: var(--theme-color-blue); cursor: pointer;">model
                    details ></span></p>
            <p style="font-size: 16px; line-height: 24px;">Combined with the data in 19 regions, we get the
                world-averaged model.</p>
            <p style="font-size: 16px; line-height: 24px;">You can explore your interested relationship!</p>
        </div>
        <div class="iBox">
            <div class="canvas"></div>
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

.iBox {
    width: 1280px;
    height: 800px;
}

.iBox .canvas {
    width: 800px;
    height: 700px;
}
</style>