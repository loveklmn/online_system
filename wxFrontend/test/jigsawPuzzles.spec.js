import { mount } from '@vue/test-utils'
import jigsawPuzzles from '@/pages/jigsawPuzzles'

describe('jigsawPuzzles', () => {
  const wrapper = mount(jigsawPuzzles)
  let vm = wrapper.vm
  describe('init game', () => {
    it('should set data correctly', () => {
      wrapper.vm.initGame()
      expect(wrapper.vm.cards).toEqual({
        card1: {num: 3, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744aef8183b.jpg'},
        card2: {num: 7, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ae8bb097.jpg'},
        card3: {num: 5, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ae679f2c.jpg'},
        card4: {num: '', hidden: true, src: 'https://i.loli.net/2018/08/15/5b744ae453d4f.jpg'},
        card5: {num: 4, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ae274208.jpg'},
        card6: {num: 6, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744add508b0.jpg'},
        card7: {num: 2, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ad901dab.jpg'},
        card8: {num: 8, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ad4b1fb6.jpg'},
        card9: {num: 1, hidden: false, src: 'https://i.loli.net/2018/08/15/5b744ad026a65.png'}
      })
    })
  })
  describe('move card1', () => {
    it('should move card correctly', () => {
      vm.initGame()
      vm.card1()
      expect(vm.cards.card1.num).toEqual('')
    })
  })

  describe('move card2', () => {
    it('should move card correctly', () => {
      vm.initGame()
      vm.card2()
      expect(vm.cards.card2.num).toEqual(7)
    })
  })

  describe('move card3', () => {
    it('should move card correctly', () => {
      vm.initGame()
      vm.card3()
      expect(vm.cards.card3.num).toEqual(5)
    })
  })

  describe('move card4', () => {
    it('should move card correctly', () => {
      vm.initGame()
      vm.card4()
      expect(vm.cards.card4.num).toEqual('')
    })
  })

  describe('move card5', () => {
    it('should move card correctly', () => {
      vm.initGame()
      vm.card5()
      expect(vm.cards.card5.num).toEqual('')
    })
  })

  describe('move card6', () => {
    it('should move card correctly', () => {
      vm.initGame()
      vm.card6()
      expect(vm.cards.card6.num).toEqual(6)
    })
  })

  describe('move card7', () => {
    it('should move card correctly', () => {
      vm.initGame()
      vm.card7()
      expect(vm.cards.card7.num).toEqual('')
    })
  })

  describe('move card8', () => {
    it('should move card correctly', () => {
      vm.initGame()
      vm.card8()
      expect(vm.cards.card8.num).toEqual(8)
    })
  })

  describe('move card9', () => {
    it('should move card correctly', () => {
      vm.initGame()
      vm.card9()
      expect(vm.cards.card9.num).toEqual(1)
    })
  })
})
