import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useProfileStore = defineStore('profile', () => {
  const labels = ref([])
  const basicRates = ref([])
  const maxRates = ref([])
  const updateChartData = () => {
    labels.value = []
    basicRates.value = []
    maxRates.value = []
    if (userInfo && userInfo.subscribed_deposits){
      userInfo.subscribed_deposits.forEach(deposit => {
        labels.value.push(deposit.product_info.fin_prdt_nm)
        basicRates.value.push(deposit.intr_rate)
        maxRates.value.push(deposit.intr_rate2)
      })
    }
  }
  
  
  return { labels, basicRates, maxRates}

   
}, { persist: true })
