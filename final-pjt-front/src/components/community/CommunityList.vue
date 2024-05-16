<template>
	<div>
		<h3>Article List</h3>
		<CommunityListItem 
		v-for="article in store.articles"
		:key="article.id"
		:article="article"
		/>
	</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import CommunityListItem from '@/components/community/CommunityListItem.vue'

const store = useCounterStore()


</script>

<style scoped>

</style>