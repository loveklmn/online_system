import Vue from 'vue'
import App from './index'

const app = new Vue(App)
app.$mount()

export default {
  config: {
    usingComponents: {
      'i-modal': '../../static/iview/modal/index',
      'i-grid': '../../static/iview/grid/index',
      'i-grid-item': '../../static/iview/grid-item/index',
      'i-cell-group': '../../static/iview/cell-group/index',
      'i-cell': '../../static/iview/cell/index',
      'i-panel': '../../static/iview/panel/index',
      'i-card': '../../static/iview/card/index',
      'i-icon': '../../static/iview/icon/index'
    }
  }
}
