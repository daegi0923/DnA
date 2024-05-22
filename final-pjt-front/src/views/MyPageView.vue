<template>
	<div class="container">
		<RouterView></RouterView>
	</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()

</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  font-family: "Nanum Gothic Coding", monospace;
  font-weight: 400;
}

</style>