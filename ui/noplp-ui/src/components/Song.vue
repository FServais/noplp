<template>
  <div>
    <h1>{{title}}</h1>
    <h3>{{artist}}</h3>

    <h3>{{missing_lyrics.split(' ').length}} mots à trouver</h3>

    <h4>{{id}}</h4>

    <div
      class="lyrics"
      :class="{'missing': this.current_line == this.lyrics.length-1, 'validation': this.current_line == this.lyrics.length}"
      >
      {{currentLyric}}
    </div>

    <br>

    <div v-if="this.current_line < this.lyrics.length-1 && this.lyrics[this.current_line+1] === ''">
      {{this.getLyricForLine(this.current_line+1)}}
    </div>

    <div v-if="this.spotify_id !== ''">
      {{this.getLyricForLine(this.current_line+1)}}
    </div>

    <iframe :src="this.spotifyURL" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>

    <div class="footer">
      <md-button class="md-raised" v-if="this.current_line == this.lyrics.length - 1" v-on:click="() => this.display_initials = true">Initiales</md-button>
      <router-link :to="{name: 'round', params: {roundid: this.$route.query.round}}">
        <md-button class="md-raised">Retour</md-button>
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
      artist: this.$route.params.artist,
      title: this.$route.params.title,
      id: "",
      lyrics: [],
      missing_lyrics: "",
      display_initials: false,
      spotify_id: "",

      current_line: 0,
    };
  },

  props: {
  },

  async created() {
    this.getSong();
    this.loadSpotify();
  },

  mounted() {
    window.addEventListener("keydown", this.keyDown);
  },

  methods: {
    async getSong() {
      let rsp = await NoPlpBackendApi.getSong(this.$route.params.artist, this.$route.params.title, this.$route.params.level);
      console.log(rsp);
      this.lyrics = rsp.lyrics;
      this.missing_lyrics = rsp.missing_lyrics;
      this.id = rsp.id;
    },

    async loadSpotify() {
      let rsp = await NoPlpBackendApi.search(this.$route.params.artist, this.$route.params.title);
      console.log(rsp);
      this.spotify_id = rsp.id;
    },

    keyDown(e) {
      if (e.keyCode == 39 || e.keyCode == 32 || e.keyCode == 13) {
        // ArrowRight, space and enter
        this.nextLine();
      }
      if (e.keyCode == 37) {
        // ArrowLeft
        this.previousLine();
      }
    },

    nextLine() {
      if (this.current_line < this.lyrics.length) {
        this.current_line += 1;
      }
    },

    previousLine() {
      if (this.current_line > 0) {
        this.current_line -= 1;
      }
    },

    getLyricForLine(n) {
      if (n == this.lyrics.length) {
        return this.missing_lyrics;
      }

      if (n == this.lyrics.length - 1 && this.display_initials) {
        return this.displayInitials()
      }

      let l = this.lyrics[n];
      
      if (l === "") {
        return "[...]";
      }

      return l;
    },

    displayInitials() {
      let splittedLyrics = this.missing_lyrics.split(' ');

      let clue = [];
      for (let i = 0; i < splittedLyrics.length; i++) {
        const word = splittedLyrics[i];
        clue.push(word.charAt(0) + '_');
      }
      console.log(clue);
      return clue.join(' ');
    }
  },

  computed: {
    currentLyric() {      
      return this.getLyricForLine(this.current_line);
    },
    spotifyURL() {
      return "https://open.spotify.com/embed/track/" + this.spotify_id + "?utm_source=generator"
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

.lyrics {
  border: 2px gray solid;
  width: 70%;
  padding: 20px;
  margin: 0 auto;
  margin-top: 70px;
  font-size: 2em;
}

.missing {
  font-size: 3em;
}

.validation {
  color: green;
  font-weight: bold;
}
</style>
