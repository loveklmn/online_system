import { mount } from '@vue/test-utils'
import index from '@/pages/index/index.vue'

describe('index', () => {
  const wrapper = mount(index)
  let book = {}
  book.progress = {}
  book.pages_num = 10
  describe('progress', () => {
    it('should count progress correctly', () => {
      let vm = wrapper.vm
      book.progress.current_page = 1
      expect(vm.progress(book)).toEqual(11)
      book.progress.current_page = 9
      expect(vm.progress(book)).toEqual(100)
      book.progress.current_page = 0
      expect(vm.progress(book)).toEqual(0)
    })
  })
})
