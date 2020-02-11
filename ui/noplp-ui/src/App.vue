<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" style="max-width: 300px;" >
    <router-view></router-view>
  </div>
</template>

<script>
import NoPlpBackendApi from "@/utils/api/NoPlpBackendApi";

export default {
  name: 'App',
  components: {
    
  },
  created() {
    if (!this.$route.params.roundid) {
      this.newRound();
    }
  },
  methods: {
    async newRound() {
      let rsp = await NoPlpBackendApi.newRound();
      this.$router.push({name: "round", params: {roundid: rsp.round.id}});
    } 
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
