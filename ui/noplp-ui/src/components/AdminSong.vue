<template>
    <div>
      <h1>{{title}} - {{artist}}</h1>

      <div class="md-layout">
        <div class="md-layout-item md-size-99">
          <div v-html="fullLyrics" class="fulllyrics"></div>
            <br>
          <div class="missinglyric">{{missing_lyrics}}</div>
        </div>

        <!-- <div class="md-layout-item md-size-99" v-if="tab">
          <iframe :src="tab" frameborder="0" style="height: 100%; width: 100%"></iframe>
        </div> -->
      </div>
      <!-- {{fullLyrics}} -->
      

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
      missing_lyrics: "",
      tab: ""
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
      this.tab = rsp.tab;
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
.md-layout-item iframe .tabframe {
  height: 600px;
}
</style>
