<template>
  <div>
    <p v-if="pair.img === null">还没上传图片哦</p>
    <img v-else class="img-preview" :src="pair.img"> </img>
    <Upload
      class="upload-button"
      name="file"
      :beforeUpload="handleUpload"
      action=""
    >
        <Button icon="ios-cloud-upload-outline">上传图片</Button>
    </Upload>
    <Input v-model="pair.word"/>
  </div>
</template>
<script>
import upload from '@/api/upload'
import baseURL from '_conf/url'
export default {
  data () {
    return {
    }
  },
  props: ['pair'],
  methods: {
    handleUpload (file) {
      let that = this
      upload(file)
        .then((res) => {
          let savepath = res.savepath
          that.pair.img = baseURL + savepath
        })
        .catch((err) => {
          console.log(err)
        })
      return false
    }
  }
}
</script>
