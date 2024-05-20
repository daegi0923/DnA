<template>
	<div>
		<h1>Profile Page</h1>
		<RouterLink :to="{name: 'profile'}">프로필</RouterLink> |
		<RouterLink :to="{name: 'updateUser'}">회원 정보 수정</RouterLink>    
		<RouterView/>
	</div>
</template>

<script setup>

</script>

<style scoped>

</style>