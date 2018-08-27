<template>
  <div>
    <p>请点击下方按钮上传图片，不需要裁切</p>
    <p v-if="img === null">现在还没有上传图片哦</p>
    <img v-else class="img-preview" :src="img"></img>
    <Upload
      class="upload-button"
      name="file"
      :beforeUpload="handleUpload"
      action=""
    >
        <Button icon="ios-cloud-upload-outline">上传图片</Button>
    </Upload>
    <Button
      class="upload-button"
      type="primary"
      @click="uploadGame">确认上传</Button>
  </div>
</template>
<script>
export default {
  data () {
    return {
      img: null
    }
  },
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
    },
    uploadGame () {
      if (this.haveNull()) {
        // return
      }
      // to be added
    }
  }
}
</script>
<style>
@import "./common.css";

</style>
