<template>
<div class="main">
  <div class="step-row">
    <Steps :current="current" class="steps">
      <Step title="填写生成账号信息"></Step>
      <Step title="确认生成账号信息"></Step>
      <Step title="账号生成成功"></Step>
    </Steps>
  </div>
  <div class="generate-result">
      <Divider>本次操作信息</Divider>
      <div class="text-tip">
        <p>
          生成账号所在级别:&nbsp;&nbsp;&nbsp;{{ level }}
          ----------
          生成账号数量:&nbsp;&nbsp;&nbsp;{{ amount }}
        </p>
      </div>
      <Divider>生成账号结果</Divider>
      <div class="csv-table">
        <tables ref="tables" v-model="codeList" :columns="titleList" />
        <Button type="primary" class="export-csv-btn" @click="exportExcel"><Icon type="md-download" color="green" />导出为Csv文件</Button>
      </div>
      <div class="operator-btns">
        <Button type="primary" class="continue-btn" @click="generateAgain">继续生成账号</Button>
        <Button type="warning" class="back-btn" @click="reset">返回首页</Button>
      </div>
  </div>
</div>
</template>
<script>
import Tables from '_c/tables'
import './format.less'
import axios from '@/libs/api.request'

export default {
  data () {
    return {
      level: '',
      amount: '',
      current: 3,
      titleList: [
        {
          title: '激活码',
          key: 'code'
        },
        {
          title: '阅读等级',
          key: 'level',
          sortable: true
        }
      ],
      codeList: []
    }
  },
  components: {
    Tables
  },
  mounted () {
    this.level = this.$route.query.level
    this.amount = this.$route.query.amount
  },
  beforeRouteEnter (to, from, next) {
    axios.request({
      url: 'generatekey/',
      data: {
        'level': to.query.level,
        'count': to.query.amount
      },
      method: 'post'
    }).then(data => {
      next(vm => {
        vm.codeList = data.map(code => {
          return {'code': code, 'level': to.query.level}
        })
      })
    })
  },
  methods: {
    generateAgain () {
      this.$router.push({
        name: 'create_user'
      })
    },
    reset () {
      this.$router.push({
        path: '/home'
      })
    },
    exportExcel () {
      this.$refs.tables.exportCsv({
        filename: `table-${(new Date()).valueOf()}.csv`
      })
    }
  }
}
</script>
