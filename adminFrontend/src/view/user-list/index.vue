<template>
<content-layout
  title="学生列表">
  <div slot="content" class="main-content">
    <filter-table
      @load= "loadData"
      :data= "selectedStudents"
      :columns= "columns"
      :search= "condition">
    </filter-table>
  </div>
</content-layout>
</template>
<script>
import FilterTable from '_c/filter-table'
import axios from '@/libs/api.request'
import contentLayout from '_c/content-layout'
const levelList = {
  0: {
    value: '',
    name: '全部'
  },
  1: {
    value: 1,
    name: 'k1'
  },
  2: {
    value: 2,
    name: 'k2'
  },
  3: {
    value: 3,
    name: 'k3'
  },
  4: {
    value: 4,
    name: 'k4'
  }
}

export default {
  name: 'userlist',
  components: {
    FilterTable,
    contentLayout
  },
  data () {
    return {
      loading: false,
      condition: {},
      columns: [
        {
          title: '序号',
          key: 'id',
          sortable: true
        },
        {
          title: '姓名',
          key: 'username',
          sortable: true,
          filter: {
            type: 'Input'
          }
        },
        {
          title: '级别',
          key: 'level',
          sortable: true,
          filter: {
            type: 'Select',
            option: levelList
          }
        },
        {
          title: '昵称',
          key: 'nickname',
          sortable: true,
          filter: {
            type: 'Input'
          }
        },
        {
          title: '分数',
          key: 'score',
          sortable: true,
          filter: {
            type: 'Input'
          }
        },
        {
          title: '详细信息',
          key: 'handle',
          render: (h, params) => {
            return h('Button', {
              props: {
                type: 'primary',
                value: '查看学生详细信息'
              },
              style: {
                margin: '5%'
              },
              on: {
                click: () => {
                  this.turnToDetailPage(params)
                }
              }
            }, '详细信息')
          }
        }
      ],
      allStudents: [],
      selectedStudents: []
    }
  },
  beforeRouteEnter (to, from, next) {
    axios.request({
      url: 'students',
      method: 'get'
    }).then(data => {
      next(vm => {
        vm.selectedStudents = vm.allStudents = data.map(student => {
          return student
        })
      })
    })
  },
  methods: {
    turnToDetailPage (params) {
      this.$router.push({
        path: '/student/' + params.row.id
      })
    },
    loadData () {
      this.selectedStudents = this.allStudents.filter(this.isSelected)
    },
    isSelected (student) {
      if (this.condition.username && student.username.indexOf(this.condition.username) === -1) {
        return false
      }
      if (this.condition.nickname && student.nickname.indexOf(this.condition.nickname) === -1) {
        return false
      }
      if (this.condition.score && student.score !== parseInt(this.condition.score)) {
        return false
      }
      if (this.condition.level && student.level !== parseInt(this.condition.level)) {
        return false
      }
      return true
    }
  }
}
</script>
<style scoped>
.main-content {
  margin-left: 4.6%;
  margin-top: 2%;
  margin-right: 4.6%;
}
</style>
