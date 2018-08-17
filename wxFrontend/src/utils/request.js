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
  upload (file) {
    const vm = this
    let theHeader = this.header
    if (store.state.token) {
      theHeader.Authorization = 'Token ' + store.state.token
    }
    return new Promise((resolve, reject) => {
      wx.uploadFile({
        url: vm.baseURL + 'upload/',
        filePath: file,
        header: theHeader,
        name: 'file',
        success (res) {
          let data = JSON.parse(res.data)
          resolve(data.savepath)
        },
        fail () {
          reject(new Error('upload error'))
        }
      })
    })
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
          console.log('request failed')
          reject(new Error('request faild'))
        }
      })
    })
  }
}

export default new Request({
  baseURL: 'http://101.200.62.189:8000/vron/',
  withBaseURL: true,
  header: {
    'content-type': 'application/x-www-form-urlencoded'
  }
})
