<template>
  <content-layout
    title="阅读拓展导入">
    <div slot="content">
      <div class="right-content">
        <Card class="right-content-card">
          <p class="title-font">作业描述</p>
          <editor ref="editor" class="input-editor" @on-change="handleChange"/>
          <div class="op-btns">
            <Button class="action-btn" type="primary" @click="clear">清空</Button>
            <Button class="action-btn" type="primary" @click="restore">还原</Button>
            <Button class="action-btn" type="primary" @click="submit">确定上传</Button>
          </div>
        </Card>
      </div>
      <div>
        <a :href="backRoute" class="float" id="menu-share">
          <i class="fa fa-share my-float">返回</i>
        </a>
        <ul>
          <li>
            <a :href="ebookRoute">
              <i class="fa fa-facebook my-float">E-book</i>
            </a>
          </li>
          <li>
            <a :href="guidanceRoute">
              <i class="fa fa-google-plus my-float">亲子指导</i>
            </a>
          </li>
          <li>
            <a :href="gameRoute">
              <i class="fa fa-twitter my-float">游戏导入</i>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </content-layout>
</template>
<script>
import Editor from '_c/editor'
import axios from '@/libs/api.request'
import contentLayout from '_c/content-layout'
export default {
  name: 'assignment_page',
  components: {
    Editor,
    contentLayout
  },
  data () {
    return {
      id: '',
      newAssignment: '',
      currentAssignment: '',
      loading: false,
      backRoute: ``,
      ebookRoute: ``,
      guidanceRoute: ``,
      gameRoute: ``
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
        vm.backRoute = `/book/${vm.id}`
        vm.ebookRoute = `/book/${vm.id}/ebook`
        vm.guidanceRoute = `/book/${vm.id}/guidance`
        vm.gameRoute = `/book/${vm.id}/game`
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
.op-btns {
  text-align: center;
  margin-top: 3%;
  margin-bottom: 5%;
}

.action-btn {
  width: 15%;
  margin-left: 2%;
  margin-right: 2%;
}

.title-font {
  margin-top: 1%;
  margin-bottom: 2%;
  font-size: 15px;
  font-weight: bold;
  margin-left: 3%;
}

.input-editor {
  margin-left: 3%;
  margin-right: 5%;
}

.label-container{
  position:fixed;
  bottom:48px;
  right:105px;
  display:table;
  visibility: hidden;
}

.label-text{
  color:#FFF;
  background:rgba(51,51,51,0.5);
  display:table-cell;
  vertical-align:middle;
  padding:10px;
  border-radius:3px;
}

.label-arrow{
  display:table-cell;
  vertical-align:middle;
  color:#333;
  opacity:0.5;
}

.float{
  position:fixed;
  width:60px;
  height:60px;
  bottom:40px;
  right:40px;
  background-color:rgb(85, 86, 87);
  color:#FFF;
  border-radius:50px;
  text-align:center;
  box-shadow: 2px 2px 3px #999;
  z-index:1000;
  animation: bot-to-top 2s ease-out;
  padding-top: 21px;
}

ul{
  position:fixed;
  right:40px;
  padding-bottom:20px;
  bottom:80px;
  z-index:100;
}

ul li{
  list-style:none;
  margin-bottom:10px;
}

ul li a{
  background-color:#828488fc;
  color:#FFF;
  border-radius:50px;
  text-align:center;
  box-shadow: 2px 2px 3px #999;
  width:60px;
  height:60px;
  display:block;
  padding-top: 21px;
}

ul:hover{
  visibility:visible!important;
  opacity:1!important;
}

.my-float{
  font-size:10px;
  margin-top:100px;
  text-align: center;
}

a#menu-share + ul{
  visibility: hidden;
}

a#menu-share:hover + ul{
  visibility: visible;
  animation: scale-in 0.5s;
}

a#menu-share i{
  animation: rotate-in 0.5s;
}

a#menu-share:hover > i{
  animation: rotate-out 0.5s;
}

@keyframes bot-to-top {
    0%   {bottom:-40px}
    50%  {bottom:40px}
}

@keyframes scale-in {
    from {transform: scale(0);opacity: 0;}
    to {transform: scale(1);opacity: 1;}
}

@keyframes rotate-in {
    from {transform: rotate(0deg);}
    to {transform: rotate(360deg);}
}

@keyframes rotate-out {
    from {transform: rotate(360deg);}
    to {transform: rotate(0deg);}
}

</style>
