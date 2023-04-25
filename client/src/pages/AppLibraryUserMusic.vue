<template>
  <div v-if="library" class="app-content user-music">
    <div class="header-user-music d-flex flex-row  p-4">
        <div class="header-user-music-img">
            <img :src="library.img" alt="" width="250" height="250">
        </div>
        <div class="header-user-music-content ms-5 d-flex flex-column justify-content-between">
            <div class="header-title">
                <h1>{{ library.title }}</h1>
            </div>
            <div class="header-time-creator">
                <p>Conçu par {{ library.mail }}</p>
                <p>Durée : {{ dureeTotal }} - {{ library.musics.length }} titres</p>
            </div>
        </div>
    </div>
    <div class="content-user-music p-4">
        <div class="content-user-music-header p-2">
            <div @click="handleModal" class="d-flex align-items-center" style="color: var(--primary); cursor: pointer;">
                <span class="material-symbols-outlined me-2">
                  add_circle
                </span>
                <span>Créer une Playlist</span>
              </div>
        </div>
        <div class="table-responsive">
            <table class="table table-hover-test table-borderless ">
              <thead>
                <tr style="color: #fff;">
                  <th scope="col">#</th>
                  <th scope="col">Titre</th>
                  <th scope="col">Artiste</th>
                  <th scope="col">
                    <span class="material-symbols-outlined">
                        schedule
                        </span>
                  </th>
                  <th scope="col">Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(music, index) in library.musics" :key="index" style="color: #fff;">
                    <th scope="row">{{ index+1 }}</th>
                    <td>{{ music.title }}</td>
                    <td>{{ music.artiste }}</td>
                    <td>{{ convertDuree(music.duree) }}</td>
                    <td>
                        <audio controls>
                            <source :src="music.music" />
                        </audio>
                    </td>
                    <td>
                      <span class="material-symbols-outlined me-2 action-cursor">
                          play_arrow
                      </span>
                      <span class="material-symbols-outlined ms-2 action-cursor">
                          delete
                      </span>
                    </td>
                </tr>
                
              </tbody>
          
            </table>
          </div>
    </div>
    <app-new-music :lib="library" :hidden="state" @changeState="handleCloseModal($event)"/>
  </div>
</template>

<script>
import AppNewMusic from './AppNewMusic.vue'

export default {
    name: 'AppLibraryUserMusic',
    components: {
        AppNewMusic
    },
    data() {
        return {
            library: null,
            state: true,
            dureeTotal: 0,
            nbTitre: 0
        }
    },
    mounted() {
        const id = this.$route.params.id
        this.$axios.get(`${this.$api}/lib/${id}`)
            .then((response) => {
                if(response.status === 200) {
                    this.library = response.data
                }
            }).catch(err => {
                console.log(err)
            }) 
    },
    methods: {
        convertDuree(duree) {
            const formattedDuration = new Date(duree * 1000).toISOString().substr(14, 5);
            this.dureeTotal = formattedDuration
            return formattedDuration
        },
        handleModal() {
            this.state = false
        },
        handleCloseModal(state) {
            this.state = state
        }
    }
}
</script>

<style lang="scss">
.action-cursor {
    cursor: pointer;
}

.table-hover-test tbody tr:hover  {
    background-color: #2a2a2a;
}

.header-user-music {
    background: var(--primary);

    .header-user-music-img {
        img {
            box-shadow: 0px 0px 15px 0px #000000;
        }
    }
    
    .header-user-music-content {
        height: 250px;
    
        > div {
            color: #fff;
    
            h1 {
                font-size: 6rem;
            }
    
            p {
                font-family: var(--font-user);
                font-weight: bold;
            }
        }
    }
}


</style>