import Vue from 'vue'
import App from './index'

const app = new Vue(App)
app.$mount()

export default {
  config: {
    'navigationBarTitleText': '等级介绍',
    usingComponents: {
      'i-switch': '../../static/iview/switch/index',
      'i-panel': '../../static/iview/panel/index',
      'i-cell': '../../static/iview/cell/index',
      'i-button': '../../static/iview/button/index'
    }
  }
}
