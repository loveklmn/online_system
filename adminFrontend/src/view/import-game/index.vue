<template>
<content-layout
  title="游戏导入">
  <div slot="content">
    <Tabs type="card" class="game-card">
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
    <float-btn
    :back="backRoute"
    :assignment="assignmentRoute"
    :guidance="guidanceRoute"
    :ebook="ebookRoute"/>
  </div>
</content-layout>
</template>

<script>
import matchingGame from './matching-game'
import jigsawGame from './jigsaw-game'
import recognitionGame from './recognition-game'
import clozeGame from './cloze-game'
import contentLayout from '_c/content-layout'
import floatBtn from './float-btn.vue'
export default {
  data () {
    return {
      tabChoice: 'tab2',
      tab1: 'matchingGame',
      tab2: 'jigsawGame',
      tab3: 'recognitionGame',
      tab4: 'clozeGame',
      bookid: -1,
      backRoute: ``,
      assignmentRoute: ``,
      guidanceRoute: ``,
      ebookRoute: ``
    }
  },
  components: {
    matchingGame,
    jigsawGame,
    recognitionGame,
    clozeGame,
    contentLayout,
    floatBtn
  },
  methods: {
  },
  created () {
    this.bookid = this.$route.params.id
    this.backRoute = `/book/${this.bookid}`
    this.ebookRoute = `/book/${this.bookid}/ebook`
    this.guidanceRoute = `/book/${this.bookid}/guidance`
    this.assignmentRoute = `/book/${this.bookid}/assignment`
  }
}
</script>
