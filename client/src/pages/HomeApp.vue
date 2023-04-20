<template>
  <div>
    <h1>Hello {{ user.mail }} </h1>
    <logout-app />
  </div>
</template>

<script>
import LogoutApp from "../components/LogoutApp.vue"
import user_mixin from "@/mixins/user_mixin"

export default {
    name: 'HomeApp',
    components: { LogoutApp },
    mixins: [user_mixin],
}
</script>

<style>

</style>