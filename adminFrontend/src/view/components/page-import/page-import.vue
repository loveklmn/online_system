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
        <div
          id="select-box"
          :style="{
            left: x1 + 'px',
            top: y1 + 'px',
            width: (x2 - x1) + 'px',
            height: (y2 - y1) + 'px'}"></div>
      </div>

      <Upload class="upload-button" action="//jsonplaceholder.typicode.com/posts/">
          <Button icon="ios-cloud-upload-outline">上传本页对应的图片</Button>
      </Upload>
      <Button
        type="error"
        class="delete-button"
        @click="deletePage">删除该页面</Button>

    </Content>
    <Content class="sentence-content">
      <Button
        long
        class="add-sentence-button"
        @click="addNewSentence"> 添加新句子 </Button>

      <Collapse v-model="curSenIndexChar" accordion>
        <Panel
          v-for="(sen, index) in page.sentences"
          :key="sen.id"
          :name="index.toString()">
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
      // x1: 0,
      // y1: 0,
      // x2: 0,
      // y2: 0,
      xstart: 0,
      ystart: 0,
      xend: 0,
      yend: 0,
      canSelect: false,
      isSelecting: false,
      // curSentence: null,
      // curSenIndex: -1,
      curSenIndexChar: '-1',
      selectBox: null,
      offsetLeft: 0,
      offsetTop: 0
    }
  },
  props: ['page'],
  components: {
    sentenceimport
  },
  watch: {
    page: function (val) {
      if (this.page.picture !== null) {
        // let holder = document.getElementById('pic-holder')
        // let rect = holder.getBoundingClientRect()
        // this.offsetTop = rect.top
        // this.offsetLeft = rect.left
      }
    }
  },
  computed: {
    curSenIndex: function () {
      return parseInt(this.curSenIndexChar)
    },
    x1: function () {
      if (this.curSenIndex >= 0) {
        return this.page.sentences[this.curSenIndex].x1
      } else {
        return -1
      }
    },
    y1: function () {
      if (this.curSenIndex >= 0) {
        return this.page.sentences[this.curSenIndex].y1
      } else {
        return -1
      }
    },
    x2: function () {
      if (this.curSenIndex >= 0) {
        return this.page.sentences[this.curSenIndex].x2
      } else {
        return -1
      }
    },
    y2: function () {
      if (this.curSenIndex >= 0) {
        return this.page.sentences[this.curSenIndex].y2
      } else {
        return -1
      }
    },
    curSentence: function () {
      return this.page.sentences[this.curSenIndex]
    }
  },
  methods: {
    addNewSentence: function () {
      let newSen = {
        content: null,
        audio: null,
        translated: null,
        x1: 0,
        x2: 0,
        y1: 0,
        y2: 0
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
      if (!this.canSelect) {
        return
      }
      this.canSelect = false
      this.isSelecting = true
      console.log('down!')
      console.log(this.xstart, this.ystart, this.xend, this.yend)
      this.xstart = e.clientX - this.offsetLeft
      this.ystart = e.clientY - this.offsetTop
      this.xend = this.xstart
      this.yend = this.ystart
      this.reCalc()
    },
    onmousemove: function (e) {
      if (!this.isSelecting) {
        return
      }
      // console.log('move!')
      this.xend = e.clientX - this.offsetLeft
      this.yend = e.clientY - this.offsetTop
      this.reCalc()
    },
    onmouseup: function (e) {
      if (!this.isSelecting) {
        return
      }
      this.isSelecting = false
      console.log('up!')
    },
    selectArea: function (sentence) {
      let holder = document.getElementById('pic-holder')
      let rect = holder.getBoundingClientRect()
      this.offsetTop = rect.top
      this.offsetLeft = rect.left
      console.log('selectArea is called!')
      this.canSelect = true
      // this.curSentence = sentence
    },
    reCalc: function () {
      console.log(this.curSentence)
      console.log(this.x1, this.y1, this.x2, this.y2)
      this.curSentence.x1 = Math.min(this.xstart, this.xend)
      this.curSentence.x2 = Math.max(this.xstart, this.xend)
      this.curSentence.y1 = Math.min(this.ystart, this.yend)
      this.curSentence.y2 = Math.max(this.ystart, this.yend)
    }
  },
  mounted () {
    // let holder = document.getElementById('pic-holder')
    // let rect = holder.getBoundingClientRect()
    // this.offsetTop = rect.top
    // this.offsetLeft = rect.left
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
    border: 2px solid red;
    position: absolute;
}
.upload-button {
  position: absolute;
  top: 423px;
}
.delete-button {
  position: absolute;
  top: 460px;
}
</style>
