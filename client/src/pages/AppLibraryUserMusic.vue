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
                <p>Durée : {{ dureeTotal }} - {{ nbTitre }} titres</p>
            </div>
        </div>
    </div>
    <div class="content-user-music p-4">
        <div class="content-user-music-header p-2">
            <div @click="handleModal" class="d-flex align-items-center" style="color: var(--primary); cursor: pointer;">
                <span class="material-symbols-outlined me-2">
                  add_circle
                </span>
                <span>Ajoutez une musique</span>
              </div>
        </div>
        <div class="table-responsive">
            <table class="table table-hover-test table-borderless ">
              <thead>
                <tr style="color: #fff;">
                  <th scope="col">#</th>
                  <th scope="col" style="width: 25%;">Titre</th>
                  <th scope="col" style="width: 50%;">Artiste</th>
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
                      <span @click="setCurrentMusic(music)"  class="material-symbols-outlined me-2 action-cursor">
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
    <div class="d-flex align-items-center justify-content-center flex-column" :hidden="stateMusic" v-if="currentMusic">
        <div class="audio-player-button p-4 d-flex flex-row align-items-center justify-content-between w-25">
            <span class="material-symbols-outlined" style="color: #fff;">
                skip_previous
            </span>
            <button @click="this.$refs.audio.play()" class="btn-play-pause d-flex align-items-center">
                <span class="material-symbols-outlined">
                    play_arrow
                </span>
            </button>
            <span class="material-symbols-outlined" style="color: #fff;">
                skip_next
            </span>
        </div>
        <div class="w-100 d-flex align-items-center justify-content-center flex-row">
            <span class="me-2" style="color: #fff;">{{ currentTimeProgressMusic }}</span>
            <div class="audio-player">

                <div class="audio-player__progress" :style="{ width: progress }"></div>
                <div class="audio-player__thumb" :style="{ left: progress }"></div>
                <audio ref="audio" :src="currentMusic" @timeupdate="updateProgress"></audio>
                
              </div>
              
            <span class="ms-2" style="color: #fff;">{{ currentTimeMusic }}</span>
        </div>
    </div>
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
            stateMusic: true,
            currentMusic: null,
            currentTimeMusic: '',
            currentTimeProgressMusic: '',
            progress: '0%',
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
    computed: {
        nbTitre() {
            return this.library.musics.length
        },
        dureeTotal() {
            const array = this.library.musics 
            var duree = 0
            array.forEach((music) => {
                duree+=music.duree
            })
            return this.convertDuree(duree)
        }
    },
    methods: {
        updateProgress() {
            try {
                const audio = this.$refs.audio;
                this.currentTimeProgressMusic = this.convertDuree(audio.currentTime)
                const progress = (audio.currentTime / audio.duration) * 100;
                this.progress = `${progress}%`;
            } catch(err) {
                console.log(err)
            }
        },
        setCurrentMusic(music) {
            this.stateMusic = false
            this.currentMusic = music.music 
            this.currentTimeMusic = this.convertDuree(music.duree)
        },
        convertDuree(duree) {
            const formattedDuration = new Date(duree * 1000).toISOString().substr(14, 5);
            
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

.btn-play-pause {
    border-radius: 50%;
    padding: 0.5rem;
    background-color: var(--primary);
    border: none;

    span {
        color: var(--dark);
    }
}

.audio-player {
    position: relative;
    width: 40%;
    height: 3px;
    background-color: #fff;

    .audio-player__progress {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        background-color: var(--primary);
        width: 0%;
    }
  
    .audio-player__thumb {
        position: absolute;
        top: -3.7px;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: var(--primary);
        
        cursor: pointer;
        transition: transform 0.1s ease-in-out;
    }
}
  
  

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