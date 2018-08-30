<template>
<div>
  <imgComp :img.sync="img"></imgComp>
  <p>请在下方输入图片对应的单词（即正确答案）</p>
  <Input class="word-input" v-model="correct_word" placeholder="word"/>
  <p>请在下方输入两个干扰项</p>
  <Input class="word-input" v-model="wrong_word_1" placeholder="第一个干扰项"/>
  <Input class="word-input" v-model="wrong_word_2" placeholder="第二个干扰项"/>
  <Button
    class="upload-button"
    type="primary"
    @click="uploadGame">确认上传</Button>
  <Button class="upload-button" type="warning" @click="handleReset">返回</Button>
</div>
</template>
<script>
import imgComp from './img'
import axios from '@/libs/api.request'
export default {
  data () {
    return {
      img: null,
      correct_word: null,
      wrong_word_1: null,
      wrong_word_2: null
    }
  },
  props: ['bookid'],
  components: {
    imgComp
  },
  methods: {
    haveNull () {
      if (this.img === null) {
        return true
      }
      if (this.correct_word === null) {
        return true
      }
      if (this.wrong_word_1 === null) {
        return true
      }
      if (this.wrong_word_2 === null) {
        return true
      }
    },
    uploadGame () {
      if (this.haveNull()) {
        return
      }
      axios.request({
        url: `books/${this.bookid}/RecognitionGame/`,
        data: {
          img: this.img,
          correct_word: this.correct_word,
          wrong_word_1: this.wrong_word_1,
          wrong_word_2: this.wrong_word_2
        },
        method: 'post'
      }).then(data => {
        this.$Message.info(`上传成功！`)
      })
    },
    handleReset () {
      this.$router.go(-1)
    }
  },
  created () {
    let loader = this.$loading.show()
    this.bookid = this.$route.params.id
    axios.request({
      url: `books/${this.bookid}/RecognitionGame/`,
      method: 'get'
    }).then(data => {
      this.img = data.img
      this.correct_word = data.correct_word
      this.wrong_word_1 = data.wrong_word_1
      this.wrong_word_2 = data.wrong_word_2
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

.word-input {
  display: block;
  width: 50%;
}
</style>
