import HomeApp from './pages/HomeApp'

import RegisterUserApp from './pages/RegisterUserApp'
import LoginUserApp from './pages/LoginUserApp'
import AppMusicHome from './pages/AppMusicHome'

import {createRouter, createWebHistory} from 'vue-router'

import { authGuard } from '@/helpers/auth-guard'

const routes = [
    {
        name: 'HomeApp',
        component: HomeApp,
        path: '/',
    },
    {
        name: 'RegisterUserApp',
        component: RegisterUserApp,
        path: '/register'
    },
    {
        name: 'LoginUserApp',
        component: LoginUserApp,
        path: '/login',
    },
    {
        name: 'AppMusicHome',
        component: AppMusicHome,
        path: '/app',
        meta: {
            requireAuth: true,
            reduireSideBar: true 
        }
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


router.beforeEach((to, from, next) => {
    console.debug(from)
    if(to.meta.requireAuth) {
        authGuard()
    }
    next()
})

export default router 