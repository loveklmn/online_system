import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    user_id: null,
    level: null
  },
  mutations: {
    setID (state, id) {
      state.user_id = id
    },
    setLevel (state, level) {
      state.level = level
    }
  }
})

export default store
