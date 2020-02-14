<template>
    <div>
      <h1>Admin panel</h1>

      <form novalidate class="md-layout">
      <md-card class="md-layout-item md-size-20 md-small-size-100">
        <md-card-header>
          <div class="md-title">Songs</div>
        </md-card-header>

        <md-card-content>
          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
              <md-field>
                <label for="first-name">Song ID</label>
                <md-input name="first-name" id="first-name" v-model="songid" />
              </md-field>
            </div>
          </div>
        </md-card-content>
        <md-card-actions>
          <md-button v-on:click="gotosong" class="md-primary">Go to song</md-button>
        </md-card-actions>
      </md-card>
    </form>
    </div>
</template>


<script>

export default {
  name: 'Admin',
  data() {
    return {
      songid: ""
    };
  },

  props: {
    
  },

  async created() {
  },

  methods: {
    gotosong() {
      this.$router.push({name: "adminsong", params: {challengeid: this.songid}});
    }
  },

  computed: {
    
  },
}
</script>

<style>
.form {
  margin: auto;
  width: 400px;
}
</style>
