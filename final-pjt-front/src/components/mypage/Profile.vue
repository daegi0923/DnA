<template>
  <div class="container-fluid">
    <div class="profile_area">
      <div class="profile_inner d-flex flex-column align-items-center">
        <img class="rounded-circle" src="\src\assets\default.png" width="84" height="84" alt="프로필 이미지">
        <div class="profile text-center">
          <p class="useid">{{ pStore.userInfo.username }}</p>
          <p class="usemail">{{ pStore.userInfo.email }}</p>
          <RouterLink :to="{name: 'UpdateUser', params:{username:store.username}}">회원 정보 수정</RouterLink>    
        </div>
      </div>
    </div>
    <!-- 내용 영역 -->
    <div class="card">
      <h3 class="card-header text-white card-title" >내 프로필</h3>
      <ul class="list-group list-group-flush">
        <li class="list-group-item">성별: {{ pStore.userInfo.gender }}</li>
        <li class="list-group-item">이메일: {{ pStore.userInfo.email }}</li>
        <li class="list-group-item">생년월일: {{ pStore.userInfo.birthday }}</li>
        <li class="list-group-item">주소: {{ pStore.userInfo.address }}</li>
      </ul>
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
const pStore = useProfileStore()
const router = useRouter()
const route = useRoute()

</script>

<style scoped>
.card-title {
  background-color: #112D4E;
  
}
</style> 
