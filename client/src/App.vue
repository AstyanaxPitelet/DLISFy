<template>
  <div class="app">
    <div class="app-main">
      <router-view />
    </div>
  </div>
</template>

<script>



export default {
  name: 'App',
  
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@100&display=swap');

:root {
  --dark-old: #161718;
  --dark: #0C0D0D;
  --primary: #22c55e;
  --font-link: 'Raleway', sans-serif;
  --font-user: 'Quicksand', sans-serif;
}




</style>
