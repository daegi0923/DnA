<template>
<div>
    <Carousel />
    <ArticleList />
    <CommunityPostList />
    <ExchangeCalculator />
    <FinanceWordList />
</div>
</template>

<script setup>
import ExchangeCalculator from '@/components/exchange/ExchangeCalculator..vue'
import Carousel from '@/components/mainpage/Carousel.vue'
import ArticleList from '@/components/mainpage/ArticleList.vue'
import CommunityPostList from '@/components/mainpage/CommunityPostList.vue'
import FinanceWordList from '@/components/mainpage/FinanceWordList.vue'
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()


</script>

<style scoped>
.content-container {
  display: flex; /* 자식 요소를 가로로 정렬 */
  flex-wrap: wrap; /* 자식 요소가 너무 많아서 한 줄에 다 들어가지 않을 경우 줄 바꿈 */
}

.main-content {
  display: flex;
  flex-direction: row; /* 내부 컨텐츠를 가로로 배치 */
  gap: 0px
}
</style>