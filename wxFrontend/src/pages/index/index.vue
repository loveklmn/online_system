<template>
  <div class="container">
    <div class="swiper-content">
      <label class="change_level" @click="NavToLevel">等<br>级</label>
      <div class="tab">
        <div @click="tabPage" :class="'tab-item '+(currentNumber==0?'tab-item-current':'') " data-index="0">精读</div>
        <div @click="tabPage" :class="'tab-item tab-item2 ' + (currentNumber==1 ? 'tab-item-current' : '')" data-index="1">泛读</div>
      </div>
      <swiper @change="switchPage" :current="currentIndex">
        <swiper-item>
          <div class="weui-tab__content" :hidden="activeIndex != 0">
            <scroll-view class="book-list" scrollX="false" scrollY="true">
                <div class="weui-grids">
                  <block v-for="book in intensiveReading" :key="book.id">
                    <div @click="navToNavigator(book)" class="weui-grid">
                      <image class="weui-grid__icon" :src="book.rcover" />
                      <div class="weui-grid__label">
                        {{book.title}}<br>
                        <i-progress v-if="book.percent === 100" :percent="book.percent" status="success" hide-info></i-progress>
                        <i-progress v-else :percent="book.percent" hide-info></i-progress>
                      </div>
                    </div>
                  </block>
                </div>
            </scroll-view>
          </div>
        </swiper-item>
        <swiper-item>
           <div class="weui-tab__content" :hidden="activeIndex != 0">
          <scroll-view class="book-list" scrollX="false" scrollY="true">
                <div class="weui-grids">
                  <block v-for="book in extensiveReading" :key="book.id">
                    <div @click="navToNavigator(book)" class="weui-grid">
                      <image class="weui-grid__icon" :src="book.rcover" />
                      <div class="weui-grid__label">
                        {{book.title}}<br>
                        <i-progress v-if="book.percent === 100" :percent="book.percent" status="success" hide-info></i-progress>
                        <i-progress v-else :percent="book.percent" hide-info></i-progress>
                      </div>
                    </div>
                  </block>
                </div>
            </scroll-view>
           </div>
        </swiper-item>
      </swiper>
    </div>
  </div>
</template>

<script>
import request from '@/utils/request'
export default {
  data () {
    return {
      currentNumber: 0,
      currentIndex: 0,
      activeIndex: 0,
      intensiveReading: [],
      extensiveReading: []
    }
  },
  computed: {
  },
  onShow () {
    request
      .get('books/')
      .then(res => {
        if (res.data.length > 0) {
          res.data.forEach((book) => {
            book.percent = this.progress(book)
            book.rcover = request.baseURL + book.cover
          })
          this.intensiveReading = res.data.filter(book => book.type === 'IR')
          this.extensiveReading = res.data.filter(book => book.type === 'ER')
        }
      })
  },
  methods: {
    switchPage: function (a) {
      this.currentNumber = a.target.current
      this.currentIndex = a.target.current
    },
    navToNavigator (book) {
      let url =
        '/pages/navigator/main?id=' + book.id + '&title=' + book.title + '&cover=' + book.rcover + '&page=' + book.progress.current_page + '&punched=' + book.progress.punched
      wx.navigateTo({ url })
    },
    progress (book) {
      var progress = Math.floor(100 * book.progress.current_page / (book.pages_num - 1))
      return progress
    },
    NavToLevel () {
      wx.navigateTo({ url: '/pages/levelinfo/main' })
    },
    tabPage: function (a) {
      this.currentNumber = a.target.dataset.index
      this.currentIndex = a.target.dataset.index
    }
  }
}
</script>

<style scoped>
page {
  height:91.6%
}

.book-list {
  height:100%;
}

.weui-tab__content {
  height: 88%;
  position: flex;
  padding-top: 100rpx;
}

.swiper-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
}

swiper {
  z-index: 500;
  display: -webkit-box;
  display: -webkit-flex;
  display: flex;
  width: 100%;
  height: 1167rpx;
}

.weui-grids {
  overflow: hidden;
}

.weui-grid {
  position: relative;
  box-sizing: border-box;
  float: left;
  width: 33.33333333%;
  padding: 10px;
}

.weui-grid__icon {
  display: block;
  width: 220rpx;
  height: 220rpx;
  margin: 0 auto;
}

.weui-grid__label {
  display: block;
  margin-top: 5px;
  margin-right:10px;
  margin-left: 10px;
  overflow: hidden;
  font-size: 14px;
  color: #000;
  text-align: center;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.weui-loading {
  display: inline-block;
  width: 20px;
  height: 20px;
  margin: 0 5px;
  vertical-align: middle;
  background: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjAiIGhlaWdodD0iMTIwIiB2aWV3Qm94PSIwIDAgMTAwIDEwMCI+PHBhdGggZmlsbD0ibm9uZSIgZD0iTTAgMGgxMDB2MTAwSDB6Ii8+PHJlY3Qgd2lkdGg9IjciIGhlaWdodD0iMjAiIHg9IjQ2LjUiIHk9IjQwIiBmaWxsPSIjRTlFOUU5IiByeD0iNSIgcnk9IjUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAgLTMwKSIvPjxyZWN0IHdpZHRoPSI3IiBoZWlnaHQ9IjIwIiB4PSI0Ni41IiB5PSI0MCIgZmlsbD0iIzk4OTY5NyIgcng9IjUiIHJ5PSI1IiB0cmFuc2Zvcm09InJvdGF0ZSgzMCAxMDUuOTggNjUpIi8+PHJlY3Qgd2lkdGg9IjciIGhlaWdodD0iMjAiIHg9IjQ2LjUiIHk9IjQwIiBmaWxsPSIjOUI5OTlBIiByeD0iNSIgcnk9IjUiIHRyYW5zZm9ybT0icm90YXRlKDYwIDc1Ljk4IDY1KSIvPjxyZWN0IHdpZHRoPSI3IiBoZWlnaHQ9IjIwIiB4PSI0Ni41IiB5PSI0MCIgZmlsbD0iI0EzQTFBMiIgcng9IjUiIHJ5PSI1IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCA2NSA2NSkiLz48cmVjdCB3aWR0aD0iNyIgaGVpZ2h0PSIyMCIgeD0iNDYuNSIgeT0iNDAiIGZpbGw9IiNBQkE5QUEiIHJ4PSI1IiByeT0iNSIgdHJhbnNmb3JtPSJyb3RhdGUoMTIwIDU4LjY2IDY1KSIvPjxyZWN0IHdpZHRoPSI3IiBoZWlnaHQ9IjIwIiB4PSI0Ni41IiB5PSI0MCIgZmlsbD0iI0IyQjJCMiIgcng9IjUiIHJ5PSI1IiB0cmFuc2Zvcm09InJvdGF0ZSgxNTAgNTQuMDIgNjUpIi8+PHJlY3Qgd2lkdGg9IjciIGhlaWdodD0iMjAiIHg9IjQ2LjUiIHk9IjQwIiBmaWxsPSIjQkFCOEI5IiByeD0iNSIgcnk9IjUiIHRyYW5zZm9ybT0icm90YXRlKDE4MCA1MCA2NSkiLz48cmVjdCB3aWR0aD0iNyIgaGVpZ2h0PSIyMCIgeD0iNDYuNSIgeT0iNDAiIGZpbGw9IiNDMkMwQzEiIHJ4PSI1IiByeT0iNSIgdHJhbnNmb3JtPSJyb3RhdGUoLTE1MCA0NS45OCA2NSkiLz48cmVjdCB3aWR0aD0iNyIgaGVpZ2h0PSIyMCIgeD0iNDYuNSIgeT0iNDAiIGZpbGw9IiNDQkNCQ0IiIHJ4PSI1IiByeT0iNSIgdHJhbnNmb3JtPSJyb3RhdGUoLTEyMCA0MS4zNCA2NSkiLz48cmVjdCB3aWR0aD0iNyIgaGVpZ2h0PSIyMCIgeD0iNDYuNSIgeT0iNDAiIGZpbGw9IiNEMkQyRDIiIHJ4PSI1IiByeT0iNSIgdHJhbnNmb3JtPSJyb3RhdGUoLTkwIDM1IDY1KSIvPjxyZWN0IHdpZHRoPSI3IiBoZWlnaHQ9IjIwIiB4PSI0Ni41IiB5PSI0MCIgZmlsbD0iI0RBREFEQSIgcng9IjUiIHJ5PSI1IiB0cmFuc2Zvcm09InJvdGF0ZSgtNjAgMjQuMDIgNjUpIi8+PHJlY3Qgd2lkdGg9IjciIGhlaWdodD0iMjAiIHg9IjQ2LjUiIHk9IjQwIiBmaWxsPSIjRTJFMkUyIiByeD0iNSIgcnk9IjUiIHRyYW5zZm9ybT0icm90YXRlKC0zMCAtNS45OCA2NSkiLz48L3N2Zz4=);
  background-size: 100%;
  -webkit-animation: a 1s steps(12) infinite;
  animation: a 1s steps(12) infinite;
}

.tab {
    position: fixed;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    top: 0rpx;
    width: 750rpx;
    margin-left: 45rpx;
    height: 100rpx;
    background-color: white;
    border: 2rpx;
    border-color:#00a7fe;
    border-radius: 50rpx;
    z-index: 999;
}

.change_level {
  position: fixed;
  top: 110rpx;
  left: 690rpx;
  z-index: 9999;
  width: 80rpx;
  height: 100rpx;
  padding-top: 10rpx;
  padding-left: 20rpx;
  font-size: 30rpx;
  color: #6db0eb;
  background-color: #ebf9fe;
  border: none;
  border-radius: 20%;
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

swiper {
    width: 100%;
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

.rank-footer {
    width: 100%;
    height: 30rpx;
}

.container {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
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
