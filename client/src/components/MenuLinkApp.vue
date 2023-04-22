<template>
    <div class="app-menu-link w-100">
        <router-link :to="path" class="d-flex flex-row align-items-center">
          <span class="material-symbols-outlined me-3">
            {{ icon }}
          </span>
          <span>{{ title }}</span>
        </router-link>
      </div>
</template>

<script>
export default {
    name: 'MenuLinkApp',
    props: {
        path: String,
        title: String,
        icon: String
    }
}
</script>

<style lang="scss">
.app-menu-link {
  a {
    padding: 1rem;
    text-decoration: none;
    color: #fff;
    font-family: var(--font-user);
    font-size: 18px;
    transition: 0.2s ease;

    &:hover {
      font-weight: bold;
    }
  }
}
</style>