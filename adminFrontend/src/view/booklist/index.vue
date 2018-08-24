<template>
  <div>
    <filter-table @load="loadData"
                :data="currentPageBookList"
                :columns="columns"
                :search="condition">
    </filter-table>
    <Page :total="page.totalCount" :page-size="page.pageSize" :current="page.pageCurrent" show-total @on-change="changePage" class="page-bar"/>
    <Divider />
    <Button type="primary" class="new-book-btn">导入新书</Button>
  </div>
</template>

<script>
import FilterTable from '_c/filter-table'
import axios from '@/libs/api.request'

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
    FilterTable
  },
  data () {
    return {
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
      selectedBooks: [],
      currentPageBookList: [],
      page: {
        totalCount: 0,
        pageSize: 10,
        pageCount: 0,
        pageCurrent: 1
      }
    }
  },
  created () {
    axios.request({
      url: 'books',
      method: 'get'
    }).then(data => {
      this.selectedBooks = this.allBooks = data.map(book => {
        if (book.type === 'IR') {
          book.type = '精读'
        } else {
          book.type = '泛读'
        }
        return book
      })
      this.loadData()
      this.changePage(1)
    })
  },
  methods: {
    changePage (currentPage) {
      this.page.totalCount = this.selectedBooks.length
      let start = this.page.pageSize * (currentPage - 1)
      let end = this.page.pageSize * currentPage
      this.currentPageBookList = this.selectedBooks.slice(start, end)
    },
    turnToDetailPage (params) {
      this.$router.push({
        path: '/book/' + params.row.id
      })
    },
    loadData () {
      this.selectedBooks = this.allBooks.filter(this.isSelected)
      this.changePage(1)
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
