<template>
  <Layout class="layout">
    <Content class="pic-content">
      <div v-if="page === null || page.picture === null">
        <img id="pic" class="pagepic" :src="defaultPic"/>
      </div>
      <div v-else id="pic-holder" class="pic-holder">
        <img
          id="pic"
          class="pagepic"
          :src="page.picture"
          ondragstart="return false;"
          v-on:mousedown="onmousedown"
          v-on:mousemove="onmousemove"
          v-on:mouseup="onmouseup"/>
        <div
          id="select-box"
          v-on:mousedown="onmousedown"
          v-on:mousemove="onmousemove"
          :style="{
            left: x1 + 'px',
            top: y1 + 'px',
            width: (x2 - x1) + 'px',
            height: (y2 - y1) + 'px'}"></div>
      </div>

      <Upload
        class="upload-button"
        name="file"
        :beforeUpload="handleUpload"
        accept="image/*"
        action=""
       >
          <Button class="upload-page" icon="ios-cloud-upload-outline">上传本页对应的图片</Button>
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

      <Collapse v-if="page !== null" v-model="curSenIndexChar" accordion>
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
import sentenceimport from './sentence-import'
import upload from '@/api/upload'
import baseURL from '_conf/url'
export default {
  data () {
    return {
      defaultPic: require('@/assets/images/addPage.png'),
      curSenIndexChar: '-1',
      // 以下均为鼠标点选区域有关的data
      scale: 10000,
      xstart: 0,
      ystart: 0,
      xend: 0,
      yend: 0,
      canSelect: false,
      isSelecting: false,
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
      if (this.page.sentences.length === 0) {
        this.addNewSentence()
      }
    }
  },
  computed: {
    curSenIndex: function () {
      return parseInt(this.curSenIndexChar)
    },
    x1: function () {
      if (this.curSenIndex >= 0) {
        return this.page.sentences[this.curSenIndex].x1 * 400 / this.scale
      } else {
        return -1
      }
    },
    y1: function () {
      if (this.curSenIndex >= 0) {
        return this.page.sentences[this.curSenIndex].y1 * 400 / this.scale
      } else {
        return -1
      }
    },
    x2: function () {
      if (this.curSenIndex >= 0) {
        return this.page.sentences[this.curSenIndex].x2 * 400 / this.scale
      } else {
        return -1
      }
    },
    y2: function () {
      if (this.curSenIndex >= 0) {
        return this.page.sentences[this.curSenIndex].y2 * 400 / this.scale
      } else {
        return -1
      }
    },
    curSentence: function () {
      return this.page.sentences[this.curSenIndex]
    }
  },
  methods: {
    deletePage: function () {
      this.$emit('deletePage', this.page.number)
    },
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
    deleteSentence: function (sentence) {
      let index = this.page.sentences.indexOf(sentence)
      this.page.sentences.splice(index, 1)
      if (this.page.sentences.length === 0) {
        this.curSenIndexChar = '-1'
      } else if (index < this.page.sentences.length) {
        this.curSenIndexChar = index.toString()
      } else {
        this.curSenIndexChar = (this.page.sentences.length - 1).toString()
      }
    },
    handleUpload (file) {
      let that = this
      let loader = this.$loading.show()
      upload(file)
        .then((res) => {
          let savepath = res.savepath
          that.page.picture = baseURL + savepath
          that.$emit('picChange')
          loader.hide()
        })
    },
    // 以下均为和鼠标点选有关的方法
    // 首先调用selectArea
    // 然后是mouse: down -> move -> up
    // reCalc 主要在move过程中调用
    selectArea: function (sentence) {
      let holder = document.getElementById('pic-holder')
      let rect = holder.getBoundingClientRect()
      this.offsetTop = rect.top
      this.offsetLeft = rect.left
      this.canSelect = true
      this.curSentence.x1 = 0
      this.curSentence.y1 = 0
      this.curSentence.x2 = 0
      this.curSentence.y2 = 0
    },
    onmousedown: function (e) {
      if (this.isSelecting) {
        this.isSelecting = false
        return
      }
      if (!this.canSelect) {
        return
      }
      this.canSelect = false
      this.isSelecting = true
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
      this.xend = e.clientX - this.offsetLeft
      this.yend = e.clientY - this.offsetTop
      this.reCalc()
    },
    onmouseup: function (e) {
      if (!this.isSelecting) {
        return
      }
      this.isSelecting = false
    },
    reCalc: function () {
      this.curSentence.x1 = Math.min(400, this.xstart, this.xend) * this.scale / 400
      this.curSentence.x2 = Math.max(this.xstart, this.xend, 0) * this.scale / 400
      this.curSentence.y1 = Math.min(400, this.ystart, this.yend) * this.scale / 400
      this.curSentence.y2 = Math.max(this.ystart, this.yend, 0) * this.scale / 400
    },
    // 以下是工具函数
    parseCoordinate: function (param) {
      if (this.curSenIndex >= 0) {
        return param
      } else {
        return -1
      }
    }
  },
  created () {
  },
  mounted () {
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
  margin-right: 10%;
}

.pagepic {
  width: 400px;
  height: 400px;
}

.add-sentence-button {
  margin: auto;
}

#select-box {
  position: absolute;
  border: 2px solid red;
}

.upload-button {
  position: absolute;
  top: 423px;
}

.delete-button {
  position: absolute;
  top: 460px;
  margin-top: 2%;
  width: 18.3%;
}

.upload-page {
  margin-top: 6%;
}

</style>
