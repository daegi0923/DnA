import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

export const useProfileStore = defineStore('profile', () => {
  const store = useCounterStore()
  const route = useRoute()
  const router = useRouter()

  const depositsLabelList = ref([])
  const depositsBasicRateList = ref([])
  const depositsMaxRateList = ref([])
  
  const savingsLabelList = ref([])
  const savingsBasicRateList = ref([])
  const savingsMaxRateList = ref([])
  const userInfo = ref(null)
  const recommendSavingList = ref([])
  const recommendDepositList = ref([])
  const getUserInfo = () => {
    axios({
      method : 'get',
          url : `${store.API_URL}/accounts/custom/user-detail/${route.params.username}/`,
    })
    .then((res)=>{
      userInfo.value = res.data;
      depositsLabelList.value = [];
      depositsBasicRateList.value = [];
      depositsMaxRateList.value = [];
      if (res.data && res.data.subscribed_deposits){
        console.log(res.data);
        res.data.subscribed_deposits.forEach(deposit => {
          depositsLabelList.value.push(deposit.product_info.fin_prdt_nm)
          depositsBasicRateList.value.push(deposit.intr_rate)
          depositsMaxRateList.value.push(deposit.intr_rate2)
        })
      }
      savingsLabelList.value = [];
      savingsBasicRateList.value = [];
      savingsMaxRateList.value = [];
      if (res.data && res.data.subscribed_savings){
        res.data.subscribed_savings.forEach(saving => {
          savingsLabelList.value.push(saving.product_info.fin_prdt_nm)
          savingsBasicRateList.value.push(saving.intr_rate)
          savingsMaxRateList?.value.push(saving.intr_rate2)
        })
      }
  })
    .catch((err)=>{
      console.log(err);
    })
  }
  const goToDepositInfo = (product_id) => {
    router.push({
      name: 'depositDetail',
      params: {
        id: product_id
      }
    })
  }
  const goToSavingInfo = (product_id) => {
    router.push({
      name: 'savingDetail',
      params: {
        id: product_id
      }
    })
  }
  
  return { depositsLabelList, 
    depositsBasicRateList, depositsMaxRateList, 
    savingsLabelList, savingsBasicRateList, savingsMaxRateList, userInfo,
     recommendSavingList, recommendDepositList, getUserInfo, goToDepositInfo, goToSavingInfo }
}, {persist: true})
