<template>
  <div class="app-music d-flex flex-row w-100">
    <side-bar-menu-app />
    <main class="d-flex flex-column">
      <user-menu-app :user="user"/>
      <router-view class="app-content"/>
    </main>
  </div>
</template>

<script>
import SideBarMenuApp from '@/components/SideBarMenuApp.vue'
import user_mixin from "../mixins/user_mixin"
import UserMenuApp from '@/components/UserMenuApp.vue'

export default {
    name: 'AppMusic',
    mixins: [user_mixin],
    components: {SideBarMenuApp, UserMenuApp}
}
</script>

<style lang="scss">
main {
  width: 90%;

  .app-content {
    background: var(--dark-old);
    height: 90.8vh;
  }
}
</style>