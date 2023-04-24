<template>
  <div>
    <h1>Profil for : {{ user.mail }}</h1>
  </div>
</template>

<script>
import user_mixin from "../mixins/user_mixin"
export default {
    name: 'AppProfilUser',
    mixins: [user_mixin],
}
</script>

<style>

</style>