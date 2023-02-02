import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'

const app = createApp(App); 
// app.config.globalProperties.$hppp = {};
app.use(router).mount('#app');
