<template>
  <div>
    <p>上传的图片不需要裁切</p>
    <imgComp :img.sync="img"></imgComp>
    <Button
      class="upload-button"
      type="primary"
      @click="uploadGame">确认上传</Button>
  </div>
</template>
<script>
import imgComp from './img'
export default {
  data () {
    return {
      img: null
    }
  },
  components: {
    imgComp
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
