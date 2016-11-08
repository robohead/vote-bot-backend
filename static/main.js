import Vue from 'vue'
import App from './App.vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.css'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(VueMaterial)

Vue.material.theme.register('default', {
  primary: 'cyan',
  accent: 'pink'
})

new Vue({
  el: '#app',
  data: {
  },
  render: h => h(App)
})
