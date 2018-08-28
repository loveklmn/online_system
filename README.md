# Deployment Document
## Quick Start
```bash
git clone git@se.jisuanke.com:english-reading/Group2.git
```

### Frontend for administrator:
Here is the link of our deployed server:
[Administration site for vron project](http://starriest.top)
```python
username = admin
password = admin
```
**P.S. Please don't mess up our database**

### Wechat mini program deployment
```bash
cd ./Group2
npm install
npm run dev
```
Use `微信开发者工具` to open the `dist` directory.
After build finishes, use `激活码生成` of admin site to get activate code and register your account.
`And you can play with this stupid app.🌚🌚🌚`

## Manual Deployment
### Backend project
#### 1. Install conda
- Install conda for later deployment. See [Tips](#Tips)
- Add `bin` directory, which includes `conda` to your `PATH` environment.

#### 2. Create virtual environment

1. Create virtual environment
```bash
cd ./backend
conda env create -n $your_environment_name -f ./environment.yml
```

2. Activate yout virtual environment

For windows user:
```bash
activate $your_environment_name
```

For Mac or Linux user:
```bash
source activate $your_environment_name
```

And then your should see `($your_environment_name)` at the front of yout command prompt.

Your should run later command under this virtual environment.

#### 3. Config database for Django

1. Create a database for django use
```bash
create database $database_name default character set utf8 collate utf8_unicode_ci;
```

2. Modify django setting to connect to yout database
Go to `setting.py` under `Group2/backend/backend`
Change the following code with your database configuration.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vron',
        'PASSWORD': 'vagrant',
        'USER': 'root',
        'HOST': '127.0.0.1',
    }
}
```

3. Migrate models to your database
```bash
python ./manage.py migrate
```

4. Create super user for [later use](####Start porject)
```bash
python ./manage.py createsuperuser
```

#### 4. Start your Django server
```bash
python ./manage.py runserver 0:8000
```

#### Tips
Choose Anaconda if you:
- Are new to conda or Python
- Like the convenience of having Python and over 150 scientific packages automatically installed at once
Have the time and disk space (a few minutes and 3 GB), and/or
- Don’t want to install each of the packages you want to use individually.

Choose Miniconda if you:
- Do not mind installing each of the packages you want to use individually.
- Do not have time or disk space to install over 150 packages at once, and/or
- Just want fast access to Python and the conda commands, and wish to sort out the other programs later.


# Wechat mini program
#### Change base url to your specific IP and port
Go to `Groups/wxFrontend/src/utils/request.js`
Replace baseURL with your specific url
```javascript
export default new Request({
  baseURL: 'http://starriest.top:8000/vron/',
  withBaseURL: true,
  header: {
    'content-type': 'application/json'
  }
})
```


# Administration frontend
#### Change base url to your specific IP and port
Go to `Group2/adminFrontend/config/url.js`
```javascript
import env from './env'

const PRO_URL = 'http://starriest.top:8000/vron/'
const DEV_URL = 'http://starriest.top:8000/vron/'

export default env === 'development' ? DEV_URL : PRO_URL
```
Replace the IP and port with your specific configuration.

#### Start porject
```bash
npm run dev
```
Go to http://localhost:8080 to see the admin site.
Use the super user account your just created to login.
