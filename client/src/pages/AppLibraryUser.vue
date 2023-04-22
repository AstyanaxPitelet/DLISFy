<template>
  <div>
    <h1>Library for : {{ user.mail }}</h1>
  </div>
</template>

<script>
import user_mixin from "../mixins/user_mixin"
export default {
    name: 'AppLibraryUser',
    mixins: [user_mixin],
}
</script>

<style>

</style>