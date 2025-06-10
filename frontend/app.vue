<template>

    <navbar-nav/>

    <main class="container-fluid py-5 bg-black overflow-x-hidden" style="min-height: 100vh; width: 100%;">
      <NuxtPage />
    </main>


</template>


<script>
import NavbarNav from './components/NavbarNav.vue';


export default{
  components : {NavbarNav}
}
</script>