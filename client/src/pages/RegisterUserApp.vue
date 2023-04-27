<template>
  <div style="background-color: var(--dark-old)" class="d-flex justify-content-center align-items-center vh-100 flex-column">
    <form ref="frmResigter" class="row form-app w-25 p-3"  @submit="e => addUser(e)">
        <div class="text-center">
            <h1>Inscription</h1>
        </div>
        <div class="form-group">
            <label class="form-label">NOM</label>
            <input type="text"  class="form-control" v-model="frmValue.name" required>
        </div>
        <div class="form-group">
            <label class="form-label">PRENOM</label>
            <input type="text" class="form-control" v-model="frmValue.firstname" required>
        </div>
        <div class="form-group">
            <label class="form-label">ADRESSE MAIL</label>
            <input type="email" class="form-control" v-model="frmValue.mail" required>
        </div>
        <div class="form-group">
            <label class="form-label">MOT DE PASSE</label>
            <input type="password" class="form-control" v-model="frmValue.password" required>  
        </div>
        <div class="form-group">
            <label class="form-label">SEXE</label>
            <select class="form-control" v-model="frmValue.sexe" required>
                <option v-for="(sexe, index) in sexes" :key="index">
                    {{ sexe }}
                </option>
            </select>
        </div>
        <div class="form-group">
            <label class="form-label">DATE DE NAISSANCE</label>
            <input type="date" class="form-control" v-model="frmValue.dateNaiss" required> 
        </div>
        <div class="form-group">
            <label class="form-label">PAYS</label>
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
        <div class="form-group text-center mt-1">
            <button type="submit" class="btn btn-success  w-100">
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

<style lang="scss">
.form-app {
    background-color: #fff;
    border-radius: 20px;

    > div {

        h1 {
            font-family: var(--font-user);
            font-weight: bold;
            text-transform: uppercase;
        }

        margin-bottom: 1rem;

        input, select {
            border: none;
            border-bottom: 2px solid var(--primary);
            border-radius: 0%;
            transition: 0.2s ease;

            &:focus {
                outline: none !important;
                box-shadow: none;
                border-bottom: 2px solid var(--dark-old);
            }
        }

    }
}
</style>
