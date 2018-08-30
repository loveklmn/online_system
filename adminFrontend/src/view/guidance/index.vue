<template>
<content-layout
title="亲子阅读指导">
  <div slot="content">
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
          <a :href="assignmentRoute">
            <i class="fa fa-google-plus my-float">阅读拓展</i>
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
import Tables from '_c/tables'
import axios from '@/libs/api.request'
import contentLayout from '_c/content-layout'
export default {
  data () {
    return {
      id: 0,
      guidance: '',
      loading: false,
      emptyTip: false,
      backRoute: ``,
      ebookRoute: ``,
      assignmentRoute: ``,
      gameRoute: ``,
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
    Tables,
    contentLayout
  },
  beforeRouteEnter (to, from, next) {
    let id = to.params.id
    axios.request({
      url: `books/${id}/guidance`,
      method: 'get'
    }).then(data => {
      next(vm => {
        vm.id = id
        vm.backRoute = `/book/${vm.id}`
        vm.ebookRoute = `/book/${vm.id}/ebook`
        vm.assignmentRoute = `/book/${vm.id}/assignment`
        vm.gameRoute = `/book/${vm.id}/game`
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
  font-size: 16px;
  font-weight: bold;
  margin-left: 1.7%;
}

.operation-btns {
  margin-top: 2%;
  margin-bottom: 3%;
  margin-left: 35%;
}

.op-btn {
  width: 200px;
  margin: auto;
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

.input-editor {
  margin-right: 4%;
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
