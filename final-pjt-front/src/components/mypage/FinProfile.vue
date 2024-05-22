<template>
  <div>
    <div class="col-12">
      <div class="card">
        <h3 class="card-header text-white card-title" >금융정보</h3>
        <ul class="list-group list-group-flush">
          <li class="list-group-item">목표 저축 금액: {{ pStore.userInfo.target_savings }}</li>
          <li class="list-group-item">연 수입: {{ pStore.userInfo.annual_income }}</li>
          <li class="list-group-item">주 거래 은행: {{ pStore.userInfo.primary_bank }}</li>
        </ul>
      </div>
    </div>
    <div class="row mt-4">
          <div class="col-12">
            <div class="card">
              <h3 class="card-header text-white card-title ">가입한 예금 상품</h3>
              <div class="card-body">
                <Graph :productType="'deposit'"></Graph>
                <table class="table table-hover">
                  <thead>
                    <tr>
                      <th>은행명</th>
                      <th>상품명</th>
                      <th>기본 금리</th>
                      <th>최고 금리</th>
                      <th>금리 유형</th>
                      <th>저축 기간</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="product in pStore.userInfo.subscribed_deposits" :key="product.id" @click="goToDepositInfo(product.product_info.id)">
                      <td>{{ product.product_info.kor_co_nm }}</td>
                      <td>
                        {{ product.product_info.fin_prdt_nm }}
                      </td>
                      <td>{{ product.intr_rate }}</td>
                      <td>{{ product.intr_rate2 }}</td>
                      <td>{{ product.intr_rate_type_nm }}</td>
                      <td>{{ product.save_trm }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          
          <div class="col-12 mt-4">
            <div class="card">
              <h3 class="card-header text-white card-title ">가입한 적금 상품</h3>
              <div class="card-body">
                <Graph :productType="'saving'"></Graph>
                <table class="table table-hover">
                  <thead>
                    <tr>
                      <th>은행명</th>
                      <th>상품명</th>
                      <th>기본 금리</th>
                      <th>최고 금리</th>
                      <th>금리 유형</th>
                      <th>저축 기간</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="product in pStore.userInfo.subscribed_savings" :key="product.id" @click="goToSavingInfo(product.product_info.id)">
                      <td>{{ product.product_info.kor_co_nm }}</td>
                      <td>
                        {{ product.product_info.fin_prdt_nm }}
                      </td>
                      <td>{{ product.intr_rate }}</td>
                      <td>{{ product.intr_rate2 }}</td>
                      <td>{{ product.intr_rate_type_nm }}</td>
                      <td>{{ product.save_trm }}</td>
                    </tr>
                  </tbody>
                </table>
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
import Graph from '@/components/mypage/Graph.vue'
const router = useRouter()
const pStore = useProfileStore()
onMounted(()=> {
  pStore.getUserInfo()
})
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
</script>

<style scoped>
.card-title {
  background-color: #112D4E;
}

</style>