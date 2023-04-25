<template>
  <div class="modal-page-add p-4">
    <div class="page-infos align-items-center justify-content-between d-flex flas-row">
        <div class="page-title">
          <h1>Nouvelle Playlist</h1>
        </div>
        <div class="add-library">
          <div @click="handleClose" class="d-flex align-items-center justify-content-center" style="color: #fff; cursor: pointer;">
            <span class="material-symbols-outlined me-2">
              close
            </span>
          </div>
        </div>
      </div>
    <form  ref="frmMusic" >
        <div class="form-group m-1">
            <label class="form-label" style="color: #fff">Titre de la Playlist</label>
            <input type="text" v-model="frmValue.title" class="form-control" >
        </div>
        <div class="form-group m-1 mt-4">
            <label class="form-label" style="color: #fff">Image de la Playlist</label>
            <input type="file" @change="e => onFileChange(e)" class="form-control" accept=".jpeg, .png, .jpg">
        </div>
        <div class="text-center m-2">
            <button class="btn btn-success">
                Créer 
            </button>
        </div>
    </form>
  </div>
</template>

<script>

export default {
    name: 'AppNewLibrary',
    props: {
        user: Object
    },
    data() {
        return {
            frmValue: {
                tempId: '',
                title: '',
                img: '',
                mail: ''
            },
        }
    }, 
    methods: {
        convertToBase64(file) {
            return new Promise((resolve, reject) => {
                const filereader = new FileReader()
                filereader.readAsDataURL(file)
                filereader.onload = () => {
                    resolve(filereader.result)
                }
                filereader.onerror = (error) => {
                    reject(error)
                }
            })
        },
        async onFileChange(e) {
            const file = e.target.files[0]
            const base64 = await this.convertToBase64(file)
            this.frmValue.img = base64
        }, 
        addLibrary(e) {
            e.preventDefault()
            this.frmValue.tempId = Date.now()
            this.frmValue.mail = this.$props.user.mail
            this.$axios.put(`${this.$api}/lib/insert`, this.frmValue)
                .then((response) => {
                    if(response.status === 200) {
                        this.$refs.frmLib.reset()
                        window.location.reload()
                    }
                })
        },
        handleClose() {
            this.$emit('changeState', true)
        }
    }
}
</script>

<style lang="scss">
.modal-page-add {
    position: fixed;
    width: 30rem;
    top: 12%;
    left: 43%;
    background: var(--dark);
    border: 1px solid var(--primary);
    border-radius: 15px;
    animation-name: animatetop;
    animation-duration: 0.4s;
    box-shadow: 0px 0px 7px 0px #000000;
}

@keyframes animatetop {
    from {top: -300px; opacity: 0}
    to {top: 110px; opacity: 1}
  }
</style>