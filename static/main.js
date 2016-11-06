import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'

Vue.use(VueResource)

new Vue({
  el: '#app',
  data: {
      api: 'https://jsonplaceholder.typicode.com/posts'
  },
  methods: {
      getAllVotes: function() {

          this.$http.get(this.api).then(function(response) {

              console.log(response.body.data)

          }, function(error) {
            //   ошибка
          })

      }
  },
  created: function() {
      this.getAllVotes()
  },
  render: h => h(App)
})
