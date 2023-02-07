import { createRouter, createWebHashHistory } from "vue-router";
import Home from '../views/Home.vue';

const routes = [
    { 
        path: "/",
        components: {
            default: Home
        }
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router