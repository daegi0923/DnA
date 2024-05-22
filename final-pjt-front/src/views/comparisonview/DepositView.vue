<template>
	<div class="container">
		<h1>예금 목록</h1>
		<DepositList></DepositList>
	</div>
</template>

<script setup>
import DepositList from '@/components/depositcomparison/DepositList.vue'
</script>

<style scoped>
.container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 30px;
    font-family: 'Arial', sans-serif;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
	margin-bottom: 20px;
}
h1{
    margin: 20px 0
}
</style>