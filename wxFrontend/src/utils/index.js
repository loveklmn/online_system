function formatNumber (n) {
  const str = n.toString()
  return str[1] ? str : `0${str}`
}

export function formatTime (date) {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()

  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  const t1 = [year, month, day].map(formatNumber).join('/')
  const t2 = [hour, minute, second].map(formatNumber).join(':')

  return `${t1} ${t2}`
}

export function formatYMD (stringDate) {
  let time = new Date(stringDate)
  let year = time.getFullYear()
  let month = time.getMonth() + 1
  let date = time.getDate()
  return `${year}年${month}月${date}日`
}

export default {
  formatNumber,
  formatTime,
  formatYMD
}
