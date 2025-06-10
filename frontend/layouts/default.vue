
<template>
    <!--the name layouts/default.vue is special not arbitrary-->

    <navbar-nav/>

    <!-- Page Content -->
    <main class="min-vh-100 bg-dark">
      <slot />
    </main>

    <FooterComp/>

</template>



<script>
import FooterComp from '~/components/FooterComp.vue';
import NavbarNav from '~/components/NavbarNav.vue';

export default{

    components: {NavbarNav, FooterComp}
}
</script>



