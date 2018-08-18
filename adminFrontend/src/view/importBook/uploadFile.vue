<template>
  <Card title="导入新书" class="import-new-book">
    <div class="flex-cards">
      <Card title="上传书目信息" class="basic-infor">
        <Form :model="currentBook" :label-width="120">
          <FormItem label="选择上传级别" prop="level">
              <Select v-model="currentBook.level" placeholder="选择上传书目所属级别">
                  <Option v-for="item in level_list " :key="item">{{ item }}</Option>
              </Select>
          </FormItem>
          <FormItem label="选择书目类别" prop="type">
              <RadioGroup v-model="currentBook.type">
                  <Radio label="精读">精读</Radio>
                  <Radio label="泛读">泛读</Radio>
              </RadioGroup>
          </FormItem>
          <FormItem label="书目标题" prop="title">
              <Input v-model="currentBook.title" placeholder="书目标题"></Input>
          </FormItem>
          <FormItem label="封面图片" prop="cover">
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
          </FormItem>
          <FormItem label="内容" prop="content">
            <Upload multiple type="drag" class="drag-upload" action="/" :before-upload="handleBeforeUploadContent" :format="['jpg','jpeg','png']">
              <div class="upload-content"  @click="handleUploadContent">
                <Icon type="ios-cloud-upload" size="25" class="upload-cavas"></Icon>
                <p>点击或者拖拽上传文件</p>
              </div>
            </Upload>
          </FormItem>
          <FormItem>
              <Button type="primary" @click="previewModal=true">点击预览</Button>
              <Button type="success" @click="handleSubmit">确认上传</Button>
              <Button type="error" @click="handleReset">重新上传</Button>
          </FormItem>
        </Form>
      </Card>
      <Card title="文件列表" class="book-preview">
        <Row>
          <transition name="fade">
            <Progress v-if="showProgress" :percent="progressPercent" :stroke-width="2">
              <div v-if="progressPercent == 100">
                <Icon type="ios-checkmark-circle"></Icon>
                <span>成功</span>
              </div>
            </Progress>
          </transition>
        </Row>
        <Row>
          <Card class="table-back">
            <Table height="200" :columns="titleList" :data="fileList" class="upload-list" :loading="tableLoading"></Table>
          </Card>
        </Row>
      </Card>
    </div>
    <Modal title="上传预览" v-model="previewModal" :styles="{top: '20px'}">
      <Card title="上传预览">
        <Form :model="currentBook" label-position="top">
          <FormItem label="上传级别">
            <Input v-model="currentBook.level" disabled></Input>
          </FormItem>
          <FormItem label="所属类别">
            <Input v-model="currentBook.type" disabled></Input>
          </FormItem>
          <FormItem label="书目标题">
            <Input v-model="currentBook.title" disabled></Input>
          </FormItem>
          <FormItem label="上传文件列表">
            <Table height="200" :columns="titleList" :data="fileList"></Table>
          </FormItem>
        </Form>
      </Card>
    </Modal>
  </Card>
</template>
<script>
export default {
  name: 'upload-file',
  data () {
    return {
      previewModal: false,
      avatarMode: true,
      showProgress: false,
      progressPercent: 0,
      tableLoading: false,
      file: null,
      level_list: [
        'k1', 'k2', 'k3', 'k4', 'k5', 'k6'
      ],
      type_list: [
        '精读', '泛读'
      ],
      titleList: [
        {
          title: '文件列表',
          key: 'fileName'
        }
      ],
      fileList: [],
      currentBook: {
        cover: '',
        level: '',
        title: '',
        read_type: '',
        pages_number: '',
        assignment: '',
        guidence: ''
      }
    }
  },
  methods: {
    initUpload () {
      this.file = null
    },
    handleUploadPicture () {

    },
    handleUploadContent () {

    },
    handleRemove () {
      this.$Message.info('上传的文件已删除！')
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
    handleBeforeUploadContent (file) {
      const fileExt = file.name.split('.').pop().toLocaleLowerCase()
      if (fileExt === 'jpg' || fileExt === 'pdf' || fileExt === '') {
        this.readFile(file)
        // add the current file to the file list
      } else {
        this.$Notice.warning({
          title: '文件类型错误',
          desc: '文件：' + file.name + '不是jpg/jpeg/png/pdf文件，请选择后缀为.jpg或者.pdf或者.jpeg或者.png的文件。'
        })
      }
      return false
    },
    readFile (file) {
      const reader = new FileReader()
      reader.readAsArrayBuffer(file)
      reader.onloadstart = e => {
        this.tableLoading = true
        this.showProgress = true
        this.progressPercent = 0
      }
      reader.onprogress = e => {
        this.progressPercent = Math.round(e.loaded / e.total * 100)
      }
      reader.onerror = e => {
        this.$Message.error('文件读取出错')
      }
      reader.onload = e => {
        this.$Message.info('文件读取成功')
      }
    },
    handleSubmit () {

    },
    handleReset () {

    }
  },
  created () {

  },
  mounted () {

  }
}
</script>
<style lang="less">
  @import "./common.less";
  .drag-upload {
    width: 40%;
    height: 8%;
  }

  .import-new-book {
    background-color: #e8eaec;
  }

  .flex-cards {
    display: flex;
    flex-direction: row;
    align-items: stretch;
  }

  .basic-infor {
    flex-grow: 2;
    flex-shrink: 2;
    margin-right: 6px;
  }

  .book-preview {
    background-image: url('~@/assets/images/blue1.jpg');
    flex-grow: 1;
    flex-shrink: 1;
    margin-left: 6px;
  }

  .upload-list {
    width: 350px;
  }

  .table-back {
    background-image: url('~@/assets/images/blue2.jpg')
  }

  .upload-camera {
    width: 58px;
    height: 58px;
    line-height: 58px;
  }

  .upload-picture {
    display: inline-block;
    width: 58px;
  }

  .upload-content {
    padding: 10px 0
  }

  .upload-avatar {
    color: #3399ff
  }
</style>
