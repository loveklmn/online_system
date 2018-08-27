<template>
  <div>
    <imgComp :img.sync="pair.img"></imgComp>
    <p>请在下方输入图片对应的单词</p>
    <Input v-model="pair.word" placeholder="word"/>
  </div>
</template>
<script>
import imgComp from './img'
export default {
  data () {
    return {
    }
  },
  components: {
    imgComp
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
