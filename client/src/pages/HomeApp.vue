<template>
  <main class="vh-100 d-flex flex-row ">
    <div class="vh-100 w-25 menu-login">
      <div class="box-menu-login d-flex flex-column justify-content-center align-items-center vh-100">
        <div class="title-app text-center">
          <h1>DLISFy</h1>
        </div>
        <div class="p-4 box-menu-login-content d-flex flex-column">
          <a href="/login">Connexion</a>
          <a href="/register">Inscription</a>
        </div>
      </div>
    </div>
    <div class="w-75 app-acc d-flex justify-content-center align-items-center">
      <img class="rotate-img"  src="../../public/img/disk-gde1ea9809_1920.png" alt="">
    </div>
  </main>
</template>

<script>

export default {
    name: 'HomeApp',
}
</script>

<style lang="scss">
.menu-login {
  background-color: var(--dark);

  .title-app {
    margin-top: 1rem;
    h1 {
      color: var(--primary);
      font-family: var(--font-link);
      font-weight: bold;
    }
  }

  .box-menu-login {
    .box-menu-login-content {


      a {
        text-decoration: none;
        color: #fff;
        font-family: var(--font-link);
        font-size: 40px;
        padding: 1rem;
        margin: 1rem;
        transition: 0.5s ease;
        background-color: var(--dark-old);
        border-radius: 20px;
        border: 1px solid var(--dark-old);

        &:hover {
          border: 1px solid var(--primary);
        }
      }
    }
  }
}

@keyframes circle {
  from { transform:rotate(0deg); }
  to { transform:rotate(360deg); }
}

.app-acc {
  background: var(--dark-old);
}

.rotate-img {
  animation: circle 5s linear infinite;
  width: 70vh;
    
}
</style>