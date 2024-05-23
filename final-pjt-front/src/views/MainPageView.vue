<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12" md="4">
        <Carousel />
      </v-col>
      <v-col cols="12" md="8">
        <v-row>
          <v-col cols="12" md="6" v-for="(component, index) in components" :key="index">
            <component :is="component" />
          </v-col>
        </v-row>
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

const components = [
  ArticleList,
  CommunityPostList,
  ExchangeCalculator,
  FinanceWordList
]
</script>

<style scoped>
.content-container {
  display: flex;
  flex-wrap: wrap;
}

.main-content {
  display: flex;
  flex-direction: row;
  gap: 0px;
}
</style>
