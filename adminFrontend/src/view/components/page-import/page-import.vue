<template>
  <!-- <div>
    <p>{{page}}</p>
  </div> -->
  <Layout class="layout">
    <Content class="pic">
      <p>{{page}}</p>
    </Content>
    <Content class="sentence">
      <p>{{page}}</p>
    </Content>
  </Layout>
</template>
<script>
export default {
  props: ['page']
}
</script>
<style scoped>
.layout {
  flex-direction: row
}
.class {
  flex: 2;
}
.sentence {
  flex: 1;
}
</style>
