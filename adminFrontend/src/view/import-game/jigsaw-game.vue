<template>
  <div id="test">
    <div v-if="urlsReady" class="preview-div">
      <img
        v-for="item in urls"
        :key="item"
        :src="baseURL + item"
        class="pic"/>
    </div>
    <div v-else>
      <p>上传的图片不需要裁切</p>
      <imgComp :img.sync="img"></imgComp>
      <Button
        v-if="img !== null"
        class="upload-button"
        type="primary"
        @click="slice">裁切</Button>
    </div>
    <Button
      class="upload-button"
      type="warning"
      @click="uploadAgain">重新上传</Button>
    <Button
      class="upload-button"
      type="primary"
      @click="uploadGame">确认上传</Button>
    <Button class="upload-button" type="warning" @click="handleReset">返回</Button>
  </div>
</template>
<script>
import upload from '@/api/upload'
import baseURL from '_conf/url'
import imgComp from './img'
import axios from '@/libs/api.request'
export default {
  data () {
    return {
      baseURL: baseURL,
      img: null,
      parts: [],
      files: [],
      urlsReady: false,
      imgReady: false,
      loader: null,
      urls: {
        1: null,
        2: null,
        3: null,
        4: null,
        5: null,
        6: null,
        7: null,
        8: null,
        9: null
      }
    }
  },
  props: ['bookid'],
  components: {
    imgComp
  },
  methods: {
    upload: function (file, index) {
      let that = this
      upload(file)
        .then((res) => {
          let savepath = res.savepath
          that.urls[index] = savepath
          if (!this.haveNull()) {
            this.loader.hide()
            this.urlsReady = true
          }
        })
      return false
    },
    handleReset () {
      this.$router.go(-1)
    },
    haveNull: function () {
      for (let i = 1; i <= 9; i++) {
        if (this.urls[i] === null) {
          return true
        }
      }
      return false
    },
    uploadAgain: function () {
      this.urlsReady = false
    },
    uploadGame: function () {
      if (this.haveNull()) {
        this.$Message.info('还有图片没有加载好哦')
        return
      }
      axios.request({
        url: `books/${this.bookid}/JigsawGame/`,
        data: this.urls,
        method: 'post'
      }).then(data => {
        this.$Message.info(`上传成功！`)
      })
    },
    slice: function () {
      this.loader = this.$loading.show()
      for (let i = 1; i <= 9; i++) {
        this.urls[i] = null
      }
      this.getBase64Image(this.img, (url) => {
        let img = new Image()
        img.onload = this.split
        img.src = url
      })
    },
    getBase64Image: function (imgUrl, callback) {
      imgUrl = baseURL + imgUrl
      let img = new Image()
      img.onload = function () {
        let canvas = document.createElement('canvas')
        canvas.width = img.width
        canvas.height = img.height
        let ctx = canvas.getContext('2d')
        ctx.drawImage(img, 0, 0)
        let dataURL = canvas.toDataURL('image/png')
        callback(dataURL)
      }
      img.setAttribute('crossOrigin', 'anonymous')
      img.src = imgUrl
    },
    split: function (e) {
      let img = e.currentTarget
      let parts = []
      let w2 = img.width / 3
      let h2 = img.height / 3
      for (let i = 0; i < 9; i++) {
        let ty = parseInt(i / 3)
        let x = (-w2 * i) % (w2 * 3)
        let y = -ty * h2
        let canvas = document.createElement('canvas')
        let ctx = canvas.getContext('2d')
        canvas.width = w2
        canvas.height = h2
        ctx.drawImage(img, x, y, w2 * 3, h2 * 3)
        parts.push(canvas.toDataURL())
      }
      this.parts = parts
      for (let i = 0; i < 9; i++) {
        this.files[i] = this.dataURLtoFile(this.parts[i], `${i}.png`)
        this.upload(this.files[i], i + 1)
      }
    },
    dataURLtoFile: function (dataurl, filename) {
      let arr = dataurl.split(',')
      let mime = arr[0].match(/:(.*?);/)[1]
      let bstr = atob(arr[1])
      let n = bstr.length
      let u8arr = new Uint8Array(n)
      while (n--) {
        u8arr[n] = bstr.charCodeAt(n)
      }
      return new File([u8arr], filename, {type: mime})
    }
  },
  created () {
    let loader = this.$loading.show()
    this.bookid = this.$route.params.id
    axios.request({
      url: `books/${this.bookid}/JigsawGame/`,
      method: 'get'
    }).then(data => {
      for (let i = 1; i <= 9; i++) {
        this.urls[i] = data[i]
      }
      this.urlsReady = true
      loader.hide()
    }).catch((err) => {
      if (err.response.status !== 404) {
        this.$Message.info('出现了网络问题，请稍后尝试')
      }
      loader.hide()
    })
  }
}
</script>
<style>
@import "./common.css";

.preview-div {
  display: flex;
  flex-wrap: wrap;
  max-width: 400px;
}

.pic {
  width: 30%;
  padding: 0;
  margin: 1%;
}
</style>
