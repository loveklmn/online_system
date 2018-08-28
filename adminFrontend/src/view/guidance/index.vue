<template>
  <div class="layout">
    <Layout>
      <Header class="layout-header-bar">亲子阅读指导</Header>
      <Content class="main-content">
        <div class="main-content">
          <p class="tip-title">指导重点：</p>
          <editor ref="editor" class="input-editor" v-model="guidance" @on-change="handleChange"/>
        </div>
        <Divider />
        <div class="vocabulary">
          <p class="tip-title"> 词汇表： </p>
        </div>
        <div class="vocabulary-list">
          <Card title="添加新单词" class="new-word">
            <Input v-model="newEnglish" class="input-word" placeholder="输入英文"/>
            <Input v-model="newChinese" class="input-word" placeholder="输入中文"/>
            <Button type="error" class="add-btn" @click="addWords">点击添加</Button>
            <Alert class="alert-tip" v-if="emptyTip" type="warning" show-icon>
              单词和翻译不能为空！
            </Alert>
          </Card>
          <Card class="word-list">
            <tables
              ref="tables"
              editable
              searchable
              search-place="top"
              v-model="words"
              :border="true"
              :stripe="true"
              :columns="columns"/>
          </Card>
        </div>
        <Divider />
        <div class="operation-btns">
          <Button :loading="loading" @click="handleCommit" type="primary" class="op-btn">确认上传</Button>
          <Button type="warning" @click="handleReset" class="op-btn">返回</Button>
        </div>
      </Content>
    </Layout>
  </div>
</template>

<script>
import Editor from '_c/editor'
import Tables from '_c/tables'
import axios from '@/libs/api.request'

export default {
  data () {
    return {
      id: 0,
      guidance: '',
      loading: false,
      emptyTip: false,
      columns: [
        {
          title: '英文',
          key: 'word',
          sortable: true,
          editable: true,
          border: true
        },
        {
          title: '中文',
          key: 'meaning',
          sortable: true,
          editable: true,
          border: true
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
      newEnglish: '',
      newChinese: '',
      words: []
    }
  },
  components: {
    Editor,
    Tables
  },
  beforeRouteEnter (to, from, next) {
    let id = to.params.id
    axios.request({
      url: `books/${id}/guidance`,
      method: 'get'
    }).then(data => {
      next(vm => {
        vm.id = id
        vm.guidance = data.guidance
        vm.$refs.editor.setValue(data.guidance)
        vm.words = data.words
      })
    })
  },
  methods: {
    addWords () {
      if (this.newEnglish !== '' && this.newChinese !== '') {
        this.emptyTip = false
        this.words.unshift({
          word: this.newEnglish,
          meaning: this.newChinese
        })
        this.newEnglish = ''
        this.newChinese = ''
      } else {
        this.emptyTip = true
      }
    },
    handleChange (html, text) {
      this.guidance = html
    },
    handleCommit () {
      this.loading = true
      axios.request({
        url: `books/${this.id}/guidance/`,
        method: 'post',
        data: {
          guidance: this.guidance,
          words: this.words
        }
      }).then(data => {
        this.guidance = data.guidance
        this.$refs.editor.setValue(data.guidance)
        this.words = data.words
        this.loading = false
        this.$Message.success('上传成功')
      })
    },
    handleReset () {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
.layout {
  position: relative;
  overflow: hidden;
  background: #f5f7f9;
  border: 1px solid #d7dde4;
  border-radius: 4px;
}

.layout-header-bar {
  background: #fff;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
}

.middle-avatar {
  margin-top: 2%;
  margin-bottom: 2%;
  margin-left: 40%;
}

.main-content {
  margin-right: 4%;
  margin-left: 3%;
  font-size: 20px;
  background: '#fff';
}

.vocabulary {
  margin-top: 2%;
  margin-right: 5%;
  margin-left: 3%;
  font-size: 20px;
}

.vocabulary-list {
  display: flex;
  flex-direction: row;
}

.new-word {
  flex-grow: 1;
  margin-left: 2%;
}

.word-list {
  flex-grow: 3;
  width: 2000px;
  margin-right: 5%;
}

.input-word {
  margin-top: 3%;
  margin-bottom: 3%;
}

.add-btn {
  width: 50%;
  margin-top: 5%;
  margin-left: 25%;
}

.tip-title {
  display: inline-block;
  margin-top: 1%;
  margin-bottom: 2%;
  font-size: 30px;
}

.operation-btns {
  margin-top: 2%;
  margin-bottom: 3%;
  margin-left: 35%;
}

.op-btn {
  width: 200px;
  margin: 5px;
  margin-bottom: 5px;
}

.add-word {
  width: 15%;
  margin: 2%;
}

.ivu-divider.ivu-divider-horizontal {
  background-color: #bcbec1;
}

.alert-tip {
  margin-top: 2%;
}
</style>
