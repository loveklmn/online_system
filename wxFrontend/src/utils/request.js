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
  validateToken () {
    let token = store.getters.token
    if (!token) {
      delete this.header.Authorization
      wx.reLaunch({url: '/pages/login/main'})
      return false
    } else {
      this.header.Authorization = 'Token ' + token
      return true
    }
  }
  login (username, password) {
    let url = this.baseURL + 'get-token/'
    let vm = this
    return new Promise((resolve, reject) => {
      wx.request({
        url: url,
        data: {
          username: username,
          password: password
        },
        method: 'POST',
        header: vm.header,
        success (res) {
          if (res.statusCode === 200 && res.data.token) {
            store.commit('setToken', res.data.token)
            resolve(0)
          } else {
            reject(new Error('用户名或密码错误'))
          }
        },
        fail () {
          reject(new Error('网络错误'))
        }
      })
    })
  }
  register (username, password, key) {
    let url = this.baseURL + 'register/'
    let vm = this
    return new Promise((resolve, reject) => {
      wx.request({
        url: url,
        data: {
          username: username,
          password: password,
          key: key
        },
        method: 'POST',
        header: vm.header,
        success (res) {
          if (res.statusCode === 201) {
            resolve(res)
          } else {
            reject(new Error(res.data.msg))
          }
        },
        fail () {
          reject(new Error('网络错误'))
        }
      })
    })
  }
  upload (file) {
    const vm = this
    return new Promise((resolve, reject) => {
      if (this.validateToken() === false) {
        reject(new Error(-1))
        return
      }
      wx.uploadFile({
        url: vm.baseURL + 'upload/',
        filePath: file,
        header: vm.header,
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
    return new Promise((resolve, reject) => {
      if (this.validateToken() === false) {
        reject(new Error(-1))
        return
      }
      wx.request({
        url: vm.withBaseURL ? vm.baseURL + url : url,
        data,
        method,
        header: vm.header,
        success (res) {
          resolve(res)
        },
        fail () {
          reject(new Error('request faild'))
        }
      })
    })
  }
}

export default new Request({
  baseURL: 'http://starriest.top:8000/vron/',
  withBaseURL: true,
  header: {
    'content-type': 'application/json'
  }
})
