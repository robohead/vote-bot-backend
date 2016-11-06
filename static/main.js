import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'

Vue.use(VueResource)

new Vue({
  el: '#app',
  data: {
      api: 'http://127.0.0.1:5000/api'
  },
  methods: {
      getAllVotes: function() {

          this.$http.get(this.api).then(function(response) {

              console.log(response)

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
