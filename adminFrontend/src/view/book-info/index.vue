<template>
<div class="book-info">
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
              <Input v-model="newBook.title" placeholder="书目标题" />
            </FormItem>
            <FormItem label="所在级别">
              <InputNumber :max="10" :min="1" v-model="newBook.level"></InputNumber>
            </FormItem>
            <FormItem label="所属类别" prop="type">
              <RadioGroup v-model="newBook.read_type">
                <Radio label="IR">精读</Radio>
                <Radio label="ER">泛读</Radio>
              </RadioGroup>
            </FormItem>
            <Button type="primary" class="new-book-btn" @click="save" :loading="loading">保存修改</Button>
            <Button type="warning" class="modify-btn" @click="decline">取消修改</Button>
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
    <Card title="功能入口">
      <div class="function-entrance">
        <Button shape="circle" class="level-icon">
          <Icon type="md-aperture" />
          <p>亲子阅读指导</p>
        </Button>
        <Button shape="circle" class="level-icon">
          <Icon type="md-aperture" />
          <p>阅读拓展导入</p>
        </Button>
        <Button shape="circle" class="level-icon">
          <Icon type="ios-aperture" />
          <p>游戏素材导入</p>
        </Button>
        <Button shape="circle" class="level-icon">
          <Icon type="ios-aperture" />
          <p>E-book导入</p>
        </Button>
      </div>
    </Card>
  </div>
</div>
</template>
<script>
import axios from '@/libs/api.request'
import upload from '@/api/upload'
import baseURL from '_conf/url'

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
        id: 0,
        title: '',
        level: '',
        read_type: '',
        cover: '',
        pages_num: '',
        assignment: '',
        guidance: ''
      },
      newBook: {
        id: 0,
        title: '',
        level: '',
        read_type: '',
        cover: '',
        pages_num: '',
        assignment: '',
        guidance: ''
      }
    }
  },
  created () {
    axios.request({
      url: 'books/',
      method: 'post',
      data: {
        id: this.$route.params.id
      }
    }).then(data => {
      this.currentBook = data
      this.newBook = Object.assign({}, this.currentBook)
    })
  },
  computed: {
  },
  methods: {
    modify () {
      this.modifyMode = true
    },
    decline () {
      this.newBook = Object.assign({}, this.currentBook)
      this.modifyMode = false
    },
    save () {
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
  width:90%;
  height: 80%;
  .top-part {
    flex-grow: 2;
    margin-top: 2%;
    margin-bottom:2%;
    .basic-info {
      .query-book {
        display: flex;
        flex-direction: row;
        .cover {
          min-width: 130px;
        }
        .book-cover {
          display: block;
          max-width: 130px;
          max-height: 200px;
          width: auto;
          height: auto;
        }
        .book-detail {
          flex-grow: 3;
          .book-title {
            font-size: 20px;
            margin-left: 7%;
          }
          .book-else-title {
            font-size: 16px;
            margin-top: 2%;
            margin-left: 7%;
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
          min-width: 130px;
          max-width: 130px;
          max-height: 200px;
          width: auto;
          height: auto;
        }
        .new-detail {
          width: 50px;
          flex-grow: 3;
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