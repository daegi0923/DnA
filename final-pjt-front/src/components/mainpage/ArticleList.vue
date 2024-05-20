<template>
  <div class="news-container">
    <h1 class="news-heading">경제 뉴스 헤드라인</h1>
    <ul class="news-list">
      <li v-for="news in limitedNewsData" :key="news.title" class="news-item">
        <div class="news-thumbnail">
          <img :src="news.thumbnailUrl" :alt="news.title" />
        </div>
        <div class="news-content">
          <h2 class="news-title">
            <a :href="news.url" target="_blank">{{ news.title }}</a>
          </h2>
          <p class="news-source">출처: {{ news.source }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, computed } from 'vue'

const url = '/api/section/101';
const newsData = ref([]);
const limitedNewsData = computed(() => newsData.value.slice(0, 5));

const getNewsHeadlines = async () => {
  try {
    const response = await axios.get(url);
    const html = response.data;
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const newsElements = Array.from(doc.querySelectorAll('.sa_text_strong'));
    newsData.value = newsElements.map((element) => {
      const newsItem = element.closest('.sa_item');
      const thumbnailElement = newsItem.querySelector('._LAZY_LOADING._LAZY_LOADING_INIT_HIDE');
      const thumbnailUrl = thumbnailElement ? thumbnailElement.getAttribute('data-src') : '';
      const sourceElement = newsItem.querySelector('.sa_text_press');
      const source = sourceElement ? sourceElement.textContent.trim() : '';
      return {
        title: element.textContent.trim(),
        url: element.closest('a').href,
        thumbnailUrl,
        source
      };
    });
  } catch (error) {
    console.error('Error fetching news headlines:', error);
  }
};

onMounted(() => {
  getNewsHeadlines();
});
</script>

<style scoped>
.news-container {
  width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.news-heading {
  font-size: 24px;
  margin-bottom: 20px;
}

.news-list {
  list-style: none;
  padding: 0;
}

.news-item {
  display: flex;
  margin-bottom: 20px;
}

.news-thumbnail img {
  width: 100px;
  height: auto;
  border-radius: 5px;
  margin-right: 20px;
}

.news-content {
  flex: 1;
}

.news-title {
  font-size: 20px;
  margin: 0 0 10px;
}

.news-title a {
  text-decoration: none;
  color: #333;
}

.news-source {
  font-size: 14px;
  color: #666;
  margin: 0;
}
</style>