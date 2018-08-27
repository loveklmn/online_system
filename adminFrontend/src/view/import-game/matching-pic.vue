<template>
  <div>
    <imgComp :img.sync="pair.img"></imgComp>
    <Input v-model="pair.word"/>
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
