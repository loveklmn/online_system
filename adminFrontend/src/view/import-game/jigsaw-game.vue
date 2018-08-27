<template>
  <div id="test">
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
    handleUpload: function (file) {
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
    uploadGame: function () {
      this.slice()
      // if (this.haveNull()) {
      //   // return
      // }
      // to be added
    },
    slice: function () {
      this.getBase64Image(this.img, (url) => {
        console.log(url)
        // this.split_4(url)
        let img = new Image()
        img.onload = this.split_4
        img.src = url
      })
    },
    getBase64Image: function (imgUrl, callback) {
      let img = new Image()
      // onload fires when the image is fully loadded, and has width and height
      img.onload = function () {
        let canvas = document.createElement('canvas')
        canvas.width = img.width
        canvas.height = img.height
        let ctx = canvas.getContext('2d')
        ctx.drawImage(img, 0, 0)
        let dataURL = canvas.toDataURL('image/png')
        // dataURL = dataURL.replace(/^data:image\/(png|jpg);base64,/, '')
        callback(dataURL) // the base64 string
      }
      // set attributes and src
      img.setAttribute('crossOrigin', 'anonymous')
      img.src = imgUrl
    },
    split_4: function (e) {
      let img = e.currentTarget
      let parts = []
      let w2 = img.width / 3 // 130
      let h2 = img.height / 3 // 40
      console.log(w2, h2)
      for (let i = 0; i < 9; i++) {
        let ty = parseInt(i / 3)
        let x = (-w2 * i) % (w2 * 3)
        let y = -ty * h2
        let canvas = document.createElement('canvas') // In memory canvas
        let ctx = canvas.getContext('2d')
        canvas.width = w2
        canvas.height = h2
        ctx.drawImage(img, x, y, w2 * 3, h2 * 3) // img, x, y, w, h
        parts.push(canvas.toDataURL()) // ("image/jpeg") for jpeg
        // ---------- JUST TO TEST
        let slicedImage = document.createElement('img')
        slicedImage.src = parts[i]
        let div = document.getElementById('test')
        div.appendChild(slicedImage)
        // ----------
      }
      console.log(parts)
    }
  }
}
</script>
<style>
@import "./common.css";

</style>
