<template>
<content-layout title="图书详情">
<div class="book-info" slot="content">
  <div class="top-part">
    <div class="basic-info">
      <div v-if="!modifyMode" class="query-book">
        <Card title="基本信息" class="book-detail">
          <h2 class="book-title">{{ currentBook.title }}</h2>
          <h4 class="book-else-title">级别:&nbsp;&nbsp;{{ currentBook.level }}</h4>
          <h4 class="book-else-title">{{ currentBook.read_type === 'IR' ? '精读书目' : '泛读书目'}}</h4>
          <h4 class="book-else-title">共&nbsp;&nbsp;{{ currentBook.pages_num }}&nbsp;&nbsp;页</h4>
          <Button type="warning" @click="modify" class="modify-btn">修改基本信息</Button>
        </Card>
        <Card class="cover" title="封面" >
          <img class="book-cover" :src="preview(currentBook.cover)" />
        </Card>
      </div>
      <div v-if="modifyMode" class="new-book">
        <Card title="基本信息" class="new-detail">
          <Form :model="newBook" :label-width="120">
            <FormItem label="标题:" prop="title">
              <Input v-model="newBook.title" placeholder="书目标题" class="input-title"/>
            </FormItem>
            <FormItem label="所在级别">
              <InputNumber :max="9" :min="1" v-model="newBook.level"></InputNumber>
            </FormItem>
            <FormItem label="所属类别" prop="type">
              <RadioGroup v-model="newBook.read_type">
                <Radio label="IR">精读</Radio>
                <Radio label="ER">泛读</Radio>
              </RadioGroup>
            </FormItem>
            <Button type="primary" class="new-book-btn" @click="save" :loading="loading">保存修改</Button>
            <Button type="warning" class="cancel-new-book-btn" @click="decline">取消修改</Button>
          </Form>
        </Card>
        <Card title="封面">
          <Upload
            ref="upload"
            :format="['jpg','jpeg','png']"
            type="drag"
            :beforeUpload="upload"
            action="">
            <Button :loading="uploading">
              <img class="book-cover" :src="preview(newBook.cover)" />
            </Button>
          </Upload>
        </Card>
      </div>
    </div>
  </div>
  <div class="bottom-part">
    <Card v-if="!modifyMode" title="功能入口">
      <div class="function-entrance">
          <Button :to="`/book/${currentBook.id}/guidance`" shape="circle" class="level-icon" type="primary">
            亲子阅读指导
          </Button>
          <Button :to="`/book/${currentBook.id}/assignment`" shape="circle" class="level-icon" type="primary">
            阅读拓展导入
          </Button>
          <Button :to="`/book/${currentBook.id}/game`" shape="circle" class="level-icon" type="primary">
            游戏素材导入
          </Button>
          <Button :to="`/book/${currentBook.id}/ebook`" shape="circle" class="level-icon" type="primary">
            E-book导入
          </Button>
      </div>
    </Card>
  </div>
  <backhome-btn
    back="/book/list"
    name="书目列表"></backhome-btn>
</div>
</content-layout>
</template>
<script>
import axios from '@/libs/api.request'
import upload from '@/api/upload'
import baseURL from '_conf/url'
import contentLayout from '_c/content-layout'
import backhomeBtn from '_c/backhome-btn'
export default {
  data () {
    return {
      baseURL: baseURL,
      loading: false,
      uploading: false,
      modifyMode: false,
      cover: '',
      bookType: '',
      currentBook: {
        id: -1,
        title: '',
        level: null,
        read_type: '',
        cover: '',
        pages_num: 0,
        assignment: '',
        guidance: '<div></div>'
      },
      newBook: {
        id: -1,
        title: '',
        level: null,
        read_type: '',
        cover: '',
        pages_num: 0,
        assignment: '',
        guidance: '<div></div>'
      }
    }
  },
  components: {
    contentLayout,
    backhomeBtn
  },
  beforeRouteEnter (to, from, next) {
    let id = parseInt(to.params.id)
    if (id !== -1) {
      axios.request({
        url: 'books/',
        method: 'post',
        data: {
          id: id
        }
      }).then(data => {
        next(vm => {
          vm.id = id
          vm.currentBook = data
          vm.newBook = Object.assign({}, vm.currentBook)
        })
      })
    } else {
      next(vm => {
        vm.id = id
        vm.modifyMode = true
      })
    }
  },
  methods: {
    modify () {
      this.modifyMode = true
    },
    decline () {
      if (this.id === -1) {
        this.$router.go(-1)
      } else {
        this.newBook = Object.assign({}, this.currentBook)
        this.modifyMode = false
      }
    },
    save () {
      let id = parseInt(this.$route.params.id)
      if (id === -1) {
        if (!this.newBook.title || !this.newBook.level || !this.newBook.cover || !this.newBook.read_type) {
          this.$Message.error('请填写完整的信息')
        } else {
          this.loading = true
          axios.request({
            url: 'books/',
            method: 'post',
            data: this.newBook
          }).then((data) => {
            this.loading = false
            this.$Message.success('修改已保存')
            this.$router.replace({
              path: '/book/' + data.id
            })
            this.newBook.id = data.id
            this.currentBook = Object.assign({}, this.newBook)
            this.modifyMode = false
          })
        }
      } else {
        this.loading = true
        axios.request({
          url: 'books/',
          method: 'post',
          data: this.newBook
        }).then((data) => {
          this.currentBook = data
          this.newBook = Object.assign({}, this.currentBook)
          this.loading = false
          this.modifyMode = false
        })
      }
    },
    upload (file) {
      this.uploading = true
      upload(file).then(data => {
        this.newBook.cover = data.savepath
        setTimeout(() => {
          this.uploading = false
        }, 2000)
      })
      return false
    },
    preview (url) {
      return url ? baseURL + url : ''
    }
  }
}
</script>

<style lang="less" scoped>
.book-info {
  display: flex;
  flex-direction: column;
  width: 95%;
  height: 80%;
  margin-left: 3%;
  margin-right: 3%;
  .top-part {
    flex-grow: 2;
    margin-top: 2%;
    margin-bottom: 2%;

    .basic-info {
      .query-book {
        display: flex;
        flex-direction: row;

        .cover {
          min-width: 130px;
          flex: 3;
        }

        .book-cover {
          display: block;
          width: auto;
          max-width: 130px;
          height: auto;
          max-height: 200px;
          margin: auto;
        }

        .book-detail {
          flex-grow: 8;

          .book-title {
            margin-left: 7%;
            font-size: 20px;
          }

          .book-else-title {
            margin-top: 2%;
            margin-left: 7%;
            font-size: 16px;
          }

          .modify-btn {
            margin-top: 2%;
            margin-left: 7%;
          }
        }
      }

      .new-book {
        display: flex;
        flex-direction: row;

        .book-cover {
          display: block;
          width: auto;
          min-width: 130px;
          max-width: 130px;
          height: auto;
          max-height: 200px;
        }

        .new-detail {
          flex-grow: 3;
          width: 50px;
          .input-title {
            width: 40%;
          }
        }

        .new-book-btn {
          margin: auto;
        }

        .cancel-new-book-btn {
          margin: auto;
        }
      }
    }
  }

  .bottom-part {
    flex-grow: 2;
    margin-bottom: 2%;

    .function-entrance {
      display: flex;
      flex-direction: row;

      .level-icon {
        flex-grow: 1;
        margin: 3%;
      }
    }
  }
}

.upload-picture {
  width: 50%;
  height: 50%;
  margin-top: 20%;
  margin-left: 20%;
}

</style>
