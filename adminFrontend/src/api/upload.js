import axios from '@/libs/api.request'

export default function (file) {
  let data = new FormData()
  let name = hash(file.name + new Date().getTime() + Math.random())
  data.append('file', file, name)
  return axios.request({
    url: 'upload/',
    data: data,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    method: 'post'
  })
}

function hash (str) {
  var i = str.length
  var hash1 = 5381
  var hash2 = 52711

  while (i--) {
    const char = str.charCodeAt(i)
    hash1 = (hash1 * 33) ^ char
    hash2 = (hash2 * 33) ^ char
  }

  return (hash1 >>> 0) * 4096 + (hash2 >>> 0)
}
