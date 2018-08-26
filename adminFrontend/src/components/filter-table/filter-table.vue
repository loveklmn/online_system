<template>
  <div>
    <Table
      border
      :data="filters"
      :columns="tableColumnsFilters"
      stripe>
    </Table>

    <Table
      :show-header=false
      border
      :data="currentData"
      :columns="columns"
      stripe>
    </Table>

    <Page :total="data.length" :page-size="pageSize" :current.sync="currentPage" show-total class="page-bar"/>
  </div>
</template>

<script>
export default {
  name: 'FilterTable',
  props: [
    'columns',
    'data',
    'search',
    'pageSize'
  ],
  data () {
    return {
      currentPage: 1,
      filters: [{
        title: ''
      }],
      tableColumnsFilters: []
    }
  },
  created () {
    for (let index in this.columns) {
      let filter = {}
      this.$set(filter, 'title', this.columns[index].title)
      if (this.columns[index].width) {
        this.$set(filter, 'width', this.columns[index].width)
      }
      let render = (h) => {
      }
      if (this.columns[index].filter) {
        if (this.columns[index].filter.type && this.columns[index].filter.type === 'Select') {
          render = (h) => {
            return h(this.columns[index].filter.type, {
              props: {
                value: 0
              },
              on: {
                'on-change': (val) => {
                  if (val === 0) {
                    this.$delete(this.search, this.columns[index].key)
                    this.load()
                    return
                  }
                  this.$set(this.search, this.columns[index].key, val)
                  this.load()
                }
              }
            }, this.createOptionsRender(index, h))
          }
        } else {
          render = (h) => {
            let inputValue = {}
            return h(this.columns[index].filter.type, {
              props: {
                placeholder: '输入' + this.columns[index].title,
                icon: 'ios-search'
              },
              on: {
                input: val => {
                  inputValue = val
                  if (!inputValue) {
                    this.validInputValue(index, inputValue)
                  }
                },
                'on-click': () => {
                  this.validInputValue(index, inputValue)
                },
                'on-enter': () => {
                  this.validInputValue(index, inputValue)
                }
              }
            })
          }
        }
      }
      this.$set(filter, 'render', render)
      this.tableColumnsFilters.push(filter)
    }
  },
  methods: {
    createOptionsRender (index, h) {
      // 选项渲染
      let optionRender = []
      if (this.columns[index].filter.option) {
        let option = this.columns[index].filter.option
        for (let i in option) {
          optionRender.push(h('Option', {
            props: {
              value: option[i].value
            }
          }, option[i].name))
        }
      }
      return optionRender
    },
    load () {
      this.$emit('load')
    },
    validInputValue (index, inputValue) {
      if (!inputValue) {
        this.$delete(this.search, this.columns[index].key)
        this.load()
        return
      }
      this.$set(this.search, this.columns[index].key, inputValue)
      this.load()
    }
  },
  computed: {
    currentData () {
      let start = this.pageSize * (this.currentPage - 1)
      let end = this.pageSize * this.currentPage
      return this.data.slice(start, end)
    }
  }
}
</script>

<style scoped>
.page-bar {
  margin-top: 2%;
}
</style>
