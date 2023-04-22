import HomeApp from './pages/HomeApp'

import RegisterUserApp from './pages/RegisterUserApp'
import LoginUserApp from './pages/LoginUserApp'

import AppMusic from './pages/AppMusic'
import AppHome from './pages/AppHome'
import AppProfilUser from './pages/AppProfilUser'
import AppLibraryUser from './pages/AppLibraryUser'

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
        name: 'AppMusic',
        component: AppMusic,
        path: '/app',
        meta: {
            requireAuth: true,
            reduireSideBar: true 
        },
        children: [
            { path: '/app/home', name: 'AppHome', component: AppHome },
            { path: '/app/profil', name: 'AppProfilUser', component: AppProfilUser },
            { path: '/app/library', name: 'AppLibraryUser', component: AppLibraryUser }
        ]
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