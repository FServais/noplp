<template>
    <div>
      <h1>{{title}}</h1>
      <h3>{{artist}}</h3>

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
      lyrics: [],
      missing_lyrics: "",

      current_line: 0,
    };
  },

  props: {
    
  },

  async created() {
    this.getSong();
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

      let l = this.lyrics[n];
      
      if (l === "") {
        return "[...]";
      }

      return l;
    }
  },

  computed: {
    currentLyric() {      
      return this.getLyricForLine(this.current_line);
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
