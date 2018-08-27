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
      @click="uploadGame">确认上传</Button>
  </div>
</template>
<script>
import matchingPic from './matching-pic'
import axios from '@/libs/api.request'
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
  props: ['bookid'],
  components: {
    matchingPic
  },
  methods: {
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
    },
    uploadGame () {
      if (this.haveNull()) {
        return
      }
      axios.request({
        url: `books/${this.bookid}/MatchingGame/`,
        data: this.pairs,
        method: 'post'
      }).then(data => {
        this.$Message.info(`上传成功！`)
      })
    }
  },
  mounted () {
    console.log('mounted!')
    axios.request({
      url: `books/${this.bookid}/MatchingGame/`,
      method: 'get'
    }).then(data => {
      console.log(data)
      this.pairs = data
    })
  }
}
</script>
<style>
@import "./common.css";
</style>
