import { mount } from '@vue/test-utils'
import matchingGamePic from '@/components/matchingGamePic'

describe('matchingGamePic', () => {
  const wrapper = mount(matchingGamePic)
  describe('img', () => {
    it('should swicth class after click', () => {
      const img = wrapper.find('img')
      expect(img.classes()).toEqual(['pic'])
      img.trigger('click')
      setTimeout(() => {
        expect(img.classes()).toEqual(['pic_selected'])
      }, 10)
    })
  })
})
