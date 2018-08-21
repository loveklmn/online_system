import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    token: ''
  },
  mutations: {
    setToken (state, token) {
      wx.setStorageSync('token', token)
      state.token = token
    }
  },
  getters: {
    token: (state) => {
      let token = state.token || wx.getStorageSync('token')
      return token
    }
  }
})

export default store
