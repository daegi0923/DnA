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
          <v-btn v-if="store.isLogin" @click="subscribeProduct(option.id)">
            <span v-if="isSubscribedList[option.id]">구독 취소 {{ isSubscribedList.id }}</span>
            <span v-else="isSubscribedList[option.id]">구독 {{ isSubscribedList.id }}</span>
          </v-btn>

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
const isSubscribedList = ref({})

const loadProduct = () => {
  axios({
  method: 'get',
  url: `${store.API_URL}/products/saving-product-options/${route.params.id}/`
})
  .then((response) => {
    console.log(response.data)
    product.value = response.data
    product.value.savingoption_set.forEach(element => {
      console.log(isSubscribedList);
      checkSubscribed(element.id)

    });
  })
  .catch((error) => {
    console.log(error)
  })

}
const subscribeProduct = (optionId) => {
  axios({
    method: 'post',
    url: `${store.API_URL}/products/subscribe-saving/${optionId}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    console.log(optionId)
    isSubscribedList.value[optionId] = response.data.is_subscribed
    loadProduct()
  })
  .catch((error) => {
    console.log(error)
  })
}

const checkSubscribed = (optionId) => {
  axios({
    method: 'get',
    url: `${store.API_URL}/products/subscribe-saving/${optionId}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    console.log(optionId)
    isSubscribedList.value[optionId] = response.data.is_subscribed
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