import Vue from 'vue'
import App from './index'

const app = new Vue(App)
app.$mount()

export default {
  config: {
    navigationBarTitleText: '书目详细',
    usingComponents: {
      'i-panel': '../../static/iview/panel/index',
      'i-button': '../../static/iview/button/index'
    }
  }
}
