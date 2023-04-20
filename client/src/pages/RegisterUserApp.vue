<template>
  <div class="container d-flex justify-content-center align-items-center vh-100 flex-column">
    <div class="text-center">
        <h1>S'inscire</h1>
    </div>
    <form ref="frmResigter" class="row form-app"  @submit="e => addUser(e)">
        <div class="row">
            <div class="form-group col-md-6">
                <label class="form-label">Nom : </label>
                <input type="text"  class="form-control" v-model="frmValue.name" required>
            </div>
            <div class="form-group col-md-6">
                <label class="form-label">Prenom : </label>
                <input type="text" class="form-control" v-model="frmValue.firstname" required>
            </div>
        </div>
        <div class="form-group">
            <label class="form-label">Adresse mail : </label>
            <input type="mail" class="form-control" v-model="frmValue.mail" required>
        </div>
        <div class="form-group">
            <label class="form-label">Mot de passe : </label>
            <input type="password" class="form-control" v-model="frmValue.password" required>
            
        </div>
        <div class="row">
            <div class="form-group col-md-6">
                <label class="form-label">Sexe : </label>
                <select class="form-control" v-model="frmValue.sexe" required>
                    <option v-for="(sexe, index) in sexes" :key="index">
                        {{ sexe }}
                    </option>
                </select>
            </div>
            <div class="form-group col-md-6">
                <label class="form-label">Date de naissance : </label>
                <input type="date" class="form-control" v-model="frmValue.dateNaiss" required> 
            </div>
        </div>
        <div class="form-group">
            <label class="form-label">Pays : </label>
            <select class="form-control" v-model="frmValue.pays" required>
                <option v-for="(pays, index) in countrys" :key="index">
                    {{ pays }}
                </option>
            </select>
        </div>
        <div  class="alert alert-success" role="alert" v-if="message" required>
            {{ message }}
        </div>
        <div  class="alert alert-danger" role="alert" v-if="error" required>
            {{ error }}
        </div>
        <div class="form-group text-center">
            <button type="submit" class="btn btn-success">
                S'enregistrer
            </button>
        </div>
    </form>
  </div>
</template>

<script>
export default {
    name: 'RegisterUserApp',
    data() {
        return {
            frmValue: {
                mail: '',
                name: '',
                firstname: '',
                password: '',
                sexe: '',
                dateNaiss: '',
                pays: '',
            },
            sexes: ['Homme', 'Femme', 'Autre'],
            countrys: [],
            message: '',
            error: ''
        }
    },
    mounted() {
        this.$axios.get(this.$apiCountry)
            .then((response) => {
                response.data.forEach((data) => {
                    this.countrys.push(data.name.common)
                })
            })
    }, 
    methods: {
        addUser(e) {
            e.preventDefault()
            this.$axios.post(`${this.$api}/user/insert`, this.frmValue)
                .then((response) => {
                    console.log(response.data)
                    if(response.data.success) {
                        this.message = response.data.message
                        this.$refs.frmResigter.reset()
                        setTimeout(() => {
                            this.$router.push({ path: '/login'})
                        }, 3000)
                    } else {
                        this.error = response.data.message
                    }
                })
        }
    }
}
</script>

<style>

</style>