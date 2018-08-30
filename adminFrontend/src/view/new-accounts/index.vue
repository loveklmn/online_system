<template>
<content-layout
  title="生成激活码">
  <div slot="content">
    <first-step
    :accountLevel="level"
    :accountAmount="amount"
    v-if="firstStage"
    @firstDone="handleFirstDone"/>
    <second-step
    :accountLevel="level"
    :accountAmount="amount"
    v-if="secondStage"
    @secondDone="handleSecondDone"
    @secondBack="handleSecondBack"/>
    <third-step
    :accountLevel="level"
    :accountAmount="amount"
    v-if="thirdStage"
    @generateAgain="handleGenerateAgain"
    @backHome="handleBackHome"/>
    <backhome-btn
      back="/home"
      name="回首页"/>
  </div>
</content-layout>
</template>
<script>
import contentLayout from '_c/content-layout'
import firstStep from './new-accounts.vue'
import secondStep from './generate-accounts.vue'
import thirdStep from './generate-result.vue'
import backhomeBtn from '_c/backhome-btn'
export default {
  data () {
    return {
      level: 1,
      amount: 1,
      firstStage: true,
      secondStage: false,
      thirdStage: false
    }
  },
  components: {
    contentLayout,
    firstStep,
    secondStep,
    thirdStep,
    backhomeBtn
  },
  methods: {
    handleFirstDone (data) {
      this.level = data.level
      this.amount = data.amount
      this.firstStage = false
      this.secondStage = true
    },
    handleSecondDone (data) {
      this.level = data.level
      this.amount = data.amount
      this.secondStage = false
      this.thirdStage = true
    },
    handleSecondBack (data) {
      this.level = data.level
      this.amount = data.amount
      this.secondStage = false
      this.firstStage = true
    },
    handleGenerateAgain () {
      this.level = 1
      this.amount = 1
      this.thirdStage = false
      this.firstStage = true
    },
    handleBackHome () {
      this.$router.replace({
        path: '/home'
      })
    }
  }
}
</script>
