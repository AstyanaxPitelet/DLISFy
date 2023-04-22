<template>
  <aside class="d-flex flex-column align-items-center justify-content-between">
    <div class="app-logo mt-3">
      <h1>Mon logo</h1>
    </div>
    <div class="app-menu d-flex align-items-center justify-content-between h-25 flex-column">
      <menu-link-app path="/app" icon="home" title="Accueil" />
      <menu-link-app path="/app/library" icon="library_music" title="Bibliothèque" />
      <menu-link-app path="/app/profil" icon="person" title="Profil" />
    </div>
    <div class="app-menu-logout mb-3">
      <logout-app />
    </div>
  </aside>
</template>

<script>
import LogoutApp from './LogoutApp.vue'
import MenuLinkApp from './MenuLinkApp.vue'
export default {
  components: { LogoutApp, MenuLinkApp },
    name: 'SideBarMenuApp'
}
</script>

<style lang="scss" scoped>
aside {
  height: 100vh;
  width: 15%;
  background: var(--dark);
  min-width: 15%;
  max-width: 15%;
  
}
</style>