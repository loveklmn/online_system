<template>
  <Tabs type="card">
      <TabPane label="连线游戏">
        <matchingGame>
        </matchingGame>
      </TabPane>
      <TabPane label="拼图游戏">标签二的内容</TabPane>
      <TabPane label="单词识别">标签三的内容</TabPane>
      <TabPane label="选词填空">标签三的内容</TabPane>
  </Tabs>
</template>

<script>
import matchingGame from './matching-game'
export default {
  components: {
    matchingGame
  }
}
</script>

<style>
</style>
