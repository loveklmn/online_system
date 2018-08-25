import { mount } from '@vue/test-utils'
import notice from '@/pages/notice'

describe('notice', () => {
  const wrapper = mount(notice)
  describe('have read', () => {
    it('should return chinese character string correctly', () => {
      let vm = wrapper.vm
      let flag = true
      expect(vm.haveRead(flag)).toEqual('(已读)')
      flag = false
      expect(vm.haveRead(flag)).toEqual('')
    })
  })
})
