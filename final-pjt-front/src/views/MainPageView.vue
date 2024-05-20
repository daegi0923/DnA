<template>
 
  <v-container fluid>
    <!-- 첫번째 줄: 코로셀 -->
    <v-row>
      <v-col cols="12">
        <Carousel />
      </v-col>
    </v-row>

    <!-- 두번째 줄: 3등분 (왼쪽 환율계산기, 나머지 2등분은 기사) -->
    <v-row>
      <v-col cols="12" md="4">
        <ExchangeCalculator />
      </v-col>
      <v-col cols="12" md="8">
        <v-row>
          <v-col cols="12" md="6">
            <ArticleList />
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- 세번째 줄: 2등분 (왼쪽 게시판, 오른쪽 단어장) -->
    <v-row>
      <v-col cols="12" md="6">
        <CommunityPostList />
      </v-col>
      <v-col cols="12" md="6">
        <FinanceWordList />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import ExchangeCalculator from '@/components/exchange/ExchangeCalculator.vue'
import Carousel from '@/components/mainpage/Carousel.vue'
import ArticleList from '@/components/mainpage/ArticleList.vue'
import CommunityPostList from '@/components/mainpage/CommunityPostList.vue'
import FinanceWordList from '@/components/mainpage/FinanceWordList.vue'
</script>

<style scoped>

</style>
