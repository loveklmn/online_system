<template>
  <Layout class="layout">
    <Content class="pic-content">
      <img class="pagepic" :src="page.picture"> </img>
      <Upload action="//jsonplaceholder.typicode.com/posts/">
          <Button icon="ios-cloud-upload-outline">Upload files</Button>
      </Upload>
      <Button
        type="error"
        @click="deletePage">删除该页面</Button>

    </Content>
    <Content class="sentence-content">
      <Button
        long
        class="add-sentence-button"
        @click="addNewSentence"> 添加新句子 </Button>
      <sentenceimport
        v-for="sen in page.sentences"
        :key="sen.content"
        :sentence.sync="sen"
        v-on:deleteSentence="deleteSentence">
      </sentenceimport>
    </Content>
  </Layout>
</template>
<script>
import sentenceimport from '@/view/components/sentence-import/sentence-import'
export default {
  props: ['page'],
  components: {
    sentenceimport
  },
  methods: {
    addNewSentence: function () {
      let newSen = {
        content: null,
        audio: null,
        translated: null,
        x1: null,
        y1: null,
        x2: null,
        y2: null
      }
      this.page.sentences.push(newSen)
    },
    deletePage: function () {
      this.$emit('deletePage', this.page.num)
    },
    deleteSentence: function (sentence) {
      let index = this.page.sentences.indexOf(sentence)
      this.page.sentences.splice(index, 1)
      console.log('delete!', index)
    }
  }
}
</script>
<style scoped>
.layout {
  flex-direction: row
}
.pic-content {
  flex: 2;
}
.sentence-content {
  flex: 1;
  height: 100px;
}

.pagepic {
  width: 400px;
  height: 400px;
}
.add-sentence-button {
  margin: auto;
}
</style>
