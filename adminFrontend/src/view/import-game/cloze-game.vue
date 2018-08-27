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
  components: {
  },
  methods: {
    uploadGame () {
      if (this.haveNull()) {
        // return
      }
      // to be added
    },
    insertLine () {
      if (this.sentence === null) {
        this.sentence = ''
      }
      this.sentence += '______'
    }
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
