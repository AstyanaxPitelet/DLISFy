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
            <table class="table table-borderless">
              <thead>
                <tr style="color: #fff;">
                  <th scope="col">#</th>
                  <th scope="col" style="width: 25%;">Titre</th>
                  <th scope="col" style="width: 50%;">Artiste</th>
                  <th scope="col">
                    <span class="material-symbols-outlined ">
                        schedule
                    </span>
                  </th>
                  <th scope="col">
                    Action
                  </th>
                </tr>
              </thead>
              <tbody ref="tBody">
                <tr v-for="(music, index) in library.musics" @mouseover="handleHover(index)" @mouseleave="isNotHover(index)" :id="index" :key="index" style="color: #fff;">
                    <th >
                        <span @click="setCurrentMusic(music, index)" style="cursor: pointer; max-width: 5px">{{ index+1 }}</span>
                    </th>
                    <td><span>{{ music.title }}</span></td>
                    <td><span>{{ music.artiste }}</span></td>
                    <td>
                        <span >{{ convertDuree(music.duree) }}</span>
                    </td>
                    <td>
                        <span style="cursor: pointer;" class="material-symbols-outlined">
                            remove
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
            <span @click="previousMusic" class="material-symbols-outlined" style="color: #fff; cursor: pointer;">
                skip_previous
            </span>
            <button @click="this.$refs.audio.play()" class="btn-play-pause d-flex align-items-center">
                <span class="material-symbols-outlined">
                    play_arrow
                </span>
            </button>
            <button @click="this.$refs.audio.pause()" class="btn-play-pause d-flex align-items-center">
                <span class="material-symbols-outlined">
                    pause
                </span>
            </button>
            <span @click="nextMusic" class="material-symbols-outlined" style="color: #fff; cursor: pointer;">
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
            isHoverPlay: false,
            actualIndex: null,
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
        },
        isIcon() {
            return this.playOrNot.isIcon ? 'material-symbols-outlined' : ''
        },
    },
    methods: {
        handleHover(index) {
            this.$refs.tBody.childNodes.forEach((tr) => {
                if(tr.id) {
                    if(parseInt(tr.id) === index) {
                        tr.childNodes[0].children[0].innerText = 'play_arrow'
                        tr.childNodes[0].children[0].classList.add('material-symbols-outlined')
                    }
                }
            })
        },
        isNotHover(index) {
            this.$refs.tBody.childNodes.forEach((tr) => {
                if(tr.id) {
                    if(parseInt(tr.id) === index) {
                        tr.childNodes[0].children[0].innerText = index+1
                        tr.childNodes[0].children[0].classList.remove('material-symbols-outlined')
                    }
                }
            })
        },
        previousMusic() {
            this.setCurrentMusic(this.library.musics.find((music, index) => index < this.actualIndex))
        },
        nextMusic() {
            this.setCurrentMusic(this.library.musics.find((music, index) => index > this.actualIndex))
        },
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
        setCurrentMusic(music, index) {
            this.actualIndex = index
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

tbody tr {
    width: 100%;
    transition: 0.2s ease;
    &:hover  {
        background-color: #2a2a2a;
    }
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