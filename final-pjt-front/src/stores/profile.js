import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useProfileStore = defineStore('profile', () => {

  const depositsLabelList = ref([])
  const depositsBasicRateList = ref([])
  const depositsMaxRateList = ref([])

  const savingsLabelList = ref([])
  const savingsBasicRateList = ref([])
  const savingsMaxRateList = ref([])
  const userInfo = ref(null)
  const recommendSavingList = ref([])
  const recommendDepositList = ref([])
  
  return { depositsLabelList, 
    depositsBasicRateList, depositsMaxRateList, 
    savingsLabelList, savingsBasicRateList, savingsMaxRateList, userInfo,
     recommendSavingList, recommendDepositList }
}, {persist: true})
