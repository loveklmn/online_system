import Vue from 'vue'
import App from './App'
import store from '@/store/index'

Vue.config.productionTip = false
App.mpType = 'app'
Vue.prototype.$store = store
const app = new Vue(App)
app.$mount()

export default {
  // 这个字段走 app.json
  config: {
    // 页面前带有 ^ 符号的，会被编译成首页，其他页面可以选填，我们会自动把 webpack entry 里面的入口页面加进去
    pages: ['^pages/index/main'],
    window: {
      backgroundTextStyle: 'light',
      navigationBarBackgroundColor: '#fff',
      navigationBarTitleText: 'WeChat',
      navigationBarTextStyle: 'black'
    },
    tabBar: {
      'list': [
        {
          pagePath: 'pages/friendCircle/main',
          iconPath: '/static/images/friend-circle-default.png',
          selectedIconPath: '/static/images/friend-circle-active.png',
          text: '小伙伴'
        },
        {
          pagePath: 'pages/index/main',
          iconPath: '/static/images/main-default.png',
          selectedIconPath: '/static/images/main-active.png',
          text: '小英语'
        },
        {
          pagePath: 'pages/aboutMe/main',
          iconPath: '/static/images/about-me-default.png',
          selectedIconPath: '/static/images/about-me-active.png',
          text: '关于我'
        }
      ],
      'selectedColor': '#999'
    }
  }
}
