<template>
    <div class="top-header">
      <div class="row">
        <img src="" alt="">
        <p>adsf</p>
      </div>
      <div>
        <button>Logout</button>
        <RouterLink :to="{name:'mypage'}"><i class="fa-regular fa-user"></i></RouterLink>
      </div>
    </div>
  </template>
  
  <script setup>
  
  </script>
  
  <style scoped>
  .top-header{
    display: flex;
    justify-content: space-between;
    background-color: #088082;
  }
  </style>