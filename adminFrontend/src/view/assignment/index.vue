<template>
  <div class="main-layout">
    <div class="center-body">
      <div class="left-menu-card">
        <Button class="left-menu-btn" @click="clear">清空</Button>
        <Button class="left-menu-btn" @click="restore">还原</Button>
        <Button class="left-menu-btn" :loading="loading" @click="submit">确定上传</Button>
        <Button class="left-menu-btn" @click="goback">返回</Button>
      </div>
      <div class="right-content">
        <Card title="阅读拓展导入" class="right-content-card">
          <editor ref="editor" class="input-editor" @on-change="handleChange"/>
        </Card>
      </div>
    </div>
  </div>
</template>
<script>
import Editor from '_c/editor'
import axios from '@/libs/api.request'

export default {
  name: 'assignment_page',
  components: {
    Editor
  },
  data () {
    return {
      id: '',
      newAssignment: '',
      currentAssignment: '',
      loading: false
    }
  },
  beforeRouteEnter (to, from, next) {
    let id = to.params.id
    axios.request({
      data: {
        id: id
      },
      url: 'books/',
      method: 'post'
    }).then(data => {
      next(vm => {
        vm.id = id
        vm.newAssignment = vm.currentAssignment = data.assignment
        vm.$refs.editor.setValue(vm.newAssignment)
      })
    })
  },
  methods: {
    clear () {
      this.newAssignment = ''
      this.$refs.editor.setValue('')
    },
    handleChange (html, text) {
      this.newAssignment = html
    },
    restore () {
      this.newAssignment = this.currentAssignment
      this.$refs.editor.setValue(this.currentAssignment)
    },
    goback () {
      this.$router.push({
        path: '/book/' + this.id
      })
    },
    submit () {
      this.loading = true
      axios.request({
        data: {
          id: this.id,
          assignment: this.newAssignment
        },
        url: 'books/',
        method: 'post'
      }).then((data) => {
        this.newAssignment = this.currentAssignment = data.assignment
        this.loading = false
        this.$Message.success('上传成功')
      })
    }
  }
}
</script>

<style lang="less" scoped>
.main-layout {
  height: 100%;
  .top-title {
    margin-bottom: 3%;
    .top-title-card {
      font-size: 20px;
      font-style: italic;
      background-color: #dcd7d7;
    }
  }
  .center-body {
    display: flex;
    flex-direction: row;
    width: 100%;
    align-items: stretch;
    height: 100%;
    .left-menu-card {
      padding-top: 2%;
      border: solid 1px;
      border-color: lightgrey;
      flex-grow: 1;
      .left-menu-btn {
        display: block;
        width: 100%;
        height: 13%;
        background-color: #4693db;
      }
    }
    .right-content {
      flex-grow: 7;
      border: solid 1px;
      border-color: lightgrey;
      .right-content-card {
        height: 100%;
      }
      .operation-btns {
        margin-top: 2%;
        text-align: center;
        .op-btn {
          margin-left: 3%;
          margin-right: 3%;
        }
      }
      .editor-wrapper {
        .w-e-text-container {
          height: 500px;
        }
      }
    }
  }
}

.cover-picture {
  margin-left: 70px;
  margin-top: 40px;
  width: 200px;
  height: 250px;
}

</style>
