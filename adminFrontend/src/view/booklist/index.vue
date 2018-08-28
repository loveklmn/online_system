<template>
<content-layout
  title="图书列表">
  <div slot="content">
    <filter-table
      @load="loadData"
      :data="selectedBooks"
      :columns="columns"
      :search="condition"
      :pageSize="10">
    </filter-table>
    <Divider />
    <Button type="primary" :loading="loading" @click="newBook" class="new-book-btn">导入新书</Button>
  </div>
</content-layout>
</template>

<script>
import FilterTable from '_c/filter-table'
import axios from '@/libs/api.request'
import contentLayout from '_c/content-layout'
const typeStatus = {
  0: {
    value: '',
    name: '全部'
  },
  1: {
    value: '精读',
    name: '精读'
  },
  2: {
    value: '泛读',
    name: '泛读'
  }
}

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
          title: '编号',
          key: 'id',
          sortable: true,
          filter: {
            type: 'Input'
          }
        },
        {
          title: '书名',
          key: 'title',
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
          title: '类别',
          key: 'type',
          sortable: true,
          filter: {
            type: 'Select',
            option: typeStatus
          }
        },
        {
          title: '页数',
          key: 'pages_num',
          sortable: true
        },
        {
          title: '详细信息',
          key: 'handle',
          render: (h, params) => {
            return h('Button', {
              props: {
                type: 'primary',
                value: '查看详细信息'
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
      allBooks: [],
      selectedBooks: []
    }
  },
  beforeRouteEnter (to, from, next) {
    axios.request({
      url: 'books',
      method: 'get'
    }).then(data => {
      next(vm => {
        vm.selectedBooks = vm.allBooks = data.map(book => {
          if (book.type === 'IR') {
            book.type = '精读'
          } else {
            book.type = '泛读'
          }
          return book
        })
      })
    })
  },
  methods: {
    turnToDetailPage (params) {
      this.$router.push({
        path: '/book/' + params.row.id
      })
    },
    loadData () {
      this.selectedBooks = this.allBooks.filter(this.isSelected)
    },
    isSelected (book) {
      if (this.condition.id && book.id !== parseInt(this.condition.id)) {
        return false
      }
      if (this.condition.level && book.level !== this.condition.level) {
        return false
      }
      if (this.condition.title && book.title.indexOf(this.condition.title) === -1) {
        return false
      }
      if (this.condition.type && book.type !== this.condition.type) {
        return false
      }
      return true
    },
    newBook () {
      this.$router.push({
        path: '/book/-1'
      })
    }
  }
}
</script>

<style>
.bookshelf {
  margin: 3%;
}
.new-book-btn {
  margin-top: 2%;
  margin-bottom: 2%;
  margin-left: 40%;
  width: 20%;
}
.page-bar {
  margin-top: 3%;
}
</style>
