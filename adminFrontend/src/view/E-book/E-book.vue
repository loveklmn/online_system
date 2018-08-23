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
                </Menu>
            </Sider>
            <Layout>
                <Header :style="{background: '#fff', boxShadow: '0 2px 3px 2px rgba(0,0,0,.1)'}">
                  <h1 class="page-num">P{{curPageNum}}</h1>
                </Header>
                <Content :style="{padding: '0 16px 16px'}">
                    <Card>
                        <pageimport class="pageimport" :page.sync="curpage"></pageimport>
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
      // curid: 0,
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
      return '@/assets/images/addPage.png'
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
      console.log(i)
      this.curpage = this.book[i]
      console.log(this.curpage)
    },
    countPreview: function () {
      this.preview = []
      for (let i = 0; i < this.book.length; i += 1) {
        this.preview.push(this.book[i].picture)
      }
    }
  },
  watch: {
    book: function (val) {
      this.countPreview()
    }
  },
  components: {
    pageimport
  },
  mounted () {
    this.countPreview()
    console.log(this.preview)
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
