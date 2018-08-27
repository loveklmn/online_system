<template>
  <div>
    <Row  :gutter="72">
        <Col
          v-for="(item,index) in pairs"
          :key="index"
          span="8">
          <matchingPic :pair.sync="item">
          </matchingPic>
        </Col>
    </Row>
    <Button
      class="upload-button"
      type="primary"
      @click="upload">确认上传</Button>
  </div>
</template>
<script>
import matchingPic from './matching-pic'
// import axios from '@/libs/api.request'
export default {
  data () {
    return {
      pairs: [
        {img: null, word: null},
        {img: null, word: null},
        {img: null, word: null}
      ]
    }
  },
  components: {
    matchingPic
  },
  methods: {
    upload () {
      if (this.haveNull()) {
        return
      }
      // to be added
    },
    haveNull () {
      for (let i = 0; i < 3; i += 1) {
        if (this.pairs[i].img === null) {
          this.$Message.info(`第${i + 1}组没有上传图片哦`)
          return true
        }
        if (this.pairs[i].word === null) {
          this.$Message.info(`第${i + 1}组没有上传单词哦`)
          return true
        }
      }
      return false
    }
  }
}
</script>
<style>
.upload-button {
  margin-top: 50px;
}
</style>
