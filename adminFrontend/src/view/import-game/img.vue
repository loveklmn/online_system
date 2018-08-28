<template>
  <div>
    <p v-if="img === null">现在还没有上传图片哦，可以点击下方按钮上传图片</p>
    <img v-else class="img-preview" :src="baseURL + img"/>
    <Upload
      class="upload-button"
      name="file"
      :beforeUpload="handleUpload"
      action=""
      accept="image/*"
    >
        <Button icon="ios-cloud-upload-outline">上传图片</Button>
    </Upload>
  </div>
</template>
<script>
import upload from '@/api/upload'
import baseURL from '_conf/url'
export default {
  data () {
    return {
      baseURL: baseURL
    }
  },
  props: ['img'],
  watch: {
  },
  methods: {
    handleUpload (file) {
      upload(file)
        .then((res) => {
          let savepath = res.savepath
          this.$emit('update:img', savepath)
        })
        .catch((err) => {
          console.log(err)
        })
      return false
    }
  }
}
</script>
