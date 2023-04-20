import { createApp } from 'vue'
import App from './App.vue'

import 'bootstrap/dist/css/bootstrap.css'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'

import router from './router'

import axios from 'axios';


const app = createApp(App)

app.config.globalProperties.$axios = axios
app.config.globalProperties.$apiCountry = "https://restcountries.com/v3.1/all"
app.config.globalProperties.$api = "http://127.0.0.1:8000"

app.use(bootstrap).use(router).mount('#app')
