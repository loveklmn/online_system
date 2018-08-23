<template>
  <Layout class="layout">
    <Content class="pic-content">
      <img class="pagepic" :src="page.picture"> </img>
      <Upload action="//jsonplaceholder.typicode.com/posts/">
          <Button icon="ios-cloud-upload-outline">Upload files</Button>
      </Upload>

    </Content>
    <Content class="sentence-content">
      <sentenceimport
        v-for="sen in page.sentences"
        :key="sen"
        :sentence.sync="sen">
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
</style>
