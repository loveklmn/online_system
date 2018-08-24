import Vue from 'vue'
import App from './index'

const app = new Vue(App)
app.$mount()

export default {
  config: {
    'navigationBarTitleText': '个人信息',
    usingComponents: {
      'i-cell-group': '../../static/iview/cell-group/index',
      'i-cell': '../../static/iview/cell/index',
      'i-panel': '../../static/iview/panel/index',
      'i-card': '../../static/iview/card/index',
      'i-icon': '../../static/iview/icon/index',
      'i-button': '../../static/iview/button/index'
    }
  }
}
