import Vue from 'vue'
import App from './index'

const app = new Vue(App)
app.$mount()

export default {
  config: {
    usingComponents: {
      'i-button': '../../static/iview/button/index',
      'i-alert': '../../static/iview/alert/index'
    }
  }
}
