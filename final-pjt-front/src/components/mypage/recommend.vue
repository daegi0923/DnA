<template>
  <div class="mt-5">
    <h1 class="text-center mb-4">금융 상품 맞춤 추천</h1>
    <div class="d-flex justify-content-around container">
      <div class="product-container">
        <h3 class="text-center mb-3">정기 예금</h3>
        <div class="d-flex flex-wrap justify-content-center">
          <div class="m-2 flip-card" v-for="(deposit, index) in pStore.recommendDepositList" :key="index">
            <div class="flip-card-inner" @click="goToDepositInfo(deposit.product_info.id)">
              <div class=" flip-card-front">
                <h4 class="">{{ deposit.product_info.fin_prdt_nm }}</h4>
                <p class="">{{ deposit.product_info.kor_co_nm }}</p>
              </div>
              <div class=" flip-card-back">
                <h4 class="">상품정보 보러가기</h4>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="product-container">
        <h3 class="text-center mb-3">적금</h3>
        <div class="d-flex flex-wrap justify-content-center">
          <div class="m-2 flip-card" v-for="(saving, index) in pStore.recommendSavingList" :key="index">
            <div class="flip-card-inner" @click="goToSavingInfo(saving.product_info.id)">
              <div class=" flip-card-front">
                <h4 class="">{{ saving.product_info.fin_prdt_nm }}</h4>
                <p class="">{{ saving.product_info.kor_co_nm }}</p>
              </div>
              <div class=" flip-card-back">
                <h4>
                  상품정보 보러가기
                </h4>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
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
    method: 'get',
    url: `${store.API_URL}/products/recommend/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    console.log(res.data)
    pStore.recommendSavingList = res.data.recommended_products.recommended_savings
    pStore.recommendDepositList = res.data.recommended_products.recommended_deposits
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


onMounted(() => {
  getRecommend()
})
</script>

<style scoped>
.product-card {
  transition: transform 0.8s;
  transform-style: preserve-3d;
  border-radius : 15px;
}
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #DBE2EF;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  font-family: "Nanum Gothic Coding", monospace;
  font-weight: 400;
}

.flip-card {
  background-color: transparent;
  width: 300px;
  height: 225px;
  perspective: 1000px;

}

.flip-card-inner {
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.6s;
  transform-style: preserve-3d;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  border-radius : 15px;

}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
  position: absolute;
  display : flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  border-radius : 15px;
}

.flip-card-front {
  background-color: #112D4E;
  color: white;
  justify-content: flex-end;

}

.flip-card-back {
  background-color: #3F72AF;
  color: white;
  transform: rotateY(180deg);
  justify-content: center;

}

</style>