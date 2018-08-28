<template>
  <div>
    <image class="main-bg" src="../../static/images/main-bg.png" />
    <div class="container">
        <div class="pintu-wrap">
            <div class="pintu-line">
                <div class="pintu-item-wrap">
                    <image class="pintu-item" type="primary" :src="cards.card1.src" :hidden="cards.card1.hidden" @click="card1" />
                </div>
                <div class="pintu-item-wrap">
                    <image class="pintu-item" type="primary" :src="cards.card2.src" :hidden="cards.card2.hidden" @click="card2" />
                </div>
                <div class="pintu-item-wrap">
                    <image class="pintu-item" type="primary" :src="cards.card3.src" :hidden="cards.card3.hidden" @click="card3" />
                </div>
            </div>
            <div class="pintu-line">
                <div class="pintu-item-wrap">
                    <image class="pintu-item" type="primary" :src="cards.card4.src" :hidden="cards.card4.hidden" @click="card4" />
                </div>
                <div class="pintu-item-wrap">
                    <image class="pintu-item" type="primary" :src="cards.card5.src" :hidden="cards.card5.hidden" @click="card5" />
                </div>
                <div class="pintu-item-wrap">
                    <image class="pintu-item" type="primary" :src="cards.card6.src" :hidden="cards.card6.hidden" @click="card6" />
                </div>
            </div>
            <div class="pintu-line">
                <div class="pintu-item-wrap">
                    <image class="pintu-item" type="primary" :src="cards.card7.src" :hidden="cards.card7.hidden" @click="card7" />
                </div>
                <div class="pintu-item-wrap">
                    <image class="pintu-item" type="primary" :src="cards.card8.src" :hidden="cards.card8.hidden" @click="card8" />
                </div>
                <div class="pintu-item-wrap">
                    <image class="pintu-item" type="primary" :src="cards.card9.src" :hidden="cards.card9.hidden" @click="card9" />
                </div>
            </div>
        </div>
        <div class="btn-wrap">
            <button type="warn" @click="initGame">重新开始</button>
        </div>
    </div>
</div>
</template>

<script>
import request from '@/utils/request'
export default {
  data () {
    return {
      word: 'It is a lucky cat.',
      cards: {
        card1: {num: 3, hidden: false, src: ''},
        card2: {num: 7, hidden: false, src: ''},
        card3: {num: 5, hidden: false, src: ''},
        card4: {num: '', hidden: true, src: ''},
        card5: {num: 4, hidden: false, src: ''},
        card6: {num: 6, hidden: false, src: ''},
        card7: {num: 2, hidden: false, src: ''},
        card8: {num: 8, hidden: false, src: ''},
        card9: {num: 1, hidden: false, src: ''}
      }
    }
  },
  methods: {
    card1 () {
      this.moveCard('1', '2')
      this.moveCard('1', '4')
    },
    card2 () {
      this.moveCard('2', '1')
      this.moveCard('2', '3')
      this.moveCard('2', '5')
    },
    card3 () {
      this.moveCard('3', '2')
      this.moveCard('3', '6')
    },
    card4 () {
      this.moveCard('4', '1')
      this.moveCard('4', '5')
      this.moveCard('4', '7')
    },
    card5 () {
      this.moveCard('5', '2')
      this.moveCard('5', '4')
      this.moveCard('5', '6')
      this.moveCard('5', '8')
    },
    card6 () {
      this.moveCard('6', '3')
      this.moveCard('6', '5')
      this.moveCard('6', '9')
    },
    card7 () {
      this.moveCard('7', '4')
      this.moveCard('7', '8')
    },
    card8 () {
      this.moveCard('8', '5')
      this.moveCard('8', '7')
      this.moveCard('8', '9')
    },
    card9 () {
      this.moveCard('9', '6')
      this.moveCard('9', '8')
    },
    initGame () {
      let vm = this.cards
      let url = 'books/' + this.id + '/JigsawGame/'
      request.get(url)
        .then(res => {
          let vt = res.data
          vm.card1.src = request.baseURL + vt['3']
          vm.card1.num = 3
          vm.card1.hidden = false
          vm.card2.src = request.baseURL + vt['7']
          vm.card2.num = 7
          vm.card2.hidden = false
          vm.card3.src = request.baseURL + vt['5']
          vm.card3.num = 5
          vm.card3.hidden = false
          vm.card4.src = request.baseURL + vt['9']
          vm.card4.num = ''
          vm.card4.hidden = true
          vm.card5.src = request.baseURL + vt['4']
          vm.card5.num = 4
          vm.card5.hidden = false
          vm.card6.src = request.baseURL + vt['6']
          vm.card6.num = 6
          vm.card6.hidden = false
          vm.card7.src = request.baseURL + vt['2']
          vm.card7.num = 2
          vm.card7.hidden = false
          vm.card8.src = request.baseURL + vt['8']
          vm.card8.num = 8
          vm.card8.hidden = false
          vm.card9.src = request.baseURL + vt['1']
          vm.card9.num = 1
          vm.card9.hidden = false
        })
    },
    moveCard (n1, n2) {
      let cards = this.cards
      let c1 = cards['card' + n1]
      let c2 = cards['card' + n2]
      if (c1.num && !c2.num) {
        let num1 = c1.num
        let hidden1 = c1.hidden
        let src1 = c1.src
        let num2 = c2.num
        let hidden2 = c2.hidden
        let src2 = c2.src
        cards['card' + n1].num = num2
        cards['card' + n1].hidden = hidden2
        cards['card' + n1].src = src2
        cards['card' + n2].num = num1
        cards['card' + n2].hidden = hidden1
        cards['card' + n2].src = src1
        let isGameOver = true
        for (let i = 1; i < 9; i++) {
          if (cards['card' + i].num !== i) {
            isGameOver = false
            break
          }
        }
        if (isGameOver) {
          cards.card9.num = 9
          cards.card9.hidden = false
          cards.card9.hidden = false
        }
        this.cards = cards

        if (isGameOver) {
          wx.showModal({
            title: 'Oooops',
            content: this.word,
            showCancel: false
          })
        }
      }
    }
  },
  onLoad (options) {
    let vm = this.cards
    this.id = options.id
    let url = 'books/' + options.id + '/JigsawGame/'
    request.get(url)
      .then(res => {
        let vt = res.data
        console.log(vt['3'])
        vm.card1.src = request.baseURL + vt['3']
        vm.card2.src = request.baseURL + vt['7']
        vm.card3.src = request.baseURL + vt['5']
        vm.card4.src = request.baseURL + vt['9']
        vm.card5.src = request.baseURL + vt['4']
        vm.card6.src = request.baseURL + vt['6']
        vm.card7.src = request.baseURL + vt['2']
        vm.card8.src = request.baseURL + vt['8']
        vm.card9.src = request.baseURL + vt['1']
      })
  }
}
</script>

<style>
input{
  padding: 20rpx
}
.container {
  height: 100%;
  display: flex;
  padding-top: 200rpx;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
  color: #4e4b4b;
}

.btn-wrap {
  width: 80%;
  padding: 20px 0;
  text-align: center;
  margin: auto;
}

.pintu-wrap {
  width: 100%;
  align-items: center;
  padding-left: 60rpx;
}

.pintu-line {
  display: flex;
}

.pintu-item-wrap {
  height: 100px;
  width: 30%;
}

.pintu-item {
  line-height: 100px;
  height: 100%;
  width: 100%;
}
</style>
