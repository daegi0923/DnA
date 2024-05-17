<template>
<div class="nav-container">
    <div class='menu'>  
        <RouterLink :to="{name: 'main'}" class="link_line">Home</RouterLink> |
        <RouterLink :to="{name: 'deposit'}" class="link_line">예금/적금 정보</RouterLink> |
        <RouterLink :to="{name: 'searchbank'}" class="link_line">은행 찾기</RouterLink> |
        <RouterLink :to="{name: 'exchange'}" class="link_line">환율계산기</RouterLink> |
        <RouterLink :to="{name: 'plan'}" class="link_line">저축도우미</RouterLink> |
        <RouterLink :to="{name: 'community-list'}" class="link_line">게시판</RouterLink>    
    </div>
</div>
</template>

<script setup>

</script>

<style scoped>
.nav-container {
display: flex;
justify-content: center; 
background-color: #fff;
width: 100%;
font-size: 23px;
height: 120px;
padding: 10px 200px;
}

.link_line {
    text-decoration: none;
    color: black;
}
</style>