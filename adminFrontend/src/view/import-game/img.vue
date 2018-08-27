<template>
  <div>
    <p v-if="img === null">现在还没有上传图片哦，可以点击下方按钮上传图片</p>
    <img v-else class="img-preview" :src="img"/>
    <Upload
      class="upload-button"
      name="file"
      :beforeUpload="handleUpload"
      action=""
    >
        <Button icon="ios-cloud-upload-outline">上传图片</Button>
    </Upload>
  </div>
</template>
<script>
import upload from '@/api/upload'
import baseURL from '_conf/url'
export default {
  props: ['img'],
  methods: {
    handleUpload (file) {
      let that = this
      upload(file)
        .then((res) => {
          let savepath = res.savepath
          that.img = baseURL + savepath
        })
        .catch((err) => {
          console.log(err)
        })
      return false
    }
  }
}
</script>
<style>
</style>
