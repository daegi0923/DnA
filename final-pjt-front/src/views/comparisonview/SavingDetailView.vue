<template>
    <div class="container">
      <div v-if="product">
        <h3>{{ product.kor_co_nm }}</h3>
        <h1>{{ product.fin_prdt_nm }}</h1>
        <br>
        <div class="row">
            <div class="info">
              <p>가입 대상 : {{ product.join_member }}</p>
            </div>
            <div class="info">
              <p>가입 방법 : {{ product.join_way }}</p>
            </div>
        </div>
        <div class="info2">
          <p>우대조건 : {{ product.spcl_cnd }}</p>
        </div>
        <div class="info2">
          <p>기타 유의사항 : {{ product.etc_note }}</p>
        </div>
        <v-divider class="border-opacity-100" color="#3F72AF"></v-divider>
        <div class="cardlist-wrapper">
          <div v-for="(option, index) in product.savingoption_set" :key="index" class="cardlist">
            <v-card class="card-container">
              <p>저축 금리 유형명 : {{ option.intr_rate_type_nm }}</p>
              <p>저축 금리 : {{ option.intr_rate }}</p>
              <p>적립 유형 : {{ option.rsrv_type }}</p>
              <p>적립 유형명 : {{ option.rsrv_type_nm }}</p>
              <p>최고 우대 금리 : {{ option.intr_rate2 }}</p>
              <p>저축 기간 : {{ option.save_trm }}</p>
              <v-btn v-if="store.isLogin" @click="subscribeProduct(option.id)" :class="{ 'subscribe': !isSubscribedList[option.id], 'unsubscribe': isSubscribedList[option.id] }">
                <span v-if="isSubscribedList[option.id]">구독 취소 {{ isSubscribedList.id }}</span>
                <span v-else="isSubscribedList[option.id]">구독 {{ isSubscribedList.id }}</span>
              </v-btn>
            </v-card>
          </div>
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
*{
  box-sizing: border-box;
}
.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px;
  font-family: 'Arial', sans-serif;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
  margin-bottom: 20px;
}
.row {
  margin: 0;
  display: flex;
  align-items: space-between;
}
.info {
  flex: 1;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  padding: 10px;
  text-align: center;
  margin: 3px 0;
  margin-right: 20px
}
.info p{
  margin: 0
}
.info:last-child {
  margin-right: 0; /* 마지막 info 요소의 오른쪽 마진 제거 */
}
.info2{
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  padding: 10px;
  text-align: center;
  margin: 20px 0;
}
.info2 p{
  margin: 0
}
.card-container{
  flex: 1;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 10px;
  width: 300px;
}
.cardlist{
  display: inline-block;
  text-align: center;
  margin: 10px;
}
.carelist-wrapper{
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}
.subscribe{
  background-color: #112D4E;
  padding: 5px;
  width: 80px;
  color: white;
  font-weight: bold;
}
.unsubscribe{
  border: 2px solid #112D4E;
  padding: 5px;
  width: 80px;
  font-weight: bold;
}
</style>