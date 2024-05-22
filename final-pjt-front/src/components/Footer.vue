<template>
<v-footer class="footer">
    <img src="@/assets/Logo.png" alt="">
    <p>Copyright &#9400 {{ new Date().getFullYear() }} All Rights Reserved. github : https://github.com/daegi0923 https://github.com/akeroroh</p>
</v-footer>
</template>

<script setup>

</script>

<style scoped>
.footer{
    display: flex;
    color: white;
    justify-content: center;
    margin-top: 40px;
    background-color: #DBE2EF;
    height: 70px
}
img{
    width: 50px;
    height: auto;
    margin: 0 20px
}
p{
    margin: 0
}
</style>