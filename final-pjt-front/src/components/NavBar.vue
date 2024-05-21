<template>
  <div class="nav-container ">
    <RouterLink :to="{name: 'main'}" class="link_line logo-font">
      <img src="@/assets/LogoSymbol.png" alt="Logo" class="logo-img">
      <span class="mx-0">
        금선생
      </span>
    </RouterLink> 
    <div class="menu">  
      <RouterLink :to="{name: 'deposit'}" class="link_line">예금/적금정보</RouterLink> 
      <RouterLink :to="{name: 'searchbank'}" class="link_line">은행찾기</RouterLink> 
      <RouterLink :to="{name: 'exchange'}" class="link_line">환율계산기</RouterLink> 
      <RouterLink :to="{name: 'plan'}" class="link_line">저축도우미</RouterLink> 
      <RouterLink :to="{name: 'community-list'}" class="link_line">게시판</RouterLink>    
    </div>
    <div class="right-header">
      <div v-if="!store.isLogin" class="link">
        <RouterLink :to="{name:'signup'}" class="link">회원가입</RouterLink>  
        <RouterLink :to="{name:'login'}" class="link">로그인</RouterLink>
      </div>
      <div v-else>
        <RouterLink :to="{name:'profile', params:{username: store.user_name}}" class="link"><i class="fa-regular fa-user"></i></RouterLink>
        <button @click="store.logOut" class="link">Logout</button>
      </div>
    </div>
  </div>

</template>
    
<script setup>
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
</script>
    
<style scoped>
.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #112D4E;
  width: 100%;
  font-size: 23px;
  height: 70px;
  padding: 10px; /* 간격 조정 */
  border: 1px solid #112D4E;
  margin-bottom: 50px;
}

.logo {
  display: flex;
  align-items: center;
}

.logo-img {
  width: auto; /* 로고의 최대 너비를 설정 */
  height: 60px; /* 비율을 유지하면서 높이 자동 조정 */
}
.menu {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  font-family : 'Nanum Myeongjo';
}

.link_line {
  text-decoration: none;
  color: white;
}

.right-header {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family : 'Nanum Myeongjo';

}

.link {
  color: white;
  text-decoration: none;
  font-size: 20px;
}

.logo-font {
  font-family : 'Nanum Myeongjo';
  font-weight: 800;

}


span {
  margin: 5px;
}
</style>
