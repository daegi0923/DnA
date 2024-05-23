<template>
  <div class="mt-5">
    <h1 class="text-center mb-4">금융 상품 맞춤 추천</h1>
    <div class="d-flex justify-content-around container">
      <div class="product-container">
        <h3 class="text-center mb-3">정기 예금</h3>
        <div class="d-flex flex-wrap justify-content-center">
          <div class="m-2 flip-card" v-for="(deposit, index) in pStore.recommendDepositList" :key="index">
            <div class="flip-card-inner" @click="goToDepositInfo(deposit.id)">
              <div class=" flip-card-front">
                <div class="mb-3">
                  <img :src="getLogoUrl(deposit.kor_co_nm)" alt="deposit.kor_co_nm" class="bankimg rounded-circle">
                </div>
                <h5 class="">{{ deposit.fin_prdt_nm }}</h5>
                <p class="">{{ deposit.kor_co_nm }}</p>
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
            <div class="flip-card-inner" @click="goToSavingInfo(saving.id)">
              <div class=" flip-card-front">
                <div class="mb-3">
                  <img :src="getLogoUrl(saving.kor_co_nm)" alt="saving.kor_co_nm" class="bankimg rounded-circle">
                </div>
                <h5 class="">{{ saving.fin_prdt_nm }}</h5>
                <p class="">{{ saving.kor_co_nm }}</p>
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
    pStore.recommendSavingList = res.data.recommended_savings
    pStore.recommendDepositList = res.data.recommended_deposits
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
const getLogoUrl = (bankName) => {
  const bankCodes = {
    '경남은행': '/bank/경남은행.png',
    '광주은행': '/bank/광주은행.png',
    '국민은행': '/bank/국민은행.png',
    '농협은행주식회사': '/bank/농협은행.jfif',
    '대구은행': '/bank/대구은행.jfif',
    '부산은행': '/bank/부산은행.png',
    '수협은행': '/bank/수협은행.png',
    '신한은행': '/bank/신한은행.png',
    '우리은행': '/bank/우리은행.jfif',
    '전북은행': '/bank/전북은행.png',
    '제주은행': '/bank/제주은행.png',
    '중소기업은행': '/bank/중소기업은행.png',
    '주식회사 카카오뱅크': '/bank/카카오뱅크.png',
    '주식회사 케이뱅크': '/bank/케이뱅크.jfif',
    '토스뱅크 주식회사': '/bank/토스.jfif',
    'KEB하나은행': '/bank/하나은행.png',
    '한국산업은행': '/bank/한국산업은행.jfif',
    '한국스탠다드차타드은행': '/bank/한국스탠다드차타드은행.png'
  };
  return bankCodes[bankName] || '';
};


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
.bankimg{
  width: 90px;
  margin-right : 0px;
}

</style>