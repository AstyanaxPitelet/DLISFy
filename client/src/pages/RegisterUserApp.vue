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
            <input type="email" class="form-control" v-model="frmValue.mail" required>
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
        <div class="mt-2 mb-2" v-if="message || error"> 
            <div :class="setAlert" role="alert" required>
                {{ setInfo }}
            </div>
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
            error: '',
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
    computed: {
        setAlert() {
            return this.message ? 'alert alert-success' : 'alert alert-danger'
        },
        setInfo() {
            return this.message ? this.message : this.error
        }
    },
    methods: {
        addUser(e) {
            e.preventDefault()
            this.$axios.post(`${this.$api}/user/insert`, this.frmValue)
                .then((response) => {
                    if(response.status === 201) {
                        this.message = response.data.detail
                        this.$refs.frmResigter.reset()
                        setTimeout(() => {
                            this.$router.push({ path: '/login'})
                        }, 3000)
                    }
                }).catch(err => {
                    this.error = err.response.data.detail
                })
        }
    }
}
</script>

<style>

</style>