<template>
  <div>
    <Row :gutter="20">
      <i-col span="12">
        <Card title="后台管理员交流QQ群" shadow>
          <img class="qq-group-img" :src="qqFans" alt="">
          <p class="qq-group-intro">本群专为弗恩英语后台管理员交流提供.</p>
        </Card>
      </i-col>
    </Row>
  </div>
</template>

<script>
import qqFans from '@/assets/images/qq-fance.jpg'
export default {
  name: 'join_page',
  data () {
    return {
      qqFans
    }
  }
}
</script>

<style>
.qq-group-img{
  display: block;
  margin: 0 auto;
  width: 240px;
}
.qq-group-intro{
  padding: 20px;
  font-size: 16px;
}
</style>
