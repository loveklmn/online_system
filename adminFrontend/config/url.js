import env from './env'

const PRO_URL = 'http://starriest.top:8000/vron/'
const DEV_URL = 'http://starriest.top:8000/vron/'

export default env === 'development' ? DEV_URL : PRO_URL
