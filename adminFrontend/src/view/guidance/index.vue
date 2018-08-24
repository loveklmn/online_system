<template>
  <div class="layout">
    <Layout>
      <Header class="layout-header-bar">亲子阅读指导</Header>
      <Content class="main-content">
        <div class="main-content">
          <p class="tip-title">指导重点：</p>
          <editor class="input-editor" v-model="guidance" @on-change="handleChange"/>
        </div>
        <Divider />
        <div class="vocabulary">
          <p class="tip-title"> 词汇表： </p>
          <Button type="error" class="add-word" @click="addWords">添加单词</Button>
          <tables
            ref="tables"
            editable
            searchable
            search-place="top"
            v-model="words"
            :columns="columns"/>
        </div>
        <div class="operation-btns">
          <Button @click="handleCommit" type="primary" class="op-btn">确认上传</Button>
          <Poptip
            confirm
            title="你确定放弃编辑返回吗？"
            @on-ok="handleReset">
            <Button type="warning" class="op-btn">返回</Button>
          </Poptip>
        </div>
      </Content>
    </Layout>
  </div>
</template>

<script>
import Editor from '_c/editor'
import Tables from '_c/tables'
export default {
  data () {
    return {
      bookId: 0,
      guidance: '',
      success: false,
      columns: [
        {
          title: '英语',
          key: 'word',
          sortable: true,
          editable: true
        },
        {
          title: '中文',
          key: 'meaning',
          sortable: true,
          editable: true
        },
        {
          title: '删除',
          key: 'handle',
          options: ['delete'],
          button: [
            (h, params, vm) => {
              return h('Poptip', {
                props: {
                  confirm: true,
                  title: '你确定要删除吗?'
                },
                on: {
                  'on-ok': () => {
                    vm.$emit('on-delete', params)
                    vm.$emit('input', params.tableData.filter((item, index) => index !== params.row.initRowIndex))
                  }
                }
              })
            }
          ]
        }
      ],
      words: []
    }
  },
  components: {
    Editor,
    Tables
  },
  created () {
    // 获得图书id赋值给bookId
  },
  methods: {
    addWords () {
      this.words.push({
        word: '输入单词',
        meaning: '输入汉译'
      })
    },
    handleChange (html, text) {
      // 得到富文本编辑器的输入
      this.guidance = html
    },
    handleCommit () {
      // 数据上传到数据库
      // if(上传成功) this.$Message.success('上传成功！')
    },
    handleReset () {
      // 跳转到图书详情页面
    }
  }
}
</script>

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
.middle-avatar {
  margin-left: 40%;
  margin-top: 2%;
  margin-bottom: 2%;
}
.main-content {
  margin-left: 3%;
  font-size: 20px;
}
.vocabulary {
  margin-top: 2%;
  margin-left: 3%;
  font-size: 20px;
}
.add-btn {
  display: inline-block;
  width: 15%;
  margin: auto;
}
.tip-title {
  display: inline-block;
  margin-top: 1%;
  margin-bottom: 2%;
  font-size: 30px;
}
.operation-btns {
  margin-top: 2%;
  margin-left: 40%;
  margin-right: 40%;
}
.op-btn {
  margin: 5px;
  width: 120px;
  margin-bottom: 5px;
}
.main-content {
  margin: '20px';
  background: '#fff';
  margin-right: 4%;
}
.add-word {
  margin: 2%;
  width: 15%;
}
.vocabulary {
  margin-right: 5%;
}
</style>