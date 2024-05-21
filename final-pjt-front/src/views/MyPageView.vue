<template>
	<div>
		<RouterView></RouterView>
	</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()

</script>

<style scoped>

</style>