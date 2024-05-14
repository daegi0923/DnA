<template>
    <div class="top-header">
      <div class="row">
        <img src="" alt="">
        <p>adsf</p>
      </div>
      <div>
        <RouterLink :to="{name:'mypage'}"><i class="fa-regular fa-user"></i></RouterLink> | 
        <div v-if="!store.isLogin">
        <RouterLink :to="{name:'signup'}" >회원 가입</RouterLink> | 
        <RouterLink :to="{name:'login'}">로그인</RouterLink>
        </div>

        <button v-else @click = store.logOut>Logout</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter'
  const store = useCounterStore()

  </script>
  
  <style scoped>
  .top-header{
    display: flex;
    justify-content: space-between;
    background-color: #088082;
  }
  </style>