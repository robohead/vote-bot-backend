<template>
  <div id="app">
      <list :votes='this.votes'></list>
  </div>
</template>

<script>
import List from './../components/List.vue'

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to VoteBot page',
      api: 'http://127.0.0.1:5000/api',
      votes: []
    }
  },
  methods: {
      getAllVotes: function() {

          this.$http.get(this.api).then(function(response) {
              console.log(response)

              this.votes = response.body.data

          }, function(error) {
            //   ошибка
          })

      }
  },
  created: function() {
      this.getAllVotes()
  },
  components: {
      List
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
