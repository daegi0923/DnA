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
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import CommunityListItem from '@/components/community/CommunityListItem.vue'
import { storeToRefs } from 'pinia'

const store = useCounterStore()


</script>

<style scoped>

</style>