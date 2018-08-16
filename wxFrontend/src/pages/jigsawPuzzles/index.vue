<template>
  <div>
    <div class="container">
  <div class="pintu-wrap">
    <div class="pintu-line">
      <div class="pintu-item-wrap">
        <image class="pintu-item" type="primary" :src="cards.card1.src" :hidden="cards.card1.hidden" @click="card1"/> 
      </div>
      <div class="pintu-item-wrap">
        <image class="pintu-item" type="primary" :src="cards.card2.src" :hidden="cards.card2.hidden" @click="card2"/> 
      </div>
      <div class="pintu-item-wrap">
        <image class="pintu-item" type="primary" :src="cards.card3.src" :hidden="cards.card3.hidden" @click="card3"/> 
      </div>
    </div>
    <div class="pintu-line">
      <div class="pintu-item-wrap">
        <image class="pintu-item" type="primary" :src="cards.card4.src" :hidden="cards.card4.hidden" @click="card4"/> 
      </div>
      <div class="pintu-item-wrap">
        <image class="pintu-item" type="primary" :src="cards.card5.src" :hidden="cards.card5.hidden" @click="card5"/> 
      </div>
      <div class="pintu-item-wrap">
        <image class="pintu-item" type="primary" :src="cards.card6.src" :hidden="cards.card6.hidden" @click="card6"/> 
      </div>
    </div>
    <div class="pintu-line">
      <div class="pintu-item-wrap">
        <image class="pintu-item" type="primary" :src="cards.card7.src" :hidden="cards.card7.hidden" @click="card7"/> 
      </div>
      <div class="pintu-item-wrap">
        <image class="pintu-item" type="primary" :src="cards.card8.src" :hidden="cards.card8.hidden" @click="card8"/> 
      </div>
      <div class="pintu-item-wrap">
        <image class="pintu-item" type="primary" :src="cards.card9.src" :hidden="cards.card9.hidden" @click="card9"/> 
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
export default {
  data () {
    return {
      word: 'It is a lucky cat.',
      cards: {
        card1: {num: 3, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744aef8183b.jpg'},
        card2: {num: 7, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ae8bb097.jpg'},
        card3: {num: 5, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ae679f2c.jpg'},
        card4: {num: '', hidden: true, src: 'https://i.loli.net/2018/08/15/5b744ae453d4f.jpg'},
        card5: {num: 4, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ae274208.jpg'},
        card6: {num: 6, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744add508b0.jpg'},
        card7: {num: 2, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ad901dab.jpg'},
        card8: {num: 8, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ad4b1fb6.jpg'},
        card9: {num: 1, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ad026a65.png'}
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
      this.cards = {
        card1: {num: 3, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744aef8183b.jpg'},
        card2: {num: 7, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ae8bb097.jpg'},
        card3: {num: 5, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ae679f2c.jpg'},
        card4: {num: '', hidden: true, src: 'https://i.loli.net/2018/08/15/5b744ae453d4f.jpg'},
        card5: {num: 4, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ae274208.jpg'},
        card6: {num: 6, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744add508b0.jpg'},
        card7: {num: 2, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ad901dab.jpg'},
        card8: {num: 8, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ad4b1fb6.jpg'},
        card9: {num: 1, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ad026a65.png'}
      }
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
