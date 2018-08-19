<template>
  <div>
    <moment :x="x"> </moment>
    <moment :x="x"> </moment>
  </div>
</template>

<script>
import moment from '@/components/moment'
export default {
  data () {
    return {
      x: {
        author: {
          username: '弗恩英语客服',
          avatar: 'https://unsplash.it/400/800/?random'
        },
        action: {
          liked: true
        },
        book: {
          cover: 'http://xxxxxxx/x.jpg',
          title: 'mpvue从入坑到弃坑'
        },
        created_time: '13个月前',
        content: '欢迎大家来弗恩英语学习',
        attachments: {
          image: [
            'https://unsplash.it/400/800/?random',
            'https://unsplash.it/400/800/?random',
            'https://unsplash.it/400/800/?random',
            'https://unsplash.it/400/800/?random'
          ]
        },
        vote_count: 23,
        comment_count: 10
      }
    }
  },
  components: {
    moment
  },

  methods: {},

  created () {}
}
</script>

<style scoped>
</style>
