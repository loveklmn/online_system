<template>
<div>
  <p>请在下方输入待填空的段落</p>
  <Input class="word-input" v-model="sentence" placeholder="paragraph"/>
  <Button @click="insertLine">插入下划线</Button>
  <p>请在下方输入正确答案</p>
  <Input class="word-input" v-model="correct_word" placeholder="word"/>
  <p>请在下方输入三个干扰项</p>
  <Input class="word-input" v-model="wrong_word_1" placeholder="第一个干扰项"/>
  <Input class="word-input" v-model="wrong_word_2" placeholder="第二个干扰项"/>
  <Input class="word-input" v-model="wrong_word_3" placeholder="第三个干扰项"/>
  <Button
    class="upload-button"
    type="primary"
    @click="uploadGame">确认上传</Button>
</div>
</template>
<script>
import axios from '@/libs/api.request'
export default {
  data () {
    return {
      sentence: null,
      correct_word: null,
      wrong_word_1: null,
      wrong_word_2: null,
      wrong_word_3: null
    }
  },
  props: ['bookid'],
  components: {
  },
  methods: {
    haveNull () {
      if (this.sentence === null) {
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
      if (this.wrong_word_3 === null) {
        return true
      }
    },
    uploadGame () {
      if (this.haveNull()) {
        return
      }
      axios.request({
        url: `books/${this.bookid}/ClozeGame/`,
        data: {
          sentence: this.sentence,
          correct_word: this.correct_word,
          wrong_word_1: this.wrong_word_1,
          wrong_word_2: this.wrong_word_2,
          wrong_word_3: this.wrong_word_3
        },
        method: 'post'
      }).then(data => {
        this.$Message.info(`上传成功！`)
      })
    },
    insertLine () {
      if (this.sentence === null) {
        this.sentence = ''
      }
      this.sentence += '______'
    }
  },
  created () {
    let loader = this.$loading.show()
    this.bookid = this.$route.params.id
    axios.request({
      url: `books/${this.bookid}/ClozeGame/`,
      method: 'get'
    }).then(data => {
      this.sentence = data.sentence
      this.correct_word = data.correct_word
      this.wrong_word_1 = data.wrong_word_1
      this.wrong_word_2 = data.wrong_word_2
      this.wrong_word_3 = data.wrong_word_3
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
