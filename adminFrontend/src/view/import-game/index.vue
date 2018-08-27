<template>
  <div>
    <Tabs type="card">
        <TabPane label="连线游戏">
          <matchingGame>
          </matchingGame>
        </TabPane>
        <TabPane label="拼图游戏">
          <jigsawGame>
          </jigsawGame>
        </TabPane>
        <TabPane label="单词识别">
          <recognitionGame>
          </recognitionGame>
        </TabPane>
        <TabPane label="选词填空">标签四的内容</TabPane>
    </Tabs>
  </div>
</template>

<script>
import matchingGame from './matching-game'
import jigsawGame from './jigsaw-game'
import recognitionGame from './recognition-game'
export default {
  data () {
    return {
      tabChoice: 'tab1',
      tab1: 'matchingGame',
      tab2: 'jigsawGame',
      tab3: 'recognitionGame',
      tab4: 'clozeGame'
    }
  },
  components: {
    matchingGame,
    jigsawGame,
    recognitionGame
  },
  methods: {
  }
}
</script>

<style>
</style>
