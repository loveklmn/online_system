<template>
  <div class="single-home">
    <Card class="navCard">
      <Row :gutter="20" class="first-row">
        <i-col span="6" v-for="(infor, i) in inforCardData" :key="`infor-${i}`" style="height: 120px;">
          <infor-card shadow :color="infor.color" :icon="infor.icon" :icon-size="36">
            <count-to :end="infor.count" count-class="count-style"/>
            <p>{{ infor.title }}</p>
          </infor-card>
        </i-col>
      </Row>
    </Card>
    <Card class="contentCard">
      <Row v-for="i in (customIconList.length / 3)" :key="`custom-icon-row-${i}`">
        <i-col span="8" v-for="item in customIconList.slice((i - 1) * 3, i * 3)" :key="`custom-icon-${item.title}`">
          <Card class="icon-card" >
            <icons :size="30" :type="item.icon" :color="`#ff9900`"/>
            <br>
            <img :src= item.imgPath  />
            <p class="icon-code">&lt;{{ item.title }}&gt;</p>
          </Card>
        </i-col>
    </Row>
    </Card>
  </div>
</template>

<script>
import InforCard from '_c/info-card'
import CountTo from '_c/count-to'
import Icons from '_c/icons'
import { ChartPie, ChartBar } from '_c/charts'
import Example from './example.vue'
import logo from '@/assets/images/logo-min.jpg'
export default {
  name: 'home',
  components: {
    InforCard,
    CountTo,
    ChartPie,
    ChartBar,
    Example,
    Icons
  },
  data () {
    return {
      inforCardData: [
        { title: '添加账户', icon: 'md-person-add', count: 803, color: '#2d8cf0' },
        { title: '资料上传', icon: 'md-locate', count: 23432, color: '#19be6b' },
        { title: '学习进度', icon: 'md-help-circle', count: 142, color: '#ff9900' },
        { title: '发布消息', icon: 'md-share', count: 657, color: '#ed3f14' }
      ],
      customIconList: [
        {icon: 'smile', imgPath: logo, title: '资料室'},
        {icon: 'smile', imgPath: logo, title: '用户数量统计'},
        {icon: 'smile', imgPath: logo, title: '通知公告'},
        {icon: 'smile', imgPath: logo, title: '工作日志'},
        {icon: 'smile', imgPath: logo, title: '用户反馈'},
        {icon: 'smile', imgPath: logo, title: '帮助'}
      ],
      logo
    }
  },
  mounted () {
    //
  }
}
</script>

<style lang="less">
.count-style{
  font-size: 50px;
}
.icon-card{
  margin: 20px 20px 20px;
  text-align: center;
  height: 240px;
  border-radius: 20%;
  background-color:rgba(247, 169, 169, 0.3);
}
.single-home {
  background-color: white;
}
.navCard {
  background-color: rgba(246, 248, 133, 0.5);
}
.contentCard {
  background-color: rgba(238, 231, 236, 0.5);
}

</style>
