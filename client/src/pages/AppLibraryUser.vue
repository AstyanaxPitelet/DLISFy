<template>
  <div class="app-content-library">
    <div class="page-infos align-items-center justify-content-between d-flex flas-row m-4">
      <div class="page-title">
        <h1>Bibliothèque</h1>
      </div>
      <div class="add-library">
        <div @click="handleModal" class="d-flex align-items-center justify-content-center" style="color: #fff; cursor: pointer;">
          <span class="material-symbols-outlined me-2">
            add_circle
          </span>
          <span>Créer une Playlist</span>
        </div>
      </div>
    </div>
    <div class="library-content d-flex flex-wrap">
      <div v-for="(lib, index) in user.librarys" :key="index">
        <router-link :to="getIdLib(lib.tempId)" class="card card-library" style="width: 13rem;">
          <img class="card-img-top" width="200" height="200" :src="lib.img" >
          <div class="card-body" style="color: #fff;">
            <h5 class="card-title">{{ lib.title }}</h5>
            <p class="card-text">Par : {{ lib.mail }}</p>
          </div> 
        </router-link>
      </div>
    </div>
    <app-new-library :user="user" :hidden="state" @changeState="handleCloseModal($event)"/>
  </div>
</template>

<script>
import user_mixin from "../mixins/user_mixin"
import AppNewLibrary from './AppNewLibrary.vue'
export default {
  components: { AppNewLibrary },
    name: 'AppLibraryUser',
    mixins: [user_mixin],
    data() {
      return {
        state: true,
      }
    }, 
    methods: {
      getIdLib(id) {
        return `/app/library/${id}`
      },
      handleModal() {
        this.state= false
      },
      handleCloseModal(state) {
        this.state=state
      }
    }
}
</script>

<style lang="scss">

.add-library a{
  text-decoration: none;
}

.library-content {
  padding: 1rem;



  .card-library {
    margin: 0.2em;
    border: 1px solid var(--dark);
    text-decoration: none;
    background-color: var(--dark);

  }
}



</style>