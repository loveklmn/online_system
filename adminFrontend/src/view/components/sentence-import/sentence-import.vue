<template>
  <Form :model="sentence">
    <FormItem label="原文">
      <Input v-model="sentence.content"/>
    </FormItem>
    <FormItem label="译文">
      <Input v-model="sentence.translated"/>
    </FormItem>

    <FormItem>
      <Button
        class="inline"
        icon="ios-play"
        @click="playSound">播放音频</Button>
      <Upload
        name="file"
        :beforeUpload="handleUpload"
        class="inline">
          <Button icon="ios-microphone">上传音频</Button>
      </Upload>
    </FormItem>

    <FormItem>
      <Button @click="selectArea"> 选择对应区域 </Button>
      <div>
        <p class="inline">x1&nbsp;</p>
        <Input readonly v-model="sentence.x1" class="coordinate"/>
        <p class="inline">y1&nbsp;</p>
        <Input readonly v-model="sentence.y1" class="coordinate"/>
      </div>
      <div>
        <p class="inline">x2&nbsp;</p>
        <Input readonly v-model="sentence.x2" class="coordinate"/>
        <p class="inline">y2&nbsp;</p>
        <Input readonly v-model="sentence.y2" class="coordinate"/>
      </div>
    </FormItem>

    <Button
      type="error"
      @click="deleteSentence">删除该句子</Button>

  </Form>
</template>
<script>
import upload from '@/api/upload'
import baseURL from '_conf/url'
export default {
  props: ['sentence'],
  watch: {
    sentence () {
      // let xleft = Math.min(this.sentence.x1, this.sentence.x2)
      // let ytop = Math.min(this.sentence.y1, this.sentence.y2)
      // let xright = Math.max(this.sentence.x1, this.sentence.x2)
      // let ybottom = Math.max(this.sentence.y1, this.sentence.y2)
      // this.sentence.x1 = xleft
      // this.sentence.y1 = ytop
      // this.sentence.x2 = xright
      // this.sentence.y2 = ybottom
    }
  },
  methods: {
    deleteSentence: function () {
      this.$emit('deleteSentence', this.sentence)
    },
    selectArea: function () {
      this.$emit('selectArea', this.sentence)
    },
    playSound: function () {
      let audio = new Audio(this.sentence.audio)
      audio.play()
    },
    handleUpload (file) {
      let that = this
      upload(file)
        .then((res) => {
          let savepath = res.savepath
          that.sentence.audio = baseURL + savepath
          alert('上传音频成功！')
        })
        .catch((err) => {
          console.log(err)
        })
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
.inline {
  display: inline;
}
</style>
