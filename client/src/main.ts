import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import App from './App.vue'
import HomeView from './views/HomeView.vue'

import './assets/main.css'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: HomeView
        },
    ]
})

const app = createApp(App)

app.use(router)

app.mount('#app')
