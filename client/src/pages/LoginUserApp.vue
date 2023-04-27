<template>
  <div style="background-color: var(--dark-old)" class="d-flex justify-content-center align-items-center vh-100 flex-column">
    
    <form ref="frmLogin" class="row form-app w-25 p-3" @submit="e => login(e)">
        <div class="text-center">
            <h1>Connexion</h1>
        </div>
        <div class="form-group">
            <input placeholder="Adresse mail" type="email" class="form-control" v-model="frmValue.username" required>
        </div>
        <div class="form-group">
            <input placeholder="Mot de passe" type="password" class="form-control" v-model="frmValue.password" required>
        </div> 
        <div class="mt-2 mb-2" v-if="error"> 
            <div class="alert alert-danger" role="alert" required>
                {{ error }}
            </div>
        </div>
        <div class="form-group text-center mt-1">
            <button type="submit" class="btn btn-success w-100">
                Se connecter
            </button>
        </div>
    </form>
  </div>
</template>

<script>
import { accountService } from '@/service'
export default {
    name: 'LoginUserApp',
    data() {
        return {
            frmValue: {
                username: '',
                password: ''
            },
            error: ''
        }
    },
    methods: {
        login(e) {
            e.preventDefault()
            var form_data = new FormData()
            for ( var key in this.frmValue ) {
                form_data.append(key, this.frmValue[key]);
            }
            accountService.login(form_data)
                .then((response) => {
                    accountService.saveToken(response.data.access_token)
                    this.$router.push({path: '/app/home'})
                }).catch((err) => {
                    this.error = err.response.data.detail
                })
        }
    }
}
</script>

<style>

</style>