<template>
  <div>
    <moment v-for="y in theData"
      :key="index"
      :x="y"></moment>
  </div>
</template>

<script>
import moment from '@/components/moment'
import request from '@/utils/request'
export default {
  data () {
    return {
      theData: null
    }
  },
  components: {
    moment
  },
  computed: {
  },
  methods: {
    getData: function () {
      let url = 'community/'
      request.get(url)
        .then((res) => {
          console.log(res.data)
          this.theData = res.data
        }).catch((err) => {
          console.log(err)
        })
    }
  },
  onLoad () {
    this.getData()
  }
}
</script>

<style scoped>
</style>
