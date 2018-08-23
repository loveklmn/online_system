<template>
  <Form :model="sentence">
    <FormItem label="原文">
      <Input v-model="sentence.content"/>
    </FormItem>
    <FormItem label="译文">
      <Input v-model="sentence.translated"/>
    </FormItem>
    <!-- <FormItem label="音频文件">
      <Input v-model="sentence.audio"/>
    </FormItem> -->

    <FormItem>
      <Upload action="//jsonplaceholder.typicode.com/posts/">
          <Button icon="ios-microphone">上传音频</Button>
      </Upload>
    </FormItem>
    <FormItem>
      <Button @click="selectArea"> 选择对应区域 </Button>
    <!-- </FormItem> -->

    <div>
      <p class="inline-p">x1&nbsp;</p>
      <Input readonly v-model="sentence.x1" class="coordinate"/>
      <p class="inline-p">y1&nbsp;</p>
      <Input readonly v-model="sentence.y1" class="coordinate"/>
    </div>

    <div>
      <p class="inline-p">x2&nbsp;</p>
      <Input readonly v-model="sentence.x2" class="coordinate"/>
      <p class="inline-p">y2&nbsp;</p>
      <Input readonly v-model="sentence.y2" class="coordinate"/>
    </div>
    </FormItem>

    <Button
      type="error"
      @click="deleteSentence">删除该句子</Button>

  </Form>
</template>
<script>
export default {
  props: ['sentence'],
  methods: {
    deleteSentence: function () {
      this.$emit('deleteSentence', this.sentence)
    },
    selectArea: function () {
      this.$emit('selectArea', this.sentence)
    }
  }
}
</script>
<style scoped>
.card {
  margin: 10px;
}
.coordinate {
  width: 30%;
  margin-right: 10px;
}
.inline-p {
  display: inline;
}
</style>
