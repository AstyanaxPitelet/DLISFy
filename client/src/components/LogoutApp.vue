<template>
  <div>
    <button @click="logout">
        Logout
    </button>
  </div>
</template>

<script>

import { accountService } from '@/service';

export default {
    name: 'LogoutApp',
    methods: {
        logout() {
            accountService.logout()
            this.$router.push('/login')
        }
    }
}
</script>

<style>

</style>