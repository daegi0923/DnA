<template>
    <div>
      <h1>Profile</h1>
      <div v-if="userInfo">
        <p>user id : {{ userInfo.id }}</p>
        <p>user email : {{ userInfo.email }}</p>
        <p>목표 저축 금액 : {{ userInfo.target_savings }}</p>
        <p>연 수입 : {{ userInfo.annual_income }}</p>
        <p>주 거래 은행 : {{ userInfo.primary_bank }}</p>
        <hr>
        <h3>{{ userInfo.username }} 님이 작성한 게시글 목록 </h3>
        <ul>
          <li v-for="post in userInfo.board_set" :key="post.id">
            <router-link :to="`/community/${post.id}`">{{ post.title }}</router-link>
          </li>
        </ul>
        <hr>
        <h3>{{ userInfo.username }} 님이 작성한 댓글 목록 </h3>
        <ul>
          <li v-for="comment in userInfo.comment_set" :key="comment.id">
            <router-link :to="`/community/${comment.board.id}`">{{ comment.content }}</router-link>
          </li>
        </ul>
        <hr>
        <h3>{{ userInfo.username }} 님이 가입한 정기 예금 상품 목록</h3>
        <ul>
          <li v-for="product in userInfo.subscribed_deposits" :key="product.id">
            <router-link :to="{name: 'depositDetail', params:{id: product.product_info.id}}">{{ product.product_info.fin_prdt_nm }}</router-link>
            <p>기본 금리 : {{ product.intr_rate }}</p>
            <p>최고 금리 : {{ product.intr_rate2 }}</p>
            <p>금리 유형 : {{ product.intr_rate_type_nm }}</p>
            <p>저축 기간 : {{ product.save_trm }}</p>
          </li>
        </ul>
        <hr>
        <h3>{{ userInfo.username }} 님이 가입한 적금 상품 목록</h3>
        <ul>
          <li v-for="product in userInfo.subscribed_savings" :key="product.id">
            <router-link :to="{name: 'savingDetail', params:{id: product.product_info.id}}">{{ product.product_info.fin_prdt_nm }}</router-link>
            <p>기본 금리 : {{ product.intr_rate }}</p>
            <p>최고 금리 : {{ product.intr_rate2 }}</p>
            <p>금리 유형 : {{ product.intr_rate_type_nm }}</p>
            <p>저축 기간 : {{ product.save_trm }}</p>
          </li>
        </ul>
      </div>
      <h3>금리 그래프</h3>
      <Graph :userInfo="userInfo"></Graph>
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
    pStore.labels.value = []
    pStore.basicRates.value = []
    pStore.maxRates.value = []
    console.log(Boolean(userInfo.value));
    console.log(Boolean(userInfo.subscribed_deposits));
    if (userInfo.value && userInfo.value.subscribed_deposits){
      userInfo.value.subscribed_deposits.forEach(deposit => {
        pStore.labels.value.push(deposit.product_info.fin_prdt_nm)
        pStore.basicRates.value.push(deposit.intr_rate)
        pStore.maxRates.value.push(deposit.intr_rate2)
      })
  }})
  .catch((err)=>{
    console.log(err);
  })
}

onMounted(() => {
  getUserInfo()
  console.log(pStore.labels.value);
  console.log(pStore.basicRates.value);
  console.log(pStore.maxRates.value);
})
</script>

<style scoped>

</style>