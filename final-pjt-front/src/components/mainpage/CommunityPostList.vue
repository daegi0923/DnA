<template>
<h1>커뮤니티 글 목록</h1>
<div>
    <ul>
        <li v-for="board in store.articles.slice(0, 10)" :key="board.id">
            <RouterLink class="link" :to="{ name: 'community-detail', params: { id: board.id }}">{{ board.title }}</RouterLink>
        </li>
    </ul>
    <RouterLink :to="{name: 'community'}">
      <button>더 보기</button>
    </RouterLink>
</div>
</template>

<script setup>
import {useCounterStore} from '@/stores/counter.js'
const store = useCounterStore()

</script>

<style scoped>
.link{
    text-decoration: none;
    color: black;
}
</style>