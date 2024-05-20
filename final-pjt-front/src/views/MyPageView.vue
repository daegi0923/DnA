<template>
	<div>
		<h1>Profile Page</h1>
		<RouterLink :to="{name: 'profile', params:{username:store.username}}">프로필</RouterLink> |
		<RouterLink :to="{name: 'updateUser', params:{username:store.username}}">회원 정보 수정</RouterLink>    
		<RouterView/>
	</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()

</script>

<style scoped>

</style>