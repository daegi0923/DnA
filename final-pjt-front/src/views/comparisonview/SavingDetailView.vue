<template>
    <div>
      <h1>deposit detail</h1>
      
      <div v-if="product">
        <p>금융회사 명 : {{ product.kor_co_nm }}</p>
        <p>금융 상품명 : {{ product.fin_prdt_nm }}</p>
        <p>가입 대상 : {{ product.join_member }}</p>
        <p>가입 방법 : {{ product.join_way }}</p>
        <p>우대조건 : {{ product.spcl_cnd }}</p>
        <p>기타 유의사항 : {{ product.etc_note }}</p>
        <div v-for="(option, index) in product.savingoption_set" :key="index">
          <hr>
          <p>저축 금리 유형명 : {{ option.intr_rate_type_nm }}</p>
          <p>저축 금리 : {{ option.intr_rate }}</p>
          <p>적립 유형 : {{ option.rsrv_type }}</p>
          <p>적립 유형명 : {{ option.rsrv_type_nm }}</p>
          <p>최고 우대 금리 : {{ option.intr_rate2 }}</p>
          <p>저축 기간 : {{ option.save_trm }}</p>
        </div>
      </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const product = ref(null)
const loadProduct = () => {
  axios({
  method: 'get',
  url: `${store.API_URL}/products/saving-product-options/${route.params.id}/`
})
  .then((response) => {
    console.log(response.data)
    product.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })

}

onMounted(() => {
  loadProduct()
})

</script>

<style scoped>

</style>