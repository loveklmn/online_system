<style scoped>
    .layout{
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
    }
    .layout-header-bar{
        background: #fff;
        box-shadow: 0 1px 1px rgba(0,0,0,.1);
    }
    .menu-item span{
        display: inline-block;
        overflow: hidden;
        width: 69px;
        text-overflow: ellipsis;
        white-space: nowrap;
        vertical-align: bottom;
        transition: width .2s ease .2s;
    }
    .menu-item i{
        transform: translateX(0px);
        transition: font-size .2s ease, transform .2s ease;
        vertical-align: middle;
        font-size: 16px;
    }
    .collapsed-menu span{
        width: 0px;
        transition: width .2s ease;
    }
    .collapsed-menu i{
        transform: translateX(5px);
        transition: font-size .2s ease .2s, transform .2s ease .2s;
        vertical-align: middle;
        font-size: 22px;
    }
</style>
<template>
    <div class="layout">
        <Layout>
            <Layout>
                <Header class="layout-header-bar">学生列表</Header>
                <Content :style="{margin: '20px', background: '#fff', minHeight: '220px'}">
                  <div>
                    <filter-table
                      @load= "loadData"
                      :data= "selectedStudents"
                      :columns= "columns"
                      :search= "condition">
                    </filter-table>
                  </div>
                </Content>
            </Layout>
        </Layout>
    </div>
</template>
<script>
import FilterTable from '_c/filter-table'
import axios from '@/libs/api.request'

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
    FilterTable
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
      console.log(params)
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
      if (this.condition.score && student.score !== this.condition.score) {
        return false
      }
      if (this.condition.level && student.level !== this.condition.level) {
        return false
      }
      return true
    }
  }
}
</script>
