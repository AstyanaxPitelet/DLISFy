<template>
  <div class="app-music d-flex flex-row w-100">
    <side-bar-menu-app />
    <main class="d-flex flex-column">
      <user-menu-app :user="user"/>
      <div class="app-content">
        <h1>Hello {{ user.mail }}</h1>
      </div>
    </main>
  </div>
</template>

<script>
import SideBarMenuApp from '@/components/SideBarMenuApp.vue'
import user_mixin from "../mixins/user_mixin"
import UserMenuApp from '@/components/UserMenuApp.vue'

export default {
    name: 'AppMusicHome',
    mixins: [user_mixin],
    components: {SideBarMenuApp, UserMenuApp}
}
</script>

<style lang="scss">
main {
  width: 90%;

}
</style>