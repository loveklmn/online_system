<template>
  <div class="tables-edit-outer">
    <div v-if="!isEditting" class="tables-edit-con">
      <span class="value-con">{{ value }}</span>
      <Button v-if="editable" @click="startEdit" class="tables-edit-btn" type="text"><Icon type="md-create"></Icon></Button>
    </div>
    <div v-else class="tables-editting-con">
      <Input :value="value" @on-enter="handleEnter" @input="handleInput" class="tables-edit-input"/>
      <Button @click="saveEdit" class="edit-btn" type="text"><Icon type="md-checkmark"></Icon></Button>
      <Button @click="canceltEdit" class="edit-btn" type="text"><Icon type="md-close"></Icon></Button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TablesEdit',
  props: {
    value: [String, Number],
    changed: Boolean,
    edittingCellId: String,
    params: Object,
    editable: Boolean
  },
  computed: {
    isEditting () {
      return this.edittingCellId === `editting-${this.params.index}-${this.params.column.key}`
    }
  },
  methods: {
    handleInput (val) {
      this.changed = true
      this.$emit('input', val)
    },
    handleEnter (val) {
      this.changed = true
      this.$emit('input', val)
    },
    startEdit () {
      this.$emit('on-start-edit', this.params)
    },
    saveEdit () {
      if (this.changed) {
        this.$emit('on-save-edit', this.params)
      } else {
        this.canceltEdit()
      }
    },
    canceltEdit () {
      this.$emit('on-cancel-edit', this.params)
    }
  }
}
</script>

<style lang="less">
.tables-edit-outer{
  height: 100%;
  .tables-edit-con{
    position: relative;
    height: 100%;
    .value-con{
      vertical-align: middle;
    }
    .tables-edit-btn{
      position: absolute;
      right: 10px;
      top: 0;
      display: none;
      padding: 2px 4px;
    }
    .tables-edit-btn{
      display: inline-block;
    }
  }
  .tables-editting-con{
    .tables-edit-input{
      width: ~"calc(100% - 60px)";
    }
  }
  .edit-btn {
    padding: 6px 4px;
  }
}
</style>
