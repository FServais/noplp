<template>
    <div>
      <h1>{{title}} - {{artist}}</h1>

      <!-- {{fullLyrics}} -->
      <div v-html="fullLyrics" class="fulllyrics"></div>
      <br>
      <div class="missinglyric">{{missing_lyrics}}</div>

      <br>

      <div class="footer">
        <md-button class="md-raised" v-if="this.current_line == this.lyrics.length - 1" v-on:click="() => this.display_initials = true">Initiales</md-button>
        <router-link :to="{name: 'admin'}">
          <md-button class="md-raised">Retour</md-button>
        </router-link>
      </div>
    </div>
</template>


<script>
import NoPlpBackendApi from "@/utils/api/NoPlpBackendApi";

export default {
  name: 'AdminSong',
  data() {
    return {
      challengeid: this.$route.params.challengeid,
      title: "",
      artist: "",
      lyrics: [],
      missing_lyrics: ""
    };
  },

  props: {
    
  },

  async created() {
    this.getAdminSong();
  },

  methods: {
    async getAdminSong() {
      let rsp = await NoPlpBackendApi.getAdminSong(this.$route.params.challengeid);
      console.log(rsp);
      this.title = rsp.title;
      this.artist = rsp.artist;
      this.lyrics = rsp.lyrics;
      this.missing_lyrics = rsp.missing_lyrics;
    }
  },

  computed: {
    fullLyrics() {
      return this.lyrics.join('<br>');
    }
  },
}
</script>

<style>
.fulllyrics {
  font-size: 1.2em;
  line-height: 1.9;
}
.missinglyric {
  font-size: 1.2em;
  color: forestgreen;
}
</style>
