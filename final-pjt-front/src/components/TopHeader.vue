<template>
    <div class="top-header">
      <div class="row">
        <img src="" alt="">
      </div>
      <div class="right-header">
        <div v-if="!store.isLogin">
          <RouterLink :to="{name:'signup'}" class="link" > 회원 가입 </RouterLink>
          <RouterLink :to="{name:'login'}" class="link">로그인</RouterLink>
        </div>
        <div v-else>
          <RouterLink :to="{name:'mypage'}" class="link"><i class="fa-regular fa-user"></i></RouterLink>
          <button @click = store.logOut class="link">Logout</button>
        </div>
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
    color: white;
    padding: 10px
  }

  .link{
    color:white;
    text-decoration: none;
    font-size: 20px
  }

  .right-header{
    display: flex;
  }

  span{
    margin: 5px
  }
  </style>