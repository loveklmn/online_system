<template>
<div>
  <Divider class="first-divider" orientation="left"><p class="title-font">历史消息统计</p></Divider>
  <Table
    :data="noticeList"
    :columns="columns">
  </Table>
</div>
</template>
<script>
import FilterTable from '_c/filter-table'
import Tables from '_c/tables'
import axios from '@/libs/api.request'
export default {
  name: 'noticeName',
  data () {
    return {
      condition: {},
      columns: [
        {
          title: '序号',
          key: 'id'
        },
        {
          title: '消息内容',
          key: 'content',
          filter: {
            type: 'Input'
          }
        },
        {
          title: '发布时间',
          key: 'created_time'
        },
        {
          title: '删除',
          key: 'handle',
          render: (h, params) => {
            return h('Button', {
              props: {
                type: 'primary',
                value: '删除消息'
              },
              style: {
                margin: '5%'
              },
              on: {
                click: () => {
                  this.handleDelete(params)
                }
              }
            }, '删除消息')
          }
        }
      ],
      noticeList: []
    }
  },
  components: {
    FilterTable,
    Tables
  },
  created () {
    axios.request({
      url: 'notices',
      method: 'get'
    }).then(data => {
      data.sort(function (a, b) {
        let d1 = new Date(a.created_time)
        let d2 = new Date(b.created_time)
        return d1 < d2 ? 1 : -1
      })
      this.noticeList.push.apply(this.noticeList, data)
      this.noticeList = this.noticeList.map(notice => {
        let time = new Date(notice.created_time)
        let year = time.getFullYear()
        let month = time.getMonth()
        let date = time.getDate()
        notice.created_time = `${year}年${month + 1}月${date}日`
        return notice
      })
    }).catch(error => {
      this.$Message.error(error)
    })
  },
  methods: {
    handleDelete (params) {
      axios.request({
        url: `notices/${params.row.id}/`,
        method: 'delete'
      }).then(msg => {
        this.$Message.success('删除成功')
        let index = -1
        for (let item in this.noticeList) {
          if (this.noticeList[item].id === params.row.id) {
            index = item
            break
          }
        }
        if (index !== -1) {
          this.noticeList.splice(index, 1)
        }
      })
    }
  }
}
</script>
<style scoped>
.first-divider {
  margin-bottom: 2%;
}
.title-font {
  font-size: 16px;
  font-weight: bold;
}
</style>
