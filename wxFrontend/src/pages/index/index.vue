<template>
  <div class="page">
    <div class="page__bd">
      <div class="weui-tab">
        <div class="weui-navbar">
          <block v-for="(item,index) in tabs" :key="index">
            <div :id="index" :class="{'weui-bar__item_on':activeIndex == index}" class="weui-navbar__item" @click="tabClick">
              <div class="weui-navbar__title">{{item}}</div>
            </div>
          </block>
        </div>
        <label class="change_level" @click="NavToLevel">等级</label>
        <div class="weui-tab__panel">
          <div class="weui-tab__content" :hidden="activeIndex != 0">
            <div class="page">
              <div class="page__bd">
                <div class="weui-grids">
                  <block v-for="book in intensiveReading" :key="book.id">
                    <div @click="navToNavigator(book)" class="weui-grid">
                      <image class="weui-grid__icon" :src="book.rcover" />
                      <div class="weui-grid__label">{{book.title}}</div>
                      <i-progress v-if="book.percent === 100" :percent="book.percent" status="success"></i-progress>
                      <i-progress v-else :percent="book.percent"></i-progress>
                    </div>
                  </block>
                </div>
              </div>
            </div>
          </div>
          <div class="weui-tab__content" :hidden="activeIndex != 1">
            <div class="page__bd">
              <div class="weui-grids">
                <block v-for="book in extensiveReading" :key="book.id">
                  <div @click="navToNavigator(book)" class="weui-grid">
                    <image class="weui-grid__icon" :src="book.rcover" />
                    <div class="weui-grid__label">{{book.title}}</div>
                    <i-progress v-if="book.percent === 100" :percent="book.percent" status="success"></i-progress>
                    <i-progress v-else :percent="book.percent"></i-progress>
                  </div>
                </block>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import request from '@/utils/request'

export default {
  data () {
    return {
      tabs: ['精读', '泛读'],
      activeIndex: 0,
      fontSize: 30,
      intensiveReading: [],
      extensiveReading: []
    }
  },
  computed: {
    navbarSliderClass () {
      if (this.activeIndex === 0) {
        return 'weui-navbar__slider_0'
      }
      if (this.activeIndex === 1) {
        return 'weui-navbar__slider_1'
      }
    }
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
    navToNavigator (book) {
      let url =
        '/pages/navigator/main?id=' + book.id + '&title=' + book.title + '&cover=' + book.rcover + '&page=' + book.progress.current_page
      wx.navigateTo({ url })
    },
    progress (book) {
      var progress = Math.floor(100 * book.progress.current_page / (book.pages_num - 1))
      return progress
    },
    NavToLevel () {
      wx.navigateTo({ url: '/pages/levelinfo/main' })
    }
  }
}
</script>

<style scoped>
page,
.page,
.page__bd {
  height: 100%;
}
.page__bd {
  padding-bottom: 0;
}
.weui-tab__content {
  padding-top: 60px;
  text-align: center;
}
.weui-navbar {
  display: -webkit-box;
  display: -webkit-flex;
  display: flex;
  position: absolute;
  z-index: 500;
  width: 100%;
  border-bottom: 1rpx solid #ccc;
  background-color: #fafafa;
}

.weui-navbar__item {
  position: relative;
  display: block;
  -webkit-box-flex: 1;
  -webkit-flex: 1;
  flex: 1;
  padding: 13px 0;
  text-align: center;
  font-size: 0;
}

.weui-navbar__item.weui-bar__item_on {
  color: #5187e8;
}

.weui-navbar__slider {
  position: absolute;
  content: " ";
  left: 0;
  bottom: 0;
  width: 6em;
  height: 3px;
  -webkit-transition: -webkit-transform 0.3s;
  transition: -webkit-transform 0.3s;
  transition: transform 0.3s;
  transition: transform 0.3s, -webkit-transform 0.3s;
}

.weui-navbar__title {
  display: inline-block;
  font-size: 15px;
  max-width: 8em;
  width: auto;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  word-wrap: normal;
}

.change_level {
  position: fixed;
  left: 690rpx;
  padding-left: 20rpx;
  top: 110rpx;
  padding-top: 10rpx;
  width: 40rpx;
  height: 100rpx;
  color: #6db0eb;
  font-size: 30rpx;
  background-color: #ebf9fe;
  border: none;
}

.weui-tab {
  position: relative;
  height: 100%;
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
.page__hd {
  padding-top: 40rpx;
}

.page__bd {
  padding-bottom: 40px;
}

.page__bd_spacing {
  padding-left: 15px;
  padding-right: 15px;
}

.page__ft {
  padding-bottom: 10px;
  text-align: center;
}

.page__title {
  text-align: left;
  font-size: 20px;
  font-weight: 400;
}

.page__desc {
  margin-top: 5px;
  color: #888888;
  text-align: left;
  font-size: 14px;
}

.weui-loadmore {
  width: 65%;
  margin: 1.5em auto;
  line-height: 1.6em;
  font-size: 14px;
  text-align: center;
  border-top: 1px solid #e5e5e5;
  margin-top: 2.4em;
}

.weui-loadmore__tips_in-line {
  position: relative;
  top: -0.9em;
  padding: 2px 0.55em;
  background-color: #fff;
  color: #999;
  display: inline-block;
  vertical-align: middle;
}

.weui-loadmore__tips_in-dot {
  position: relative;
  padding: 0 0.16em;
  width: 4px;
  height: 1.6em;
}

.weui-loadmore_line {
  border-top: 1px solid #e5e5e5;
  margin-top: 2.4em;
}
</style>
