<style lang="less">
  @import "./common.less";
  .dragUpload {
    width: 50%;
    height: 10%;
  }
</style>
<template>
  <Row>
    <Col>
      <Card title="导入新书">
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
            <Upload multiple type="drag" class="dragUpload" action="/" :before-upload="handleBeforeUpload" :format="['jpg','jpeg','png']">
              <div style="padding: 20px 0" @click="handleUploadPicture">
                <Icon type="ios-cloud-upload" size="25" style="color: #3399ff"></Icon>
                <p>Click or drag files here to upload</p>
              </div>
            </Upload>
          </FormItem>
          <FormItem label="阅读拓展" prop="assignment">
            <Upload multiple type="drag" class="dragUpload" action="" :before-upload="handleBeforeUpload" :format="['pdf','docx','txt']">
              <div style="padding: 20px 0" @click="handleUploadFile">
                <Icon type="ios-cloud-upload" size="25" style="color: #3399ff"></Icon>
                <p>Click or drag files here to upload</p>
              </div>
            </Upload>
          </FormItem>
          <FormItem label="阅读指导" prop="guidence">
            <Upload multiple type="drag" class="dragUpload" action="" :before-upload="handleBeforeUpload" :format="['pdf','docx','txt']">
              <div style="padding: 20px 0" @click="handleUploadFile">
                <Icon type="ios-cloud-upload" size="25" style="color: #3399ff"></Icon>
                <p>Click or drag files here to upload</p>
              </div>
            </Upload>
          </FormItem>
          <FormItem>
              <Button type="success" @click="handleSubmit">确认上传</Button>
              <Button type="primary" @click="previewModal=true" style="margin-left: 8px">点击预览</Button>
              <Button type="error" @click="handleReset" style="margin-left: 8px">重新上传</Button>
          </FormItem>
        </Form>
      </Card>
    </Col>
    <Modal
        title="上传预览"
        v-model="previewModal"
        :styles="{top: '20px'}">
        <Card title="上传预览">
        <Form :model="currentBook" label-position="top">
          <FormItem label="书目级别">
            <Input v-model="currentBook.level" disabled></Input>
          </FormItem>
          <FormItem label="书目类别">
            <Input v-model="currentBook.type" disabled></Input>
          </FormItem>
          <FormItem label="书目标题">
            <Input v-model="currentBook.title" disabled></Input>
          </FormItem>
          <FormItem label="阅读拓展文件列表">
            <Table height="200" :columns="listTitle" :data="fileList1"></Table>
          </FormItem>
          <FormItem label="亲子指导文件列表">
            <Table height="200" :columns="listTitle" :data="fileList2"></Table>
          </FormItem>
        </Form>
      </Card>
    </Modal>
  </Row>
</template>
<script>
export default {
  name: 'upload-file',
  data () {
    return {
      previewModal: false,
      assignMode: true,
      level_list: [
        'k1', 'k2', 'k3', 'k4', 'k5', 'k6'
      ],
      type_list: [
        '精读', '泛读'
      ],
      listTitle: [
        {
          title: '文件列表',
          key: 'fileName'
        }
      ],
      fileList1: [],
      fileList2: [],
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
    handleUploadFile () {
      initUpload()
    },
    handleUploadPicture () {
      // pass
    },
    handleRemove () {
      this.$Message.info('上传的文件已删除！')
    },
    handleBeforUploadPicture (file) {
      const fileExt = file.name.split('.').pop().toLocaleLowerCase()
      if (fileExt === 'jpg' || fileExt === 'jpeg' || fileExt === 'png') {
        // set cover for the current_book
      } else {
        this.$Notice.warning({
          title: '文件类型错误',
          desc: '文件：' + file.name + '不是jpg/jpeg/png文件，请选择后缀为.jpeg或者.jpg或者png的图片文件。'
        })
      }
    },
    handleBeforeUploadText (file) {
      const fileExt = file.name.split('.').pop().toLocaleLowerCase()
      if (fileExt === 'txt' || fileExt === 'pdf' || fileExt === 'docx') {
        // if (assignMode): add file to the list of assignment
        // else: add file to the list of guidence
      } else {
        this.$Notice.warning({
          title: '文件类型错误',
          desc: '文件：' + file.name + '不是txt/docx/pdf文件，请选择后缀为.txt或者.pdf或者.docx的文本文件。'
        })
      }
      return false
    },
    readFile (file) {
      const reader = new FileReader()
      reader.readAsArrayBuffer(file)
      reader.onloadstart = e => {
        // something to do at this stage
      }
      reader.onerror = e => {
        this.$Message.error('文件读取出错')
      }
      reader.onload = e => {
        // pass
      }
    },
    handleSubmit () {
      // handle form submit event
    },
    handleCache () {
      // handle form cache event
    },
    handleReset () {
      // handle reset event
    }
  },
  created () {
  },
  mounted () {
  }
}
</script>
