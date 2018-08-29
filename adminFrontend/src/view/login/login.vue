<template>
<div class="main-content">
  <div class="login-page">
    <Carousel autoplay v-model="value1" loop class="slider">
      <CarouselItem>
          <div class="demo-carousel"></div>
      </CarouselItem>
      <CarouselItem>
          <div class="demo-carouse2"></div>
      </CarouselItem>
      <CarouselItem>
          <div class="demo-carouse3"></div>
      </CarouselItem>
      <CarouselItem>
          <div class="demo-carouse4"></div>
      </CarouselItem>
    </Carousel>
    <div class="login-main">
      <div class="login">
        <div class="login-con">
          <Card icon="log-in" title="欢迎登录" :bordered="false">
            <div class="form-con">
              <login-form @on-success-valid="handleSubmit"></login-form>
              <p class="login-tip">输入管理员账号和密码登录</p>
            </div>
          </Card>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import LoginForm from '_c/login-form'
import { mapActions } from 'vuex'
export default {
  components: {
    LoginForm
  },
  methods: {
    ...mapActions([
      'handleLogin'
    ]),
    handleSubmit ({ userName, password }) {
      this.handleLogin({ userName, password })
        .then(res => {
          this.$router.push({
            name: 'home'
          })
        }).catch(err => {
          console.log(err)
          this.$Message.error('用户不存在或密码错误')
        })
    }
  }
}
</script>
<style scoped>
@import './login.less';
.login-page {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 600px;
  height: 450px;
  margin: 50px auto;
  border-radius: 4px;
  background-color: #ffffff;
  box-shadow: 0 8px 8px 0 rgba(51, 51, 51, 0.05), 0 0 8px 0 rgba(51, 51, 51, 0.15);
}
.slider {
  width: 200px;
  height: 180px;
  margin-left: 45px;
  background-color:rgb(216, 197, 215);
  border-radius: 5px;
}
.demo-carousel {
  height: 180px;
  background-image: url("../../assets/images/joy1.jpg");
  border-radius: 5px;
}
.demo-carouse2 {
  height: 180px;
  background-image: url("../../assets/images/joy2.jpg");
  border-radius: 5px;
}
.demo-carouse3 {
  height: 180px;
  background-image: url("../../assets/images/joy3.jpg");
  border-radius: 5px;
}
.demo-carouse4 {
  height: 180px;
  background-image: url("../../assets/images/joy4.jpg");
  border-radius: 5px;
}
.login-main {
  position: relative;
  display: inline-block;
  width: 50%;
  height: 100%;
  background: #ffffff;
  overflow: hidden;
}
.login-tip {
  margin-left: 50px;
}
body {
  width: 100%;
  height: 100%;
}
</style>
