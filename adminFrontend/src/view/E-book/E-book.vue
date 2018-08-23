<template>
    <div class="layout">
        <!-- <Layout :style="{minHeight: '100vh'}"> -->
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
                      <!-- class="menu-item"> -->
                      <img
                        :src="img"
                        :class="[ index === curid ? 'preview-selected' : 'preview']"/>
                    </MenuItem>
                    <!-- <MenuItem
                      :name="-1">
                      <img src="@/assets/images/addPage.png" class="preview"/>
                    </MenuItem> -->
                    <Button
                      type="dashed"
                      ghost
                      class="add-page-button"
                      @click="addNewPage">添加新页面</Button>
                </Menu>
            </Sider>
            <Layout>
                <Header :style="{background: '#fff', boxShadow: '0 2px 3px 2px rgba(0,0,0,.1)'}">
                  <h1 class="page-num">P{{curPageNum}}</h1>
                </Header>
                <Content :style="{padding: '0 16px 16px'}">
                    <Card>
                        <pageimport
                          class="pageimport"
                          :page.sync="curpage"
                          v-on:deletePage="deletePage"></pageimport>
                    </Card>
                </Content>
            </Layout>
        </Layout>
    </div>
</template>
<script>
import pageimport from '@/view/components/page-import/page-import.vue'
export default {
  data () {
    return {
      preview: [],
      curpage: null,
      book: [
        {
          number: 1,
          picture: 'https://picsum.photos/200/300/?image=1',
          sentences: [
            {
              content: 'I do something',
              audio: 'http://a/b',
              translated: '我干某事',
              x1: 100,
              y1: 50,
              x2: 20,
              y2: 10
            },
            {
              content: 'I did something',
              audio: 'http://a/b',
              translated: '我干过某事',
              x1: 100,
              y1: 50,
              x2: 20,
              y2: 50
            }
          ]
        },
        {
          number: 2,
          picture: 'https://picsum.photos/200/300/?image=2',
          sentences: [
            {
              content: 'I eat a banana',
              audio: 'http://b/y',
              translated: '我吃了一个香蕉',
              x1: 100,
              y1: 100,
              x2: 200,
              y2: 200
            }
          ]
        }
      ]
    }
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
    select: function (i) {
      // console.log(i)
      this.curpage = this.book[i]
      // console.log(this.curpage)
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
        sentences: [
          {
            content: null,
            audio: null,
            translated: null,
            x1: null,
            y1: null,
            x2: null,
            y2: null
          }
        ]
      }
      this.book.push(newPage)
      this.curpage = newPage
    },
    deletePage: function (pageNum) {
      console.log(pageNum)
      let index = pageNum - 1
      this.book.splice(index, 1)
      if (this.book.length === 0) {
        this.addNewPage()
      } else if (index < this.book.length) {
        this.curpage = this.book[index]
      } else {
        this.curpage = this.book[this.book.length - 1]
      }
      console.log(this.curpage)
      console.log(this.book)
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
    this.countPreview()
  }
}
</script>
<style scoped>
.layout-con {
    height: 100%;
    width: 100%;
}
.menu {
  height: 560px;
}
.menu-item {
  padding: auto;
  margin: 0;
}
.add-page-button {
  width: 100px;
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
