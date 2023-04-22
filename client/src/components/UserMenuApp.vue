<template>
    <nav class="navbar navbar-user">
        <div class="d-flex justify-content-end w-100">
            <a class="text-right w" href="/profil">
                {{ user.name }} - {{ user.firstname }}
            </a>
        </div>
      </nav>
</template>

<script>
export default {
    name: 'UserMenuApp',
    props: {
        user: Object
    }
}
</script>

<style lang="scss">
.navbar-user {
    background-color: var(--dark);
   
    a {
        text-decoration: none;
        color: #fff;
        font-family: var(--font-user);
        padding: 0.5rem;
        margin: 1rem;
        margin-right: 5rem;
        transition: 0.5s ease;
        background-color: var(--dark-old);
        border-radius: 20px;
        border: 1px solid var(--dark-old);

        &:hover {
          border: 1px solid var(--primary);
        }
      }
}
</style>