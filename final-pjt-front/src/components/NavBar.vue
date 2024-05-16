<template>
<div>
    <div>
        <div class="nav-container">
            <div class='menu'>  
                <p>Home</p>
                <RouterLink :to="{name: 'searchbank'}">searchbank</RouterLink> |
                <RouterLink :to="{name: 'community-list'}">community</RouterLink>    
            </div>
        </div>
    </div> 
</div>
</template>

<script setup>

</script>

<style scoped>
.nav-container {
display: flex; /* 주축과 교차축 나눠서 아이템식 */
justify-content: space-between;
background-color: #fff;
width: 100%;
height: 120px;
padding: 0px 200px;
}
</style>