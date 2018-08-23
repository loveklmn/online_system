import env from './env'

const DEV_URL = 'http://101.200.62.189:8000/vron/'
const PRO_URL = 'http://101.200.62.189:8000/vron/'

export default env === 'development' ? DEV_URL : PRO_URL
