<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <RouterLink 
      :to="{ name: 'community-detail', params: { id: article.id }}"
    > 
    [DETAIL]
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})

</script>

<style lang="scss" scoped>

</style>