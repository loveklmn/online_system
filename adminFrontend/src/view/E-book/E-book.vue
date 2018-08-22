<template>
    <div class="layout">
        <!-- <Layout :style="{minHeight: '100vh'}"> -->
        <Layout>
            <Sider width="auto" >
                <Menu
                  theme="dark"
                  width="auto"
                  class="menu"
                  @on-select="test">
                    <MenuItem
                      v-for="img in preview"
                      :key="img"
                      :name="img"
                      class="menu-item">
                      <img :src="img" class="preview"></img>
                    </MenuItem>
                </Menu>
            </Sider>
            <Layout>
                <Header :style="{background: '#fff', boxShadow: '0 2px 3px 2px rgba(0,0,0,.1)'}">
                  <h1 class="page-num">P1</h1>
                </Header>
                <Content :style="{padding: '0 16px 16px'}">
                    <Card>
                        <pageimport class="pageimport">Content</pageimport>
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
      preview: [
        'https://picsum.photos/200/300/?image=1',
        'https://picsum.photos/200/300/?image=2',
        'https://picsum.photos/200/300/?image=3'
      ]
    }
  },
  computed: {
  },
  methods: {
    test: function (e) {
      console.log(e)
    }
  },
  components: {
    pageimport
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
  border: 2px solid blue;
}
.pageimport {
  height: 560px;
}
</style>
