<template>
    <div>
			<h1>예금 적금 정보 비교</h1>
			<RouterLink :to="{name: 'deposit'}">예금 목록</RouterLink> |
			<RouterLink :to="{name: 'saving'}">적금 목록</RouterLink>    
			<RouterView/>
    </div>
</template>

<script setup>

</script>

<style scoped>

</style>