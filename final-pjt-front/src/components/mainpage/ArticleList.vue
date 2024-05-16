<template>
  <div class="news-container">
    <h1>경제 뉴스 헤드라인</h1>
    <ul class="news-list">
      <li v-for="news in limitedNewsData" :key="news.title">
        <div class="news-item">
          <img :src="news.thumbnailUrl" :alt="news.title" class="news-thumbnail" />
          <div class="news-content">
            <h2 class="news-title">
              <a :href="news.url" target="_blank">{{ news.title }}</a>
            </h2>
            <p class="news-source">{{ news.source }}</p>
          </div>
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

<style>
.news-item {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.news-thumbnail {
  width: 100px;
  height: 75px;
  object-fit: cover;
  margin-right: 1rem;
}

.news-content {
  flex: 1;
}

.news-title {
  margin: 0;
  font-size: 1rem;
}

.news-source {
  margin: 0.25rem 0 0;
  font-size: 0.875rem;
  color: #666;
}
</style>