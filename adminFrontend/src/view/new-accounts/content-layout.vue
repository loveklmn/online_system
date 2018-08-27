<template>
    <div class="layout">
        <Layout>
            <Layout>
                <Header class="layout-header-bar">{{ pageTitle }}</Header>
                <Content class="content-model">
                  <slot name="content"></slot>
                </Content>
            </Layout>
        </Layout>
    </div>
</template>
<script>
export default {
  name: 'contentLayout',
  props: {
    title: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      pageTitle: this.title
    }
  }
}
</script>
<style scoped>
    .layout{
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
    }
    .layout-header-bar{
        background: #fff;
        box-shadow: 0 1px 1px rgba(0,0,0,.1);
    }
    .content-model {
      margin: '20px';
      background-color: '#fff';
      min-height: '220px';
    }
</style>
