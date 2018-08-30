<template>
<div class="gameboard">
  <div v-if="loading" class="loading-outer-wrapper">
  <image class="main-bg" src="../../static/images/main-bg.png"/>
    <div class="loading-inner-wrapper">
      <BallPulse />
    </div>
  </div>
  <div v-else class="gameboard">
    <div class="vertical-list">
      <matchingGamePic
        v-for="pic in leftpics"
        v-bind:key="pic.id"
        v-bind:src="pic.src"
        v-bind:inmatch="pic.inmatch"
        v-bind:selected="pic.selected"
        v-bind:id="pic.id"
        v-bind:value="pic.value"
        v-bind:word="pic.word"
        v-on:isselect="select"
      ></matchingGamePic>
    </div>
    <div class="vertical-list">
      <matchingGamePic
        v-for="pic in rightpics"
        v-bind:key="pic.id"
        v-bind:src="pic.src"
        v-bind:inmatch="pic.inmatch"
        v-bind:selected="pic.selected"
        v-bind:id="pic.id"
        v-bind:value="pic.value"
        v-bind:word="pic.word"
        v-on:isselect="select"
      ></matchingGamePic>
    </div>
    <!-- inline style cannot be avoided. No criticism will be accepted.-->
    <canvas class="canvas" :style="{display:hide?'none':'block'}" canvas-id="1"/>
  </div>
</div>
</template>

<script>
import matchingGamePic from '@/components/matchingGamePic'
import request from '@/utils/request'
import BallPulse from 'mpvue-loading/src/loaders/ball-pulse'
export default {
  data () {
    return {
      leftpics: {
        1: {id: -1, value: -1, src: null, word: null, inmatch: false, selected: false},
        2: {id: -2, value: -2, src: null, word: null, inmatch: false, selected: false},
        3: {id: -3, value: -3, src: null, word: null, inmatch: false, selected: false}
      },
      rightpics: {
        1: {id: 1, value: 1, src: null, word: null, inmatch: false, selected: false},
        2: {id: 2, value: 3, src: null, word: null, inmatch: false, selected: false},
        3: {id: 3, value: 2, src: null, word: null, inmatch: false, selected: false}
      },
      previd: 0,
      hide: true,
      num: 3,
      matchedNum: 0,
      innerAudioContext: null,
      correct1src: '/static/audios/correct1.mp3',
      correctallsrc: '/static/audios/correctall.mp3',
      wrongsrc: '/static/audios/wrong.mp3',
      waittime: 600,
      loading: true
    }
  },
  components: {
    matchingGamePic,
    BallPulse
  },
  methods: {
    select: function (id) {
      if (this.previd === id) {
        this.unselect(id)
        this.previd = 0
        return
      }
      if (!this.getPic(id).inmatch) {
        this.getPic(id).selected = true
      }
      if (this.previd === 0) { // 之前没有选中按钮
        this.previd = id
        return
      }
      if (this.sameSide(id)) { //  之前选中的按钮在同一侧
        this.unselect(this.previd)
        this.previd = id
        return
      }
      // 之前选中的按钮在对面一侧，分为两种情况：匹配和不匹配
      setTimeout(() => {
        if (this.match(id)) { // 若匹配
          this.matchedNum += 1
          this.drawCorrectLine(id, this.previd)
          this.setInmatch(id)
          this.setInmatch(this.previd)
          this.previd = 0
          this.makeCorrectSound()
          if (this.matchedNum === this.num) {
            this.drawAllCorrectLine()
            this.makeAllCorrectSound()
          } else {
            this.slowlyHideCanvas()
          }
        } else { // 若不匹配
          this.drawWrongLine(id, this.previd)
          this.makeWrongSound()
          this.slowlyHideCanvas()
          this.unselectBoth(id, this.previd)
        }
      }, 300)
    },
    unselectBoth: function (id, previd) {
      let that = this
      setTimeout(function () {
        that.unselect(id)
        that.unselect(that.previd)
        that.previd = 0
      }, 0)
    },
    sameSide: function (id) {
      return id * this.previd > 0
    },
    match: function (id) {
      let value = this.getPic(id).value
      let prevvalue = this.getPic(this.previd).value
      return value + prevvalue === 0
    },
    getPic: function (id) {
      return (id < 0 ? this.leftpics : this.rightpics)[Math.abs(id)]
    },
    getPos: function (id) {
      return this.getPic(id).pos
    },
    unselect: function (id) {
      if (!this.getPic(this.previd).inmatch) {
        this.getPic(id).selected = false
      }
    },
    setInmatch: function (id) {
      this.getPic(id).inmatch = true
    },
    drawCorrectLine: function (id, previd) {
      let green = '#008000'
      this.drawLineBetween(id, previd, green)
      this.showCanvas()
    },
    makeCorrectSound: function () {
      this.innerAudioContext.src = this.correct1src
      this.innerAudioContext.play()
    },
    drawWrongLine: function (id, previd) {
      let red = '#ff0000'
      this.drawLineBetween(id, previd, red)
      this.showCanvas()
    },
    makeWrongSound: function () {
      this.innerAudioContext.src = this.wrongsrc
      this.innerAudioContext.play()
    },
    getX: function (id) {
      let W = wx.getSystemInfoSync().windowWidth
      return W / 2 + (id / Math.abs(id)) * W / 4
    },
    getY: function (id) {
      let H = wx.getSystemInfoSync().windowHeight
      return Math.abs(id) * H / this.num - H / (2 * this.num)
    },
    drawLineBetween: function (id1, id2, color) {
      let context = this.getContext(color)
      this.contextAction(context, id1, id2)
      wx.drawCanvas({
        canvasId: 1,
        actions: context.getActions()
      })
    },
    getContext: function (color) {
      let context = wx.createContext()
      context.setLineWidth(4)
      context.setStrokeStyle(color)
      return context
    },
    contextAction: function (context, id1, id2) {
      let x1 = this.getX(id1)
      let y1 = this.getY(id1)
      let x2 = this.getX(id2)
      let y2 = this.getY(id2)
      context.moveTo(x1, y1)
      context.lineTo(x2, y2)
      context.stroke()
    },
    getIdOfValue: function (value, pics) {
      for (let k = 1; k <= this.num; k += 1) {
        if (pics[k].value === value) {
          return pics[k].id
        }
      }
    },
    drawAllCorrectLine: function () {
      let green = '#008000'
      let context = this.getContext(green)
      for (let value = 1; value <= this.num; value += 1) {
        let id1 = this.getIdOfValue(-value, this.leftpics)
        let id2 = this.getIdOfValue(value, this.rightpics)
        this.contextAction(context, id1, id2)
      }
      wx.drawCanvas({
        canvasId: 1,
        actions: context.getActions()
      })
      this.showCanvas()
    },
    makeAllCorrectSound: function () {
      this.innerAudioContext.src = this.correctallsrc
      this.innerAudioContext.play()
    },
    showCanvas: function () {
      this.hide = false
    },
    hideCanvas: function () {
      this.hide = true
    },
    slowlyHideCanvas: function () {
      setTimeout(this.hideCanvas, 700)
    },
    getRandomInt: function (max) {
      return Math.floor(Math.random() * Math.floor(max))
    }
  },
  onLoad (options) {
    this.innerAudioContext = wx.createInnerAudioContext()
    let url = 'books/' + options.id + '/MatchingGame/'
    let map = [
      [1, 2, 3],
      [1, 3, 2],
      [2, 1, 3],
      [2, 3, 1],
      [3, 1, 2],
      [3, 2, 1]
    ]
    let vm = this
    request.get(url)
      .then((res) => {
        let leftArrangement = this.getRandomInt(6)
        let rightArrangement = this.getRandomInt(6)
        for (let i = 1; i <= 3; i++) {
          let leftPos = map[leftArrangement][i - 1]
          this.leftpics[leftPos].src = request.baseURL + res.data[i - 1].img
          this.leftpics[leftPos].value = -i
          this.leftpics[i].selected = false
          let rightPos = map[rightArrangement][i - 1]
          this.rightpics[rightPos].word = res.data[i - 1].word
          this.rightpics[rightPos].value = i
          this.rightpics[i].selected = false
        }
        vm.loading = false
      })
  }
}
</script>

<style>
page {
  width: 100%;
  height: 100%;
}

.gameboard {
  display: flex;
  flex-direction: row;
  flex-grow: 1 1;
  width: 100%;
  height: 100%;
}

.loading-outer-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  height: 100%;
}

.loading-inner-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: center;
  display: inline;
  margin: auto auto;
  padding: 0;
}

.vertical-list {
  display: flex;
  flex-direction: column;
  width: 50%;
  height: 100%;
  justify-content: space-around;
}

.canvas {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
}

.hidden {
  position: absolute;
  left: -1000;
  top: -1000;
  width: 0;
  height: 0;
}
</style>
