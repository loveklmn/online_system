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
                    <div class="page">
                        <div class="page__bd">
                            <div class="weui-grids">
                                <block v-for="book in intensiveReading" :key="book.id">
                                    <div @click="navToNavigator(book)" class="weui-grid">
                                        <image class="weui-grid__icon" :src="book.rcover" />
                                        <div class="weui-grid__label" >
                                          {{book.title}}<br>
                                          <i-progress v-if="book.percent === 100" :percent="book.percent" status="success" hide-info></i-progress>
                                          <i-progress v-else :percent="book.percent" hide-info></i-progress>
                                        </div>

                                    </div>
                                </block>
                            </div>
                        </div>
                    </div>
                </div>
            </swiper-item>
            <swiper-item>
                <scroll-view bindscrolltolower="lower" class="scroll-views" scrollX="false" scrollY="true">
                    <div class="page__bd">
                        <div class="weui-grids">
                            <block v-for="book in extensiveReading" :key="book.id">
                                <div @click="navToNavigator(book)" class="weui-grid">
                                    <image class="weui-grid__icon" :src="book.rcover" />
                                    <div class="weui-grid__label" >
                                        {{book.title}}<br>
                                        <i-progress v-if="book.percent === 100" :percent="book.percent" status="success" hide-info></i-progress>
                                        <i-progress v-else :percent="book.percent" hide-info></i-progress>
                                      </div>
                                </div>
                            </block>
                        </div>
                    </div>
                </scroll-view>
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
    tabClick (e) {
      this.activeIndex = e.currentTarget.id
    },
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

.swiper-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}

swiper {
  display: -webkit-box;
  display: -webkit-flex;
  display: flex;
  z-index: 500;
  height: 1167rpx;
  width: 100%;
}

.weui-grids {
  overflow: hidden;
}

.weui-grid {
  position: relative;
  float: left;
  padding: 10px;
  width: 33.33333333%;
  box-sizing: border-box;
}

.weui-grid__icon {
  display: block;
  width: 170rpx;
  height: 240rpx;
  margin: 0 auto;
}

.weui-grid__label {
  margin-top: 5px;
  display: block;
  text-align: center;
  color: #000;
  font-size: 14px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  margin-left: 10px;
  margin-right:10px;
}

.weui-grid__label_punched {
  margin-top: 5px;
  display: block;
  text-align: center;
  color: green;
  font-size: 14px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}

.weui-loading {
  margin: 0 5px;
  width: 20px;
  height: 20px;
  display: inline-block;
  vertical-align: middle;
  -webkit-animation: a 1s steps(12) infinite;
  animation: a 1s steps(12) infinite;
  background: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjAiIGhlaWdodD0iMTIwIiB2aWV3Qm94PSIwIDAgMTAwIDEwMCI+PHBhdGggZmlsbD0ibm9uZSIgZD0iTTAgMGgxMDB2MTAwSDB6Ii8+PHJlY3Qgd2lkdGg9IjciIGhlaWdodD0iMjAiIHg9IjQ2LjUiIHk9IjQwIiBmaWxsPSIjRTlFOUU5IiByeD0iNSIgcnk9IjUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAgLTMwKSIvPjxyZWN0IHdpZHRoPSI3IiBoZWlnaHQ9IjIwIiB4PSI0Ni41IiB5PSI0MCIgZmlsbD0iIzk4OTY5NyIgcng9IjUiIHJ5PSI1IiB0cmFuc2Zvcm09InJvdGF0ZSgzMCAxMDUuOTggNjUpIi8+PHJlY3Qgd2lkdGg9IjciIGhlaWdodD0iMjAiIHg9IjQ2LjUiIHk9IjQwIiBmaWxsPSIjOUI5OTlBIiByeD0iNSIgcnk9IjUiIHRyYW5zZm9ybT0icm90YXRlKDYwIDc1Ljk4IDY1KSIvPjxyZWN0IHdpZHRoPSI3IiBoZWlnaHQ9IjIwIiB4PSI0Ni41IiB5PSI0MCIgZmlsbD0iI0EzQTFBMiIgcng9IjUiIHJ5PSI1IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCA2NSA2NSkiLz48cmVjdCB3aWR0aD0iNyIgaGVpZ2h0PSIyMCIgeD0iNDYuNSIgeT0iNDAiIGZpbGw9IiNBQkE5QUEiIHJ4PSI1IiByeT0iNSIgdHJhbnNmb3JtPSJyb3RhdGUoMTIwIDU4LjY2IDY1KSIvPjxyZWN0IHdpZHRoPSI3IiBoZWlnaHQ9IjIwIiB4PSI0Ni41IiB5PSI0MCIgZmlsbD0iI0IyQjJCMiIgcng9IjUiIHJ5PSI1IiB0cmFuc2Zvcm09InJvdGF0ZSgxNTAgNTQuMDIgNjUpIi8+PHJlY3Qgd2lkdGg9IjciIGhlaWdodD0iMjAiIHg9IjQ2LjUiIHk9IjQwIiBmaWxsPSIjQkFCOEI5IiByeD0iNSIgcnk9IjUiIHRyYW5zZm9ybT0icm90YXRlKDE4MCA1MCA2NSkiLz48cmVjdCB3aWR0aD0iNyIgaGVpZ2h0PSIyMCIgeD0iNDYuNSIgeT0iNDAiIGZpbGw9IiNDMkMwQzEiIHJ4PSI1IiByeT0iNSIgdHJhbnNmb3JtPSJyb3RhdGUoLTE1MCA0NS45OCA2NSkiLz48cmVjdCB3aWR0aD0iNyIgaGVpZ2h0PSIyMCIgeD0iNDYuNSIgeT0iNDAiIGZpbGw9IiNDQkNCQ0IiIHJ4PSI1IiByeT0iNSIgdHJhbnNmb3JtPSJyb3RhdGUoLTEyMCA0MS4zNCA2NSkiLz48cmVjdCB3aWR0aD0iNyIgaGVpZ2h0PSIyMCIgeD0iNDYuNSIgeT0iNDAiIGZpbGw9IiNEMkQyRDIiIHJ4PSI1IiByeT0iNSIgdHJhbnNmb3JtPSJyb3RhdGUoLTkwIDM1IDY1KSIvPjxyZWN0IHdpZHRoPSI3IiBoZWlnaHQ9IjIwIiB4PSI0Ni41IiB5PSI0MCIgZmlsbD0iI0RBREFEQSIgcng9IjUiIHJ5PSI1IiB0cmFuc2Zvcm09InJvdGF0ZSgtNjAgMjQuMDIgNjUpIi8+PHJlY3Qgd2lkdGg9IjciIGhlaWdodD0iMjAiIHg9IjQ2LjUiIHk9IjQwIiBmaWxsPSIjRTJFMkUyIiByeD0iNSIgcnk9IjUiIHRyYW5zZm9ybT0icm90YXRlKC0zMCAtNS45OCA2NSkiLz48L3N2Zz4=);
  background-size: 100%;
}

.tab {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    background-color: white;
    border: 2rpx;
    border-color:#00a7fe;
    width: 660rpx;
    height: 100rpx;
    border-radius: 50rpx;
    position: relative;
}

.change_level {
  position: fixed;
  left: 690rpx;
  padding-left: 20rpx;
  top: 110rpx;
  padding-top: 10rpx;
  width: 80rpx;
  height: 100rpx;
  color: #6db0eb;
  font-size: 30rpx;
  background-color: #ebf9fe;
  border: none;
  z-index: 9999;
  border-radius: 20%;
}

.tab>image {
    width: 414rpx;
    height: 54rpx;
    position: absolute;
    left: -1rpx;
    top: -1rpx;
}

.tab-item {
    font-size: 30rpx;
    width: 340rpx;
    height: 80rpx;
    line-height: 80rpx;
    text-align: center;
    position: absolute;
    left: -10rpx;
    top: 10rpx;
}

.tab-item2 {
    left: 330rpx;
}

.tab-item-current {
    background-color: #00a7fe;
    border-radius: 40rpx;
    font-weight: bold;
    color: #fff;
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
    border: solid #00a7fe 1rpx;
    border-radius: 10rpx;
    height: 140rpx;
    margin-top: 25rpx;
    margin-left: 45rpx;
    width: 660rpx;
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
    border-radius: 50%;
    background-color: #dcaa63;
    font-size: 18rpx;
    color: #382198;
    text-align: center;
    line-height: 50rpx;
    font-weight: bold;
}

.user-head {
    width: 100rpx;
    height: 100rpx;
    border-radius: 50%;
    border: solid 3rpx #d0e2ef;
    margin-left: 30rpx;
}

.user-name {
    width: 250rpx;
    font-size: 32rpx;
    margin-left: 28rpx;
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
    justify-content: center;
    align-items: flex-start;
    margin-top: 20rpx;
    width: 100%;
}

.main-bg {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 750rpx;
    height: 1214rpx;
    z-index: -1;
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
    width: 584rpx;
    height: 958rpx;
    z-index: -1;
    margin-left: 83rpx;
}
</style>
