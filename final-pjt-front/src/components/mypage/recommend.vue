<template>
    <div>
      금융상품 추천 페이지입니다..
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useProfileStore } from '@/stores/profile'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const store = useCounterStore()
const pStore = useProfileStore()

const router = useRouter()
const route = useRoute()

const getRecommend = () => {
  axios({
    method : 'get',
    url : `${store.API_URL}/products/recommend/`,
    headers: { Authorization: `Token ${store.token}` }
  })
  .then((res) => {
    console.log(res.data)
    pStore.recommendSavingList = res.data.recommended_products.recommended_deposits
    pStore.recommendDepositList = res.data.recommended_products.recommended_savings
  })
}

onMounted(() => { 
  getRecommend() 
  })
</script>

<style scoped>

</style>