<template>
<div class="d-flex">
  <nav id="sidebarMenu" class="d-lg-block sidebar bg-white">
    <div class="position-sticky">
      <div class="profile_area">
          <div class="profile_inner d-flex flex-column align-items-center">
            <img class="rounded-circle" src="\src\assets\default.png" width="84" height="84" alt="프로필 이미지">
            <div class="profile text-center" v-if="pStore.userInfo">
              <p class="useid">{{ pStore.userInfo.username }}</p>
              <p class="usemail">{{ pStore.userInfo.email }}</p>
            </div>
          </div>
        </div>
      <div class="list-group list-group-flush mx-3 mt-4">
          <li @click="goToProfile" class="list-group-item list-group-item-action active">내 프로필</li>
          <li @click="goToFinance" class="list-group-item list-group-item-action">금융 프로필</li>
          <li @click="goToPost" class="list-group-item list-group-item-action">내가 쓴 글</li>
          <li @click="goToRecommend" class="list-group-item list-group-item-action">금융 상품 맞춤 추천</li>
          <li @click="goToUpdate" class="list-group-item list-group-item-action">개인 정보 수정</li>
      </div>
    </div>
  </nav>
	<div class="container">
		<RouterView></RouterView>
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
const getUserInfo = () => {
  axios({
    method : 'get',
        url : `${store.API_URL}/accounts/custom/user-detail/${route.params.username}/`,
  })
  .then((res)=>{
    pStore.userInfo = res.data;
    pStore.depositsLabelList.value = [];
    pStore.depositsBasicRateList.value = [];
    pStore.depositsMaxRateList.value = [];
    if (res.data && res.data.subscribed_deposits){
      console.log(res.data);
      res.data.subscribed_deposits.forEach(deposit => {
        pStore.depositsLabelList.value.push(deposit.product_info.fin_prdt_nm)
        pStore.depositsBasicRateList.value.push(deposit.intr_rate)
        pStore.depositsMaxRateList.value.push(deposit.intr_rate2)
      })
    }
    pStore.savingsLabelList.value = [];
    pStore.savingsBasicRateList.value = [];
    pStore.savingsMaxRateList.value = [];
    if (res.data && res.data.subscribed_savings){
      res.data.subscribed_savings.forEach(saving => {
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
const goToProfile = () =>{
  router.push({name: "profile", params: {username: route.params.username}})
}
const goToFinance = () =>{
  router.push({name: "Finance-profile", params: {username: route.params.username}})
}
const goToPost = () =>{
  router.push({name: "User-Posts", params: {username: route.params.username}})
}
const goToRecommend = () =>{
  router.push({name: "Recommend", params: {username: route.params.username}})
}
const goToUpdate = () =>{
  router.push({name: "UpdateUser", params: {username: route.params.username}})
}
onMounted(() => {
  getUserInfo()
})
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  font-family: "Nanum Gothic Coding", monospace;
  font-weight: 400;
}
.sidebar {
  top: 0;
  bottom: 0;
  left: 30px;
  padding: 58px 0 0; /* Height of navbar */
  box-shadow: 0 2px 5px 0 rgb(0 0 0 / 5%), 0 2px 10px 0 rgb(0 0 0 / 5%);
  width: 240px;
  z-index: 600;
}


</style>