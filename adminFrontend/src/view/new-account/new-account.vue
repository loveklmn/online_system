<template>
<Card class="main">
  <Row class="step-row">
    <Steps :current="current" class="steps">
          <Step title="生成账号所在级别"></Step>
          <Step title="本次生成账号数量"></Step>
          <Step title="生成账号"></Step>
    </Steps>
  </Row>
  <Divider />
  <Row class="content-row">
    <choose-level v-if="chooseLevelStage" :accounts-level="levelGetter" @on-select="getLevel" />
    <input-amount v-if="inputAmountStage" :accounts-amount="amountGetter" @on-select="getAmount" @go-back="resetLevel"/>
    <confirm-info v-if="confirmInfoStage" :accounts-level="levelGetter" :accounts-amount="amountGetter" @on-select="generate" @go-back="resetAmount" />
    <generate-again v-if="generateAgainStage" :level="levelGetter" :amount="amountGetter" />
  </Row>
</Card>
</template>
<script>
import chooseLevel from './components/choose-level'
import inputAmount from './components/input-amount'
import confirmInfo from './components/confirm-info'
import generateAgain from './components/generate-again'
import './format.less'
export default {
  name: 'new-account',
  components: {
    chooseLevel,
    inputAmount,
    confirmInfo,
    generateAgain
  },
  data () {
    return {
      currentAdmin: 'super',
      current: 0,
      chooseLevelStage: true,
      inputAmountStage: false,
      confirmInfoStage: false,
      generateAgainStage: false,
      accounts: {
        level: 'k1',
        amount: 1
      }
    }
  },
  computed: {
    levelGetter () {
      return this.accounts.level
    },
    amountGetter () {
      return this.accounts.amount
    }
  },
  methods: {
    getLevel (level) {
      this.current = 1
      this.accounts.level = level
      this.chooseLevelStage = false
      this.inputAmountStage = true
    },
    getAmount (amount) {
      this.current = 2
      this.accounts.amount = amount
      this.inputAmountStage = false
      this.confirmInfoStage = true
    },
    resetLevel () {
      this.current = 1
      this.inputAmountStage = false
      this.chooseLevelStage = true
    },
    resetAmount () {
      this.current = 2
      this.confirmInfoStage = false
      this.inputAmountStage = true
    },
    generate () {
      this.current = 3
      this.confirmInfoStage = false
      this.generateAgainStage = true
    }
  }
}
</script>
