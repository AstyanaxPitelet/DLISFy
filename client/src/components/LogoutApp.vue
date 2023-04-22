<template>
  <div class="logout-button">
    
    <button @click="logout" class="d-flex flex-row align-items-center">
      <span class="material-symbols-outlined me-2">
        logout
      </span>
      <span>
        Déconnexion
      </span>
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

<style lang="scss">
.logout-button {
  button {
    padding: 1rem;
    font-family: var(--font-link);
    background: var(--dark-old);
    border: 1px solid var(--dark-old);
    color: #fff;
    border-radius: 20px;
    font-size: 20px;
    transition: 0.2s ease;

    &:hover {
      border: 1px solid var(--primary);
    }
  }
  
  
}
</style>