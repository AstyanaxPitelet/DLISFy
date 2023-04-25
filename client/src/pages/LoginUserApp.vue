<template>
  <div class="container d-flex justify-content-center align-items-center vh-100 flex-column">
    <div class="text-center">
        <h1>Connexion</h1>
    </div>
    <form ref="frmLogin" class="row form-app" @submit="e => login(e)">
        <div class="form-group">
            <label class="form-label">Adresse mail : </label>
            <input type="mail" class="form-control" v-model="frmValue.username" required>
        </div>
        <div class="form-group">
            <label class="form-label">Mot de passe : </label>
            <input type="password" class="form-control" v-model="frmValue.password" required>
        </div> 
        <div class="mt-2 mb-2" v-if="error"> 
            <div class="alert alert-danger" role="alert" required>
                {{ error }}
            </div>
        </div>
        <div class="form-group text-center">
            <button type="submit" class="btn btn-success">
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