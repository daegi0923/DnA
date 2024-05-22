<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">
        <div class="profile_area">
          <div class="profile_inner d-flex flex-column align-items-center">
            <img class="rounded-circle" src="\src\assets\default.png" width="84" height="84" alt="프로필 이미지">
            <div class="profile text-center">
              <p class="useid">{{ userInfo.username }}</p>
              <p class="usemail">{{ userInfo.email }}</p>
              <RouterLink :to="{name: 'updateUser', params:{username:store.username}}">회원 정보 수정</RouterLink>    
            </div>
          </div>
        </div>
        <!-- 내용 영역 -->
        <div class="row">
          <div class="col-12">
            <div class="card">
              <h3 class="card-header text-white card-title" >내 프로필</h3>
              <ul class="list-group list-group-flush">
                <li class="list-group-item">성별: {{ userInfo.gender }}</li>
                <li class="list-group-item">이메일: {{ userInfo.email }}</li>
                <li class="list-group-item">생년월일: {{ userInfo.birthday }}</li>
                <li class="list-group-item">주소: {{ userInfo.address }}</li>
              </ul>
            </div>
          </div>

          <div class="col-12">
            <div class="card">
              <h3 class="card-header text-white card-title" >금융정보</h3>
              <ul class="list-group list-group-flush">
                <li class="list-group-item">목표 저축 금액: {{ userInfo.target_savings }}</li>
                <li class="list-group-item">연 수입: {{ userInfo.annual_income }}</li>
                <li class="list-group-item">주 거래 은행: {{ userInfo.primary_bank }}</li>
              </ul>
            </div>
          </div>


        <div class="row mt-4">
          <div class="col-12">
            <div class="card">
              <h3 class="card-header text-white card-title ">가입한 예금 상품</h3>
              <div class="card-body">
                <Graph :productType="'deposit'"></Graph>
                <table class="table">
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
                    <tr v-for="product in userInfo.subscribed_deposits" :key="product.id">
                      <td>{{ product.product_info.kor_co_nm }}</td>
                      <td>
                        <router-link :to="{name: 'depositDetail', params:{id: product.product_info.id}}">{{ product.product_info.fin_prdt_nm }}</router-link>
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

          
          <div class="col-12">
            <div class="card">
              <h3 class="card-header text-white card-title ">가입한 적금 상품</h3>
              <div class="card-body">
                <Graph :productType="'saving'"></Graph>
                <table class="table">
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
                    <tr v-for="product in userInfo.subscribed_savings" :key="product.id">
                      <td>{{ product.product_info.kor_co_nm }}</td>
                      <td>
                        <router-link :to="{name: 'depositDetail', params:{id: product.product_info.id}}">{{ product.product_info.fin_prdt_nm }}</router-link>
                      </td>
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
        </div>

          <div class="col-12">
            <div class="card">
              <h3 class="card-header text-white card-title" >작성한 게시글 목록</h3>
              <ul class="list-group list-group-flush">
                <li class="list-group-item" v-for="post in userInfo.board_set" :key="post.id">
                  <router-link :to="`/community/${post.id}`">{{ post.title }}</router-link>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="row mt-4">
          <div class="col-12">
            <div class="card">
              <h3 class="card-header text-white card-title" >작성한 댓글 목록</h3>
              <ul class="list-group list-group-flush">
                <li class="list-group-item" v-for="comment in userInfo.comment_set" :key="comment.id">
                  <router-link :to="`/community/${comment.board.id}`">{{ comment.content }}</router-link>
                </li>
              </ul>
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

const store = useCounterStore()
const userInfo = ref({})
const pStore = useProfileStore()

const router = useRouter()
const route = useRoute()
const getUserInfo = () => {
  axios({
    method : 'get',
        url : `${store.API_URL}/accounts/custom/user-detail/${route.params.username}/`,
  })
  .then((res)=>{
    console.log(res.data);
    userInfo.value = res.data;
    pStore.depositsLabelList.value = [];
    pStore.depositsBasicRateList.value = [];
    pStore.depositsMaxRateList.value = [];
    if (userInfo.value && userInfo.value.subscribed_deposits){
      userInfo.value.subscribed_deposits.forEach(deposit => {
        pStore.depositsLabelList.value.push(deposit.product_info.fin_prdt_nm)
        pStore.depositsBasicRateList.value.push(deposit.intr_rate)
        pStore.depositsMaxRateList.value.push(deposit.intr_rate2)
      })
    }
    pStore.savingsLabelList.value = [];
    pStore.savingsBasicRateList.value = [];
    pStore.savingsMaxRateList.value = [];
    if (userInfo.value && userInfo.value.subscribed_savings){
      userInfo.value.subscribed_savings.forEach(saving => {
        pStore.savingsLabelList.value.push(saving.product_info.fin_prdt_nm)
        pStore.savingsBasicRateList.value.push(saving.intr_rate)
        pStore.savingsMaxRateList?.value.push(saving.intr_rate2)
      })
    }
})
  .catch((err)=>{
    console.log(err);
  })
}

onMounted(() => {
  getUserInfo()
})
</script>

<style scoped>
.card-title {
  background-color: #112D4E;
}
</style> 
