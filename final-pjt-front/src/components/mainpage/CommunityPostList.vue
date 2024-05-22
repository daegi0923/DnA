<template>
    <div class="community-article-list">
      <h1 class="list-heading">커뮤니티 글 목록</h1>
      <div class="article-list-container">
        <ul class="article-list">
          <li v-for="board in store.articles.slice(0, 10)" :key="board.id" class="article-item">
            <RouterLink :to="{ name: 'community-detail', params: { id: board.id }}" class="article-link">{{ board.title }}</RouterLink>
          </li>
        </ul>
        <RouterLink :to="{ name: 'community-list' }" class="load-more-link">
          <button class="load-more-button">더 보기</button>
        </RouterLink>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter.js'
  const store = useCounterStore()
  </script>
  
  <style scoped>
  .community-article-list {
    width: 100%;
    box-shadow: 0 2px 8px #DBE2EF;
    border-radius: 5px;
    padding: 20px;
    height: 100%;
    position: relative; /* 부모 요소를 상대적으로 설정 */
  }
  
  .list-heading {
    font-size: 24px;
    margin-bottom: 20px;
    font-family: "Nanum Gothic Coding", monospace;
    font-weight: 800;
  }
  
  .article-list-container {
    width: 100%;
    height: 100%; /* 부모 요소의 높이에 맞춤 */
  }
  
  .article-list {
    list-style: none;
    padding: 0;
  }
  
  .article-item {
    margin-bottom: 10px;
  }
  
  .article-link {
    text-decoration: none;
    color: #333;
    font-weight: bold;
    font-size: 18px;
    font-family: "Nanum Gothic Coding", monospace;
    font-weight: 400;
  }
  
  .load-more-link {
    position: absolute; /* 절대적인 위치 설정 */
    bottom: 20px; /* 하단 여백 설정 */
    right: 20px; /* 우측 여백 설정 */
  }
  
  .load-more-button {
    padding: 10px 20px;
    background-color: #3F72AF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .load-more-button:hover {
    background-color: #3F72AF;
  }
  </style>
  