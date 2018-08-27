<template>
<div class="main">
  <div class="step-row">
    <Steps :current="2" class="steps">
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
        <Button type="primary" class="continue-btn " @click="generateAgain">继续生成账号</Button>
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
  name: 'thirdStep',
  props: {
    accountLevel: {
      type: Number,
      default: 1
    },
    accountAmount: {
      type: Number,
      default: 1
    }
  },
  data () {
    return {
      level: this.accountLevel,
      amount: this.accountAmount,
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
  created () {
    axios.request({
      url: 'generatekey/',
      data: {
        'level': this.level,
        'count': this.amount
      },
      method: 'post'
    }).then(data => {
      this.codeList = data.map(code => {
        return {'code': code, 'level': this.level}
      })
    })
  },
  methods: {
    generateAgain () {
      this.$emit('generateAgain')
    },
    reset () {
      this.$emit('backHome')
    },
    exportExcel () {
      this.$refs.tables.exportCsv({
        filename: `table-${(new Date()).valueOf()}.csv`
      })
    }
  }
}
</script>
