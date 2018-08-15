<template>
  <div class="gameboard">
    <div class="vertical_list">
      <matchingGamePic
        v-for="pic in leftpics"
        v-bind:key="pic.id"
        v-bind:src="pic.src"
      ></matchingGamePic>
    </div>
    <div class="vertical_list">
      <matchingGamePic
        v-for="pic in rightpics"
        v-bind:key="pic.id"
        v-bind:src="pic.src"
      ></matchingGamePic>
    </div>
  </div>
</template>

<script>
import matchingGamePic from '@/components/matchingGamePic'
export default {
  data () {
    return {
      leftpics: [
        {id: 1, src: 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png'},
        {id: 2, src: 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png'},
        {id: 3, src: 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png'}
      ],
      rightpics: [
        {id: 1, src: 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png'},
        {id: 2, src: 'https://i.loli.net/2018/08/12/5b6f09c2b5b34.png'}
      ]
    }
  },
  components: {
    matchingGamePic
  },
  methods: {

  },
  created () {

  }
}
</script>

<style>
page {
  width: 100%;
  height: 100%;
}
.gameboard {
  display: flex;
  flex-direction: row;
  flex-grow: 1 1;
  width: 100%;
  height: 100%;
}

.vertical_list {
  display: flex;
  flex-direction: column;
  width: 50%;
  height: 100%;
  justify-content: space-around;
}
</style>
