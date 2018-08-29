<template>
  <div>
    <Tabs type="card">
        <TabPane label="连线游戏">
          <matchingGame :bookid="bookid">
          </matchingGame>
        </TabPane>
        <TabPane label="拼图游戏">
          <jigsawGame :bookid="bookid">
          </jigsawGame>
        </TabPane>
        <TabPane label="单词识别">
          <recognitionGame :bookid="bookid">
          </recognitionGame>
        </TabPane>
        <TabPane label="选词填空">
          <clozeGame :bookid="bookid">
          </clozeGame>
        </TabPane>
    </Tabs>
  </div>
</template>

<script>
import matchingGame from './matching-game'
import jigsawGame from './jigsaw-game'
import recognitionGame from './recognition-game'
import clozeGame from './cloze-game'
export default {
  data () {
    return {
      tabChoice: 'tab2',
      tab1: 'matchingGame',
      tab2: 'jigsawGame',
      tab3: 'recognitionGame',
      tab4: 'clozeGame',
      bookid: -1
    }
  },
  components: {
    matchingGame,
    jigsawGame,
    recognitionGame,
    clozeGame
  },
  methods: {
  },
  created () {
    this.bookid = this.$route.params.id
  }
}
</script>
