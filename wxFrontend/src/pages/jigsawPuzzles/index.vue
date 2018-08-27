<template>
  <div>
      <div class="container">
        <div class="pintu-wrap">
            <div class="pintu-line">
                <div :style="icon1" @click="touch1" data-index=3 data-space=1></div>
                <div :style="icon2" @click="touch2" data-index=5 data-space=2></div>
                <div :style="icon3" @click="touch3" data-index=6 data-space=3></div>
            </div>
            <div class="pintu-line">
                <div :style="icon4" @click="touch4" data-index=8 data-space=4></div>
                <div :style="icon5" @click="touch5" data-index=1 data-space=5></div>
                <div :style="icon6" @click="touch6" data-index=4 data-space=6></div>
            </div>
            <div class="pintu-line">
                    <div :style="icon7" @click="touch7" data-index=2 data-space=7></div>
                    <div :style="icon8" @click="touch8" data-index=7 data-space=8></div>
                    <div :style="icon9" @click="touch9" data-index=9 data-space=9></div>
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
      picture: 'https://i.loli.net/2018/08/27/5b82f5e0be22a.png',
      note: -1,
      space: -1,
      arr: ['3', '5', '6', '8', '1', '4', '2', '7', '9'],
      icon: ''
    }
  },
  computed: {
    icon1: function () {
      return 'top:0px;left:0px;background:url(' + this.picture + ') no-repeat -500rpx 0px/750rpx 1206rpx;width:250rpx;height:402rpx;'
    },
    icon2: function () {
      return 'top:0px;left:250rpx;background:url(' + this.picture + ') no-repeat -250rpx -402rpx/750rpx 1206rpx;width:250rpx;height:402rpx;'
    },
    icon3: function () {
      return 'top:0px;left:500rpx;background:url(' + this.picture + ') no-repeat -500rpx -402rpx/750rpx 1206rpx;width:250rpx;height:402rpx;'
    },
    icon4: function () {
      return 'top:402rpx;left:0px;background:url(' + this.picture + ') no-repeat -250rpx -804rpx/750rpx 1206rpx;width:250rpx;height:402rpx;'
    },
    icon5: function () {
      return 'top:402rpx;left:250rpx;background:url(' + this.picture + ') no-repeat 0px 0px/750rpx 1206rpx;width:250rpx;height:402rpx;'
    },
    icon6: function () {
      return 'top:402rpx;left:500rpx;background:url(' + this.picture + ') no-repeat 0px -402rpx/750rpx 1206rpx;width:250rpx;height:402rpx;'
    },
    icon7: function () {
      return 'top:804rpx;left:0px;background:url(' + this.picture + ') no-repeat -250rpx 0px/750rpx 1206rpx;width:250rpx;height:402rpx;'
    },
    icon8: function () {
      return 'top:804rpx;left:250rpx;background:url(' + this.picture + ') no-repeat 0px -804rpx/750rpx 1206rpx;width:250rpx;height:402rpx;'
    },
    icon9: function () {
      return 'top:804rpx;left:500rpx;background:url(' + this.picture + ') no-repeat -500rpx -804rpx/750rpx 1206rpx;width:250rpx;height:402rpx;'
    }
  },
  methods: {
    touch1 (e) {
      if (this.space === -1 || this.space === e.currentTarget.dataset.space) {
        this.space = e.currentTarget.dataset.space
        console.log('condition 1, space = ' + this.space)
        return 0
      } else {
        console.log('condition 2, you touched ' + this.space + '. you touch 3 now')
        this.space = -1
      }
    },
    touch2 (e) {
      if (this.space === -1 || this.space === e.currentTarget.dataset.space) {
        this.space = e.currentTarget.dataset.space
        console.log('condition 1, space = ' + this.space)
        return 0
      } else {
        console.log('condition 2, you touched ' + this.space + '. you touch 3 now')
        this.space = -1
      }
    },
    touch3 (e) {
      if (this.space === -1 || this.space === e.currentTarget.dataset.space) {
        this.space = e.currentTarget.dataset.space
        console.log('condition 1, space = ' + this.space)
        return 0
      } else {
        console.log('condition 2, you touched ' + this.space + '. you touch 3 now')
        this.space = -1
      }
    },
    touch4 (e) {
      if (this.space === -1 || this.space === e.currentTarget.dataset.space) {
        this.space = e.currentTarget.dataset.space
        console.log('condition 1, space = ' + this.space)
        return 0
      } else {
        console.log('condition 2, you touched ' + this.space + '. you touch 4 now')
        this.space = -1
      }
    },
    touch5 (e) {
      if (this.space === -1 || this.space === e.currentTarget.dataset.space) {
        this.space = e.currentTarget.dataset.space
        console.log('condition 1, space = ' + this.space)
        return 0
      } else {
        console.log('condition 2, you touched ' + this.space + '. you touch 5 now')
        this.space = -1
      }
    },
    touch6 (e) {
      if (this.space === -1 || this.space === e.currentTarget.dataset.space) {
        this.space = e.currentTarget.dataset.space
        console.log('condition 1, space = ' + this.space)
        return 0
      } else {
        console.log('condition 2, you touched ' + this.space + '. you touch 6 now')
        this.space = -1
      }
    },
    touch7 (e) {
      if (this.space === -1 || this.space === e.currentTarget.dataset.space) {
        this.space = e.currentTarget.dataset.space
        console.log('condition 1, space = ' + this.space)
        return 0
      } else {
        console.log('condition 2, you touched ' + this.space + '. you touch 7 now')
        this.space = -1
      }
    },
    touch8 (e) {
      if (this.space === -1 || this.space === e.currentTarget.dataset.space) {
        this.space = e.currentTarget.dataset.space
        console.log('condition 1, space = ' + this.space)
        return 0
      } else {
        console.log('condition 2, you touched ' + this.space + '. you touch 8 now')
        this.space = -1
      }
    },
    touch9 (e) {
      if (this.space === -1 || this.space === e.currentTarget.dataset.space) {
        this.space = e.currentTarget.dataset.space
        console.log('condition 1, space = ' + this.space)
        return 0
      } else {
        console.log('condition 2, you touched ' + this.space + '. you touch 9 now')
        this.space = -1
      }
    }
  }
}
</script>
<style>
.container {
  height: 100%;
  display: flex;
  /* padding-top: 200rpx; */
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
  color: #4e4b4b;
}

.btn-wrap {
  width: 100%;
  padding: 20px 0;
  text-align: center;
  margin: auto;
}

.pintu-wrap {
  width: 100%;
  align-items: center;
  /* padding-left: 60rpx; */
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
