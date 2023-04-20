import Axios from './caller.service'

let login = (credential) => {
    const config = {
        headers: {
            'Content-Type': 'application/x-www-form-urlencode',
        }
    }
    return Axios.post('/user/login', credential, config)
}

let logout = () => {
    localStorage.removeItem('access_token')
}

let getToken = () => {
    return localStorage.getItem('access_token')
}

let saveToken = (token) => {
    localStorage.setItem('access_token', token)
}

let isLogged = () => {
    let token = localStorage.getItem('access_token')
    return !!token
}

export const accountService = {
    login,
    logout,
    saveToken,
    isLogged,
    getToken,
}