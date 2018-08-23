<template>
<div class="book-info">
  <div class="top-part">
    <div class="basic-info">
      <div v-if="modifyMode" class="query-book">
        <Card title="封面" class="book-cover">
          <img src='currentBook.cover' />
        </Card>
        <Card title="基本信息" class="book-detail">
          <h2 class="book-title">{{ currentBook.title }}</h2>
          <h4 class="book-else-title">级别:&nbsp;&nbsp;{{ currentBook.level }}</h4>
          <h4 class="book-else-title">{{ currentBook.read_type === 'ER' ? '精读书目' : '泛读书目'}}</h4>
          <h4 class="book-else-title">{{ currentBook.pages_num }}&nbsp;&nbsp;页</h4>
          <Button type="warning" @click="modifyInfo" class="modify-btn">修改基本信息</Button>
        </Card>
      </div>
      <div v-if="newMode" class="new-book">
        <Card title="封面" class="new-cover">
          <Upload
            ref="upload"
            :format="['jpg','jpeg','png']"
            :max-size="2048"
            :before-upload="handleBeforeUploadPicture"
            type="drag"
            action=""
            class="upload-picture">
            <div class="upload-camera" @click="handleUploadPicture">
              <Icon type="ios-camera" size="20"></Icon>
            </div>
          </Upload>
        </Card>
        <Card title="基本信息" class="new-detail">
          <Form :model="currentBook" :label-width="120">
            <FormItem label="标题:" prop="title">
              <Input v-model="currentBook.title" placeholder="书目标题" />
            </FormItem>
            <FormItem label="所在级别" prop="level">
              <Select v-model="currentBook.level" placeholder="选择上传书目所属级别">
                  <Option v-for="item in level_list " :key="item">{{ item }}</Option>
              </Select>
            </FormItem>
            <FormItem label="所属类别" prop="type">
              <RadioGroup v-model="bookType">
                <Radio label="精读">精读</Radio>
                <Radio label="泛读">泛读</Radio>
              </RadioGroup>
            </FormItem>
            <Button type="primary" class="new-book-btn" @click="handleNewBookInfo">创建</Button>
          </Form>
        </Card>
      </div>
    </div>
  </div>
  <div class="bottom-part">
    <Card title="功能入口">
      <div class="function-entrance">
        <Button shape="circle" class="level-icon" @click="turnToGuidance">
          <Icon type="md-aperture" />
          <p>亲子阅读指导</p>
        </Button>
        <Button shape="circle" class="level-icon" @click="turnToAssignment">
          <Icon type="md-aperture" />
          <p>阅读拓展导入</p>
        </Button>
        <Button shape="circle" class="level-icon" @click="turnToGame">
          <Icon type="ios-aperture" />
          <p>游戏素材导入</p>
        </Button>
        <Button shape="circle" class="level-icon" @click="turnToEbook">
          <Icon type="ios-aperture" />
          <p>E-book导入</p>
        </Button>
      </div>
    </Card>
  </div>
</div>
</template>
<script>
import './format.less'
export default {
  name: 'bookDetail',
  data () {
    return {
      newMode: false,
      modifyMode: true,
      cover: '',
      bookType: '',
      currentBook: {
        id: 0,
        title: 'hello world',
        level: 'k1',
        read_type: 'ER',
        cover: '',
        pages_num: 30,
        assignment: '',
        guidance: ''
      },
      level_list: [
        'k1', 'k2', 'k3', 'k4', 'k5', 'k6'
      ]
    }
  },
  created () {
    if (this.$route.query.book) {
      this.currentBook = this.$route.query.book
      this.modifyMode = true
      this.newMode = false
    } else {
      this.newMode = true
      this.modifyMode = false
      this.$Message.success('创建新书状态')
    }
  },
  mounted: function () {
  },
  computed: {
  },
  methods: {
    turnToGuidance () {
      this.$router.push({
        name: 'import_guidance',
        query: this.currentBook
      })
    },
    turnToAssignment () {
      this.$router.push({
        name: 'import_assignment',
        query: this.currentBook
      })
    },
    turnToGame () {
      this.$router.push({
        name: 'import_game',
        query: this.currentBook
      })
    },
    turnToEbook () {
      this.$router.push({
        name: 'import_Ebook',
        query: this.currentBook
      })
    },
    modifyInfo () {
      this.newMode = true
      this.modifyMode = false
    },
    handleBeforeUploadPicture (file) {
      const fileExt = file.name.split('.').pop().toLocaleLowerCase()
      if (fileExt === 'jpg' || fileExt === 'jpeg' || fileExt === 'png') {
        this.readFile(file)
        // set currentBook.avatar
      } else {
        this.$Notice.warning({
          title: '文件类型错误',
          desc: '文件：' + file.name + '不是jpg/jpeg/png文件，请选择后缀为.jpeg或者.jpg或者png的文件。'
        })
      }
    },
    readFile (file) {
      const reader = new FileReader()
      reader.readAsArrayBuffer(file)
      reader.onerror = e => {
        this.$Message.error('文件读取出错')
      }
      reader.onload = e => {
        console.log(file)
        this.currentBook.cover = file
        this.$Message.info('文件读取成功')
      }
    },
    handleUploadPicture () {
      this.$Message.success('开始上传')
    },
    handleNewBookInfo () {
      if (this.bookType === '精读') {
        this.currentBook.read_type = 'ER'
      } else {
        this.currentBook.read_type = 'IR'
      }
    }
  }
}
</script>
