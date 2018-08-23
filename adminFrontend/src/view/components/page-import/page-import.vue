<template>
  <Layout class="layout">
    <Content class="pic-content">
      <div v-if="page.picture === null">
        <img id="pic" class="pagepic" :src="defaultPic"/>
      </div>
      <div v-else id="pic-holder" class="pic-holder">
        <img
          id="pic"
          class="pagepic"
          :src="page.picture"
          @click="onmousedown"
          ondragstart="return false;"
          v-on:mousedown="onmousedown"
          v-on:mousemove="onmousemove"
          v-on:mouseup="onmouseup"/>
        <div id="select-box" hidden></div>
      </div>

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
      <!-- <sentenceimport
        v-for="sen in page.sentences"
        :key="sen.id"
        :sentence.sync="sen"
        v-on:deleteSentence="deleteSentence"
        v-on:selectArea="selectArea">
      </sentenceimport> -->

      <Collapse accordion>
        <Panel
          v-for="sen in page.sentences"
          :key="sen.id"
          :name="sen.content">
          {{sen.content}}
          <sentenceimport
            slot="content"
            :sentence.sync="sen"
            v-on:deleteSentence="deleteSentence"
            v-on:selectArea="selectArea">
          </sentenceimport>
        </Panel>
    </Collapse>

    </Content>
  </Layout>
</template>
<script>
import sentenceimport from '@/view/components/sentence-import/sentence-import'
export default {
  data () {
    return {
      defaultPic: require('@/assets/images/addPage.png'),
      x1: 0,
      y1: 0,
      x2: 0,
      y2: 0,
      isSelecting: false,
      curSentence: null
    }
  },
  props: ['page'],
  components: {
    sentenceimport
  },
  computed: {
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
      newSen.content = `新句子${this.page.sentences.length + 1}`
      this.page.sentences.push(newSen)
    },
    deletePage: function () {
      this.$emit('deletePage', this.page.number)
    },
    deleteSentence: function (sentence) {
      let index = this.page.sentences.indexOf(sentence)
      this.page.sentences.splice(index, 1)
      console.log('delete!', index)
    },
    onmousedown: function (e) {
      if (!this.isSelecting) {
        return
      }
      console.log('down!')
      let div = document.getElementById('select-box')
      div.hidden = 0
      this.x1 = e.clientX
      this.y1 = e.clientY
      this.x2 = this.x1
      this.y2 = this.y1
      this.reCalc()
    },
    onmousemove: function (e) {
      if (!this.isSelecting) {
        return
      }
      console.log('move!')
      this.x2 = e.clientX
      this.y2 = e.clientY
      this.reCalc()
    },
    onmouseup: function (e) {
      if (!this.isSelecting) {
        return
      }
      this.isSelecting = false
      console.log('up!')
      let div = document.getElementById('select-box')
      div.hidden = 1
    },
    selectArea: function (sentence) {
      console.log('selectArea is called!')
      this.isSelecting = !this.isSelecting
      this.curSentence = sentence
    },
    reCalc: function () {
      let x1 = this.x1
      let y1 = this.y1
      let x2 = this.x2
      let y2 = this.y2
      console.log(x1, y1, x2, y2)
      let x3 = Math.min(x1, x2)
      let x4 = Math.max(x1, x2)
      let y3 = Math.min(y1, y2)
      let y4 = Math.max(y1, y2)
      let div = document.getElementById('select-box')
      let holder = document.getElementById('pic-holder')
      let rect = holder.getBoundingClientRect()
      let top = rect.top
      let left = rect.left
      div.style.left = x3 - left + 'px'
      div.style.top = y3 - top + 'px'
      div.style.width = x4 - x3 + 'px'
      div.style.height = y4 - y3 + 'px'

      this.curSentence.x1 = x3 - left
      this.curSentence.y1 = y3 - top
      this.curSentence.x2 = x4 - left
      this.curSentence.y2 = y4 - top
    }
  }
}
</script>
<style scoped>
.layout {
  flex-direction: row;
}
.pic-content {
  flex: 2;
}
.pic-holder {
  position: absolute;
}
.sentence-content {
  flex: 1;
  max-height: 560px;
}

.pagepic {
  width: 400px;
  height: 400px;
}
.add-sentence-button {
  margin: auto;
}
#select-box {
    border: 1px dotted #000;
    position: absolute;
}
</style>
