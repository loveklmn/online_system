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
    .layout {
      position: relative;
      overflow: hidden;
      background: #f5f7f9;
      border: 1px solid #d7dde4;
      border-radius: 4px;
    }

    .layout-header-bar {
      background: #fff;
      box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
      font-size: 16px;
      font-weight: bold;
      height: 50px;
    }

    .content-model {
      min-height: '220px';
      margin: '20px';
      background-color: '#fff';
    }
</style>
