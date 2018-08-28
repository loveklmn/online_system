<template>
    <div class="layout">
        <Layout>
            <Sider width="auto" >
                <Menu
                  theme="dark"
                  width="auto"
                  class="menu"
                  @on-select="select">
                    <MenuItem
                      v-for="(img, index) in preview"
                      :key="index"
                      :name="index"
                      class="menu-item"
                      >
                      <img
                        :src="img"
                        :class="[ index === curid ? 'preview-selected' : 'preview']"/>
                    </MenuItem>
                    <Button
                      type="dashed"
                      ghost
                      class="add-page-button"
                      @click="addNewPage">添加新页面</Button>
                    <Button
                      type="primary"
                      class="add-page-button"
                      @click="importBook">上传这本书</Button>
                </Menu>
            </Sider>
            <Layout>
                <Header v-if="curpage !==  null" :style="{background: '#fff', boxShadow: '0 2px 3px 2px rgba(0,0,0,.1)'}">
                  <h1 class="page-num">P{{curPageNum}}</h1>
                </Header>
                <Content :style="{padding: '0 16px 16px'}">
                    <Card>
                        <pageimport
                          class="pageimport"
                          :page.sync="curpage"
                          v-on:deletePage="deletePage"
                          v-on:picChange="countPreview"></pageimport>
                    </Card>
                </Content>
            </Layout>
        </Layout>
    </div>
</template>
<script>
import pageimport from './page-import.vue'
import axios from '@/libs/api.request'
export default {
  data () {
    return {
      bookid: -1, // 在created () 中修改
      preview: [],
      curpage: null,
      book: []
    }
  },
  created () {
    this.bookid = this.$route.params.id
    axios.request({
      url: `books/${this.bookid}/ebook/`,
      method: 'get'
    }).then(data => {
      this.initBook(data)
    })
  },
  computed: {
    defaultPic: function () {
      return require('@/assets/images/addPage.png')
    },
    curid: function () {
      return this.book.indexOf(this.curpage)
    },
    curPageNum: function () {
      return this.curid + 1
    }
  },
  methods: {
    // 被created调用
    initBook: function (data) {
      this.book = Object.values(data)
      if (this.book.length === 0) {
        this.addNewPage()
      }
      this.curpage = this.book[0]
    },
    // 左侧Menu(预览)点击时调用
    select: function (i) {
      this.curpage = this.book[i]
    },
    countPreview: function () {
      this.preview = []
      for (let i = 0; i < this.book.length; i += 1) {
        if (this.book[i].picture === null) {
          this.preview.push(this.defaultPic)
        } else {
          this.preview.push(this.book[i].picture)
        }
      }
    },
    countPage: function () {
      for (let i = 0; i < this.book.length; i += 1) {
        this.book[i].number = i + 1
      }
    },
    addNewPage: function () {
      let newPage = {
        number: this.book.length,
        picture: null,
        sentences: []
      }
      this.book.push(newPage)
      this.curpage = newPage
    },
    deletePage: function (pageNum) {
      let index = pageNum - 1
      this.book.splice(index, 1)
      if (this.book.length === 0) {
        alert('至少要有一面书！')
        this.addNewPage()
      } else if (index < this.book.length) {
        this.curpage = this.book[index]
      } else {
        this.curpage = this.book[this.book.length - 1]
      }
    },
    // 上传这本书
    importBook: function () {
      if (!this.testBook()) {
        return
      }
      axios.request({
        url: `books/${this.bookid}/ebook/`,
        data: this.book,
        method: 'post'
      }).then(data => {
        this.$Message.info(`上传成功！`)
      })
    },
    testBook: function () {
      for (let i = 0; i < this.book.length; i += 1) {
        let page = this.book[i]
        if (page.picture === null) {
          this.$Message.info(`第${i + 1}页没有上传图片哦`)
          return false
        }
        if (page.sentences.length === 0) {
          this.$Message.info(`第${i + 1}页至少要有一句话哦`)
          return false
        }
        for (let j = 0; j < page.sentences.length; j += 1) {
          let sen = page.sentences[j]
          if (sen.content === null) {
            this.$Message.info(`第${i + 1}页的第${j + 1}句话没有文本哦`)
            return false
          }
          if (sen.translated === null) {
            this.$Message.info(`第${i + 1}页的第${j + 1}句话没有翻译哦`)
            return false
          }
          if (sen.audio === null) {
            this.$Message.info(`第${i + 1}页的第${j + 1}句话没有上传音频哦`)
            return false
          }
          if (sen.x1 === null) {
            this.$Message.info(`第${i + 1}页的第${j + 1}句话没有选择区域哦`)
            return false
          }
        }
      }
      return true
    }
  },
  watch: {
    book: function (val) {
      this.countPreview()
      this.countPage()
    }
  },
  components: {
    pageimport
  },
  mounted () {
  }
}
</script>
<style scoped>
.layout-con {
  width: 100%;
  height: 100%;
}

.menu {
  height: 560px;
}

.menu-item {
  padding: auto;
  margin: 0;
}

.add-page-button {
  display: block;
  width: 100px;
  margin-top: 5px;
  margin-right: 25px;
  margin-left: 25px;
}

.page-num {
  font-size: 30px;
}

.preview {
  display: block;
  width: 100px;
  height: 100px;
  padding: 0;
  margin: auto;
  border: 2px solid grey;
}

.preview-selected {
  display: block;
  width: 100px;
  height: 100px;
  padding: 0;
  margin: auto;
  border: 2px solid red;
}

.pageimport {
  height: 560px;
}
</style>
