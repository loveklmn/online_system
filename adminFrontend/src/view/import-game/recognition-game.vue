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
export default {
  data () {
    return {
      img: null,
      correct_word: null,
      wrong_word_1: null,
      wrong_word_2: null
    }
  },
  components: {
    imgComp
  },
  uploadGame () {
    if (this.haveNull()) {
      // return
    }
    // to be added
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
