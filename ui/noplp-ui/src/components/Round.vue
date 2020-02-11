<template>
    <div>
        <h1>Catégories</h1>
        <div v-for="cat in categories_lvl" v-bind:key="cat.name">
          <h4><router-link :to="{name: 'category', params: {category: cat.name, level: cat.level}}">{{cat.name}} ({{cat.level}})</router-link></h4>
        </div>
        <div class="footer">
          <button>New round</button>
        </div>
    </div>
</template>


<script>
import NoPlpBackendApi from "@/utils/api/NoPlpBackendApi";

export default {
  name: 'Round',
  data() {
    return {
      categories: [],
    }
  },

  async created() {
    this.getRound();
  },

  methods: {
    async getRound() {
      let rsp = await NoPlpBackendApi.getRound(this.$route.params.roundid);
      this.categories = rsp.round.categories;
    }
  },

  computed: {
    categories_lvl() {
      let to_ret = [];
      let levels = ["50", "40", "30", "20", "10"];
      for (let i = 0; i < this.categories.length; i++) {
        const cat = this.categories[i];
        to_ret.push({name: cat, level: levels[i]});
      }

      return to_ret;
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
