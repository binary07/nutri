<template>
	<div v-if="$route.meta.isPublic">
    <Header/>
    <div id="main">
      <router-view/>
    </div>

  </div>
  <!-- si esta autenticado -->
  <div v-else>
    <HomeComponent />
  </div>
</template>


<script>

    import HomeComponent from '@/components/Dashboard.vue';
    import Header from '@/components/layout/inicio/header.vue';

    export default {
      name: "Inicio",
      components: {HomeComponent, Header},
      data () {
        return {
          msj: 'Welcome to Your Vue.js App',
        }
      },
    };
</script>