<template>
  <div class="gameboard">
    <image class="main-bg" src="../../static/images/main-bg.png"/>
    <div class="vertical-list">
      <matchingGamePic
        v-for="pic in leftpics"
        v-bind:key="pic.id"
        v-bind:src="pic.src"
        v-bind:inmatch="pic.inmatch"
        v-bind:selected="pic.selected"
        v-bind:id="pic.id"
        v-bind:value="pic.value"
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
        v-on:isselect="select"
      ></matchingGamePic>
    </div>
    <!-- inline style cannot be avoided. No criticism will be accepted.-->
    <canvas class="canvas" :style="{display:hide?'none':'block'}" canvas-id="1"/>
  </div>
</template>

<script>
import matchingGamePic from '@/components/matchingGamePic'
export default {
  data () {
    return {
      leftpics: {
        1: {id: -1, value: -1, src: null, inmatch: false, selected: false},
        2: {id: -2, value: -2, src: null, inmatch: false, selected: false},
        3: {id: -3, value: -3, src: null, inmatch: false, selected: false}
      },
      rightpics: {
        1: {id: 1, value: 1, src: null, inmatch: false, selected: false},
        2: {id: 2, value: 3, src: null, inmatch: false, selected: false},
        3: {id: 3, value: 2, src: null, inmatch: false, selected: false}
      },
      previd: 0,
      hide: true,
      num: 3,
      matchedNum: 0,
      innerAudioContext: null,
      correct1src: '/static/audios/correct1.mp3',
      correctallsrc: '/static/audios/correctall.mp3',
      wrongsrc: '/static/audios/wrong.mp3',
      waittime: 600
    }
  },
  components: {
    matchingGamePic
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
    }
  },
  mounted () {
    this.innerAudioContext = wx.createInnerAudioContext()
    for (let i = 1; i <= 3; i++) {
      this.leftpics[i].src = 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png'
      this.rightpics[i].src = 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png'
    }
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
