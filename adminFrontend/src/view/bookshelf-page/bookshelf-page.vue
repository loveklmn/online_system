<template>
  <div>
    <Card title="所有图书" class="bookshelf">
      <filter-table @load="loadData"
                  :data="currentPageBookList"
                  :columns="columns"
                  :search="search">
      </filter-table>
      <Page :total="page.totalCount" :page-size="page.pageSize" :current="page.pageCurrent" show-total @on-change="changePage" class="page-bar"/>
      <Divider />
      <Button type="primary" class="new-book-btn">导入新书</Button>
    </Card>
  </div>
</template>

<script>
import { getAllBooks } from '@/api/data'
import FilterTable from './FilterTable'

const pageStatus = {
  0: {
    value: 0,
    name: '少于100'
  },
  1: {
    value: 1,
    name: '100-200'
  },
  2: {
    value: 2,
    name: '多于200'
  }
}

const typeStatus = {
  'ER': {
    value: 'ER',
    name: '精读'
  },
  'IR': {
    value: 'IR',
    name: '泛读'
  }
}

const levelList = {
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
  name: 'bookshelf_page',
  components: {
    FilterTable
  },
  data () {
    return {
      search: {},
      columns: [
        {
          type: 'selection',
          width: 60,
          align: 'center'
        },
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
          key: 'page_num',
          sortable: true,
          filter: {
            type: 'Select',
            option: pageStatus
          }
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
      currentPageBookList: [
        {
          id: 1,
          title: 'a',
          level: 'k1',
          type: 'ER',
          page_num: 20
        }
      ],
      page: {
        totalCount: 0,
        pageSize: 3,
        pageCount: 0,
        pageCurrent: 1
      }
    }
  },
  created () {
    getAllBooks().then(res => {
      this.allBooks = res.data
      this.page.totalCount = this.allBooks.length
      this.page.pageCount = Math.ceil(this.page.totalCount / this.page.pageSize)
      this.currentPageBookList = this.allBooks.slice(0, this.page.pageSize)
    })
  },
  async mounted () {
    await this.loadData(conditionObject)
  },
  methods: {
    changePage (currentPage) {
      let start = this.page.pageSize * (currentPage - 1)
      let end = this.page.pageSize * currentPage
      this.currentPageBookList = this.allBooks.slice(start, end)
    },
    turnToDetailPage (params) {
      // params 获得当前书目的数据
      // let currentBook = params.row
      // this.$router.push({
      //   name: 'book_detail_info',
      //   query: currentBook
      // })
    },
    loadData () {
      // serach 记录下会当前的查询条件，此处添加一段逻辑
      // let conditionObject = {
      //   id: this.search.id,
      //   title: this.search.title,
      //   level: this.search.level,
      //   type: this.search.type,
      //   page_num: this.search.page_num
      // }
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
