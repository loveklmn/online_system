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
    }
  },
  created () {
    this.bookid = this.$route.params.id
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
