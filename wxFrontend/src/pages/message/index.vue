<template>
  <div>
    <i-card full title="username" extra="\>" thumb="https://i.loli.net/2018/08/11/5b6edc7419a1a.png"></i-card>
    <i-panel class="cell-panel-demo" title="账户">
      <i-cell-group>
        <i-cell title="修改密码" isLink url="/pages/changePassword/main" />
        <i-cell title="消息" isLink />
      </i-cell-group>
    </i-panel>

    <i-panel class="cell-panel-demo" title="关于">
      <i-cell title="关于弗恩英语" is-link url="/pages/aboutVron/main" />
    </i-panel>
  </div>
</template>

<script>
export default {
  data () {
    return {}
  },

  methods: {},

  created () {}
}
</script>
<style scoped>
</style>
