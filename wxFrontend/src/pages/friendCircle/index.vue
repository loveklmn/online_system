<template>
  <div class="container">
    <div class="swiper-content">
      <div class="tab">
        <div @click="tabPage" :class="'tab-item '+(currentNumber==0?'tab-item-current':'') " data-index="0">朋友圈</div>
        <div @click="tabPage" :class="'tab-item tab-item2 ' + (currentNumber==1 ? 'tab-item-current' : '')" data-index="1">排行榜</div>
      </div>
      <swiper @change="switchPage" :current="currentIndex">
        <swiper-item>
          <scroll-view class="scroll-views" scrollX="false" scrollY="true">
            <moment v-for="(y,index) in theData" :key="index" :x="y"></moment>
          </scroll-view>
        </swiper-item>
        <swiper-item>
          <scroll-view class="scroll-views" scrollX="false" scrollY="true">
            <div class="rank-list">
              <div class="rank-list-item" v-for="(item,index) in aList" :key="index">
                <div class="rank-num">
                  <image :src="'../../static/images/rank-num-' + (index + 1) + '.png'" v-if="index<3" />
                  <div v-if="index>=3">{{index>=9?index+1:'0' + (index + 1) }}</div>
                </div>
                <image class="user-head" :src="item.avatarurl" />
                <div class="user-name">{{item.nickname}}</div>
                <div class="user-challenge-success-times">
                  <div>获得</div>
                  <rich-text>
                    <i style="font-size: 36rpx;color: red;font-style:italic;">{{item.score}}</i>
                    分</rich-text>
                </div>
              </div>
            </div>
            <div class="rank-footer"></div>
          </scroll-view>
        </swiper-item>
      </swiper>
    </div>
  </div>
</template>

<script>
import moment from '@/components/moment'
import request from '@/utils/request'
export default {
  data () {
    return {
      theData: null,
      currentNumber: 0,
      currentIndex: 0,
      aList: []
    }
  },
  components: {
    moment
  },
  computed: {
  },
  methods: {
    tabClick (e) {
      this.activeIndex = e.currentTarget.id
    },
    getData: function () {
      let url = 'community/'
      request.get(url)
        .then((res) => {
          this.theData = res.data.reverse()
        })
    },
    tabPage: function (a) {
      this.currentNumber = a.target.dataset.index
      this.currentIndex = a.target.dataset.index
    },
    switchPage: function (a) {
      this.currentNumber = a.target.current
      this.currentIndex = a.target.current
    }
  },
  onLoad () {
    this.getData()
    let url = 'ranklist/'
    request.get(url).then((res) => {
      if (res.statusCode === 200) {
        this.aList = res.data
        this.aList.forEach(element => {
          element.avatarurl = request.baseURL + element.avatar
        })
      }
    })
  },
  onPullDownRefresh () {
    this.getData()
  }
}
</script>

<style scoped>
.swiper-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
}

.tab {
    position: fixed;
    position: relative;
    top: 0;
    left: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    width: 660rpx;
    height: 100rpx;
    border-radius: 50rpx;
}

.tab>image {
    position: absolute;
    top: -1rpx;
    left: -1rpx;
    width: 414rpx;
    height: 54rpx;
}

.tab-item {
    position: absolute;
    top: 10rpx;
    left: -10rpx;
    width: 340rpx;
    height: 80rpx;
    font-size: 30rpx;
    line-height: 80rpx;
    text-align: center;
}

.tab-item2 {
    left: 330rpx;
}

.tab-item-current {
    font-weight: bold;
    color: #fff;
    background-color: #00a7fe;
    border-radius: 40rpx;
}

.swiper-content>swiper {
    width: 100%;
    height: 1167rpx;
}

.rank-list {
    width: 100%;
}

.rank-list-item {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    width: 660rpx;
    height: 140rpx;
    margin-top: 25rpx;
    margin-left: 45rpx;
    border: solid #00a7fe 1rpx;
    border-radius: 10rpx;
}

.rank-list-item:first-child {
    margin-top: 28rpx;
}

.rank-num>image {
    width: 54rpx;
    height: 44rpx;
}

.rank-num>view {
    width: 50rpx;
    height: 50rpx;
    font-size: 18rpx;
    font-weight: bold;
    line-height: 50rpx;
    color: #382198;
    text-align: center;
    background-color: #dcaa63;
    border-radius: 50%;
}

.user-head {
    width: 100rpx;
    height: 100rpx;
    margin-left: 30rpx;
    border: solid 3rpx #d0e2ef;
    border-radius: 50%;
}

.user-name {
    width: 250rpx;
    margin-left: 28rpx;
    font-size: 32rpx;
}

.user-challenge-success-times {
    width: 110rpx;
    font-size: 24rpx;
    text-align: right;
}

.scroll-views {
    height: 100%;
}

.rank-footer {
    width: 100%;
    height: 30rpx;
}

page {
    width: 100%;
    height: 100%;
    color: white;
    background-color: #91ccf0;
}

.container {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    height: 100%;
    margin-top: 20rpx;
}

.main-bg {
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: -1;
    width: 750rpx;
    height: 1214rpx;
}

.main-content {
    width: 662rpx;
    height: 100%;
}

button,button::after {
    border: none;
}

.loading {
    position: fixed;
    top: 80rpx;
    left: 0;
    z-index: -1;
    width: 584rpx;
    height: 958rpx;
    margin-left: 83rpx;
}
</style>
