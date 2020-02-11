<template>
    <div>
      <h1>{{categoryName}}</h1>

      <div class="song" v-for="song in songs" v-bind:key="song.title">
        <router-link :to="{name: 'song', params: {artist: song.artist, title: song.title, level: $route.params.level}}">
          <h2>{{song.title}}</h2>
          
          <h4>{{song.artist}}</h4>
        </router-link>
      </div>

    </div>
</template>


<script>
import NoPlpBackendApi from "@/utils/api/NoPlpBackendApi";

export default {
  name: 'Category',
  data() {
    return {
      categoryName: this.$route.params.category,
      songs: [],
    };
  },

  props: {
    
  },

  async created() {
    this.getSongs();
  },

  methods: {
    async getSongs() {
      let rsp = await NoPlpBackendApi.getSongsFromCategory(this.$route.params.category)
      console.log(rsp);
      this.songs = rsp.songs;
    }
  },

  computed: {
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

.song {
  border: 1px black solid;
  width: 50%;
  margin: 0 auto;
  margin-bottom: 50px;

}
</style>
