<template>
    <div>
      <h1>{{decodeURIComponent(categoryName)}}</h1>

      <div class="song" v-for="song in songs" v-bind:key="song.title">
        <router-link :to="{name: 'song', params: {artist: song.artist, title: song.title, level: $route.params.level}, query: {round: $route.query.round}}">
          <h2>{{song.title}}</h2>
          
          <h4>{{song.artist}}</h4>
        </router-link>
      </div>

      <router-link :to="{name: 'round', params: {roundid: this.$route.query.round}}">
        <md-button class="md-raised">Retour</md-button>
      </router-link>

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
.song {
  border: 1px black solid;
  width: 50%;
  margin: 0 auto;
  margin-top: 50px;

}
</style>
