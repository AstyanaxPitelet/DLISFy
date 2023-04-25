<template>
  <div class="modal-page-add p-4">
    <div class="page-infos align-items-center justify-content-between d-flex flas-row">
        <div class="page-title">
          <h1>Nouvelle Musique</h1>
        </div>
        <div class="add-library">
          <div @click="handleClose" class="d-flex align-items-center justify-content-center" style="color: #fff; cursor: pointer;">
            <span class="material-symbols-outlined me-2">
              close
            </span>
          </div>
        </div>
      </div>
    <form @submit="e => addMusic(e)" ref="frmLib" >
        <div class="form-group m-1">
            <label class="form-label" style="color: #fff">Titre de la musique</label>
            <input type="text" v-model="frmValue.title"  class="form-control" >
        </div>
        <div class="form-group m-1">
            <label class="form-label" style="color: #fff">Artiste</label>
            <input type="text" v-model="frmValue.artiste"  class="form-control" >
        </div>
        <div class="form-group m-1">
          <label class="form-label" style="color: #fff">Votre musique</label>
          <input type="file" @change="e => onFileChange(e)"  class="form-control" accept=".mp3, .mp4">
        </div>
        <div class="text-center m-2">
            <button class="btn btn-success">
                Ajoutez
            </button>
        </div>
    </form>
  </div>
</template>

<script>
export default {
    name: 'AppNewMusic',
    props: {
        lib: Object
    },
    data() {
      return {
        frmValue: {
          tempId: '',
          title: '',
          artiste: '',
          duree: '',
          music: ''
        }
      }
    },
    methods: {
      getDuration(fileaudio) {
        return new Promise((resolve, reject) => {
                const audio = new Audio(fileaudio)
                audio.onloadedmetadata = () => {
                    resolve(audio.duration)
                }
                audio.onerror = (error) => {
                    reject(error)
                }
            })
      },
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
        const duration = await this.getDuration(base64)
        this.frmValue.music = base64
        this.frmValue.duree = duration
      },
      addMusic(e) {
        e.preventDefault()
        this.frmValue.tempId = Date.now()
        const id = this.$props.lib.tempId
        console.log(id)
        this.$axios.put(`${this.$api}/music/insert/${id}`, this.frmValue)
          .then((response) => {
            console.log(response)
          })
      },
      handleClose() {
          this.$emit('changeState', true)
      }
    }
}
</script>

<style>

</style>