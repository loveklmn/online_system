import store from '@/store/index'

class Request {
  constructor (parms) {
    this.withBaseURL = parms.withBaseURL
    this.baseURL = parms.baseURL
    this.header = parms.header
  }
  get (url, data) {
    return this.request('GET', url, data)
  }
  post (url, data) {
    return this.request('POST', url, data)
  }
  put (url, data) {
    return this.request('PUT', url, data)
  }
  request (method, url, data) {
    const vm = this
    let theHeader = this.header
    if (store.state.token) {
      theHeader.Authorization = 'Token ' + store.state.token
    }
    return new Promise((resolve, reject) => {
      wx.request({
        url: vm.withBaseURL ? vm.baseURL + url : url,
        data,
        method,
        header: theHeader,
        success (res) {
          resolve(res)
        },
        fail () {
          reject(new Error({
            msg: '请求失败',
            url: vm.withBaseURL ? vm.baseURL + url : url,
            method,
            data
          }))
        }
      })
    })
  }
}

export default new Request({
  baseURL: 'http://192.168.55.33:8000/vron',
  withBaseURL: true,
  header: {
    'content-type': 'application/x-www-form-urlencoded'
  }
})
