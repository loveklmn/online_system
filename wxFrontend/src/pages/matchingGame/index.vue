<template>
  <div class="gameboard">
    <image class="main-bg" src="../../static/images/main-bg.png"/>
    <div class="vertical_list">
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
    <div class="vertical_list">
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
        1: {id: -1, value: -1, src: 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png', inmatch: false, selected: false},
        2: {id: -2, value: -2, src: 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png', inmatch: false, selected: false},
        3: {id: -3, value: -3, src: 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png', inmatch: false, selected: false}
      },
      rightpics: {
        1: {id: 1, value: 1, src: 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png', inmatch: false, selected: false},
        2: {id: 2, value: 3, src: 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png', inmatch: false, selected: false},
        3: {id: 3, value: 2, src: 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png', inmatch: false, selected: false}
      },
      previd: 0,
      hide: true,
      num: 3,
      matched_num: 0,
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
      if (!this.get_pic(id).inmatch) {
        this.get_pic(id).selected = true
      }
      if (this.previd === 0) { // 之前没有选中按钮
        this.previd = id
        return
      }
      if (this.same_side(id)) { //  之前选中的按钮在同一侧
        this.unselect(this.previd)
        this.previd = id
        return
      }
      // 之前选中的按钮在对面一侧，分为两种情况：匹配和不匹配
      setTimeout(() => {
        if (this.match(id)) { // 若匹配
          this.matched_num += 1
          this.draw_correct_line(id, this.previd)
          this.set_inmatch(id)
          this.set_inmatch(this.previd)
          this.previd = 0
          this.make_correct_sound()
          // this.unselect_both(id, this.previd)
          if (this.matched_num === this.num) {
            this.draw_all_correct_line()
            this.make_all_correct_sound()
          } else {
            this.slowly_hide_canvas()
          }
        } else { // 若不匹配
          this.draw_wrong_line(id, this.previd)
          this.make_wrong_sound()
          this.slowly_hide_canvas()
          this.unselect_both(id, this.previd)
        }
      }, 300)
    },
    unselect_both: function (id, previd) {
      let that = this
      setTimeout(function () {
        that.unselect(id)
        that.unselect(that.previd)
        that.previd = 0
      }, 0)
    },
    same_side: function (id) {
      return id * this.previd > 0
    },
    match: function (id) {
      let value = this.get_pic(id).value
      let prevvalue = this.get_pic(this.previd).value
      return value + prevvalue === 0
    },
    get_pic: function (id) {
      return (id < 0 ? this.leftpics : this.rightpics)[Math.abs(id)]
    },
    get_pos: function (id) {
      return this.get_pic(id).pos
    },
    unselect: function (id) {
      if (!this.get_pic(this.previd).inmatch) {
        this.get_pic(id).selected = false
      }
    },
    set_inmatch: function (id) {
      this.get_pic(id).inmatch = true
    },
    draw_correct_line: function (id, previd) {
      let green = '#008000'
      this.draw_line_between(id, previd, green)
      this.show_canvas()
    },
    make_correct_sound: function () {
      this.innerAudioContext.src = this.correct1src
      this.innerAudioContext.play()
    },
    draw_wrong_line: function (id, previd) {
      let red = '#ff0000'
      this.draw_line_between(id, previd, red)
      this.show_canvas()
    },
    make_wrong_sound: function () {
      this.innerAudioContext.src = this.wrongsrc
      this.innerAudioContext.play()
    },
    get_x: function (id) {
      let W = wx.getSystemInfoSync().windowWidth
      return W / 2 + (id / Math.abs(id)) * W / 4
    },
    get_y: function (id) {
      let H = wx.getSystemInfoSync().windowHeight
      return Math.abs(id) * H / this.num - H / (2 * this.num)
    },
    draw_line_between: function (id1, id2, color) {
      let context = this.get_context(color)
      this.context_action(context, id1, id2)
      wx.drawCanvas({
        canvasId: 1,
        actions: context.getActions()
      })
    },
    get_context: function (color) {
      let context = wx.createContext()
      context.setLineWidth(4)
      context.setStrokeStyle(color)
      return context
    },
    context_action: function (context, id1, id2) {
      let x1 = this.get_x(id1)
      let y1 = this.get_y(id1)
      let x2 = this.get_x(id2)
      let y2 = this.get_y(id2)
      context.moveTo(x1, y1)
      context.lineTo(x2, y2)
      context.stroke()
    },
    get_id_of_value: function (value, pics) {
      for (let k = 1; k <= this.num; k += 1) {
        if (pics[k].value === value) {
          return pics[k].id
        }
      }
    },
    draw_all_correct_line: function () {
      let green = '#008000'
      let context = this.get_context(green)
      for (let value = 1; value <= this.num; value += 1) {
        let id1 = this.get_id_of_value(-value, this.leftpics)
        let id2 = this.get_id_of_value(value, this.rightpics)
        this.context_action(context, id1, id2)
      }
      wx.drawCanvas({
        canvasId: 1,
        actions: context.getActions()
      })
      this.show_canvas()
    },
    make_all_correct_sound: function () {
      this.innerAudioContext.src = this.correctallsrc
      this.innerAudioContext.play()
    },
    show_canvas: function () {
      this.hide = false
    },
    hide_canvas: function () {
      this.hide = true
    },
    slowly_hide_canvas: function () {
      setTimeout(this.hide_canvas, 700)
    }
  },
  mounted () {
    this.innerAudioContext = wx.createInnerAudioContext()
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

.vertical_list {
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
