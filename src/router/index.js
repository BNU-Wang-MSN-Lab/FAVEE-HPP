import { createRouter, createWebHashHistory } from 'vue-router';
const routes = [
    {
        path: '/',
        redirect: '/layout/home'
    },
    {
        path: '/layout',
        name: 'Layout',
        component: () => import('../views/Layout/index.vue'),
        children: [
            {
                path: 'home',
                name: 'Home',
                component: () => import('../views/Home/index.vue')
            },
            {
                path: 'science',
                name: 'Science',
                component: () => import('../views/Science/index.vue')
            },
            {
                path: 'data',
                name: 'Data',
                component: () => import('../views/Data/index.vue')
            }
        ]
    }
]
const router = createRouter({
    history: createWebHashHistory(),
    routes
})
export default router;