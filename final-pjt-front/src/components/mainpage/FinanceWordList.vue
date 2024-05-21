<template>
    <div class="finance-vocabulary">
      <h1 class="vocabulary-heading">금융 단어장</h1>
      <div class="vocabulary-content">
        <p class="current-word">{{ currentWord }}</p>
        <p class="current-description">{{ currentDiscription }}</p>
      </div>
    </div>
  </template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
const currentWord = ref('');
const currentDiscription = ref('')


const updateWord = () => {
    // 현재 단어와 설명이 비어 있는 경우에만 값을 업데이트
    const index = Math.floor(Math.random() * store.vocaList.length);
    currentWord.value = store.vocaList[index].fnceDictNm;
    const description = store.vocaList[index].ksdFnceDictDescContent;
    
    // Remove only HTML tags, not content inside <ksdFnceDictDescContent>
    const tempElement = document.createElement('div');
    tempElement.innerHTML = description;
    const contentInsideTags = tempElement.querySelector('ksdFnceDictDescContent').innerHTML;
        
    // Remove HTML tags and entities from the content inside <ksdFnceDictDescContent>
    const processedContent = contentInsideTags.replace(/&nbsp;/g, '').replace(/<p[^>]*>/g, '').replace(/<\/p>/g, '').replace(/<[^>]+>/g, '').replace(/&[^;]+;/g, '').replace(/p/, '')
    currentDiscription.value = processedContent;
}

// updateWord 함수를 최초에 한 번 호출하여 페이지 로드 시에도 단어가 표시되도록 함
onMounted(async () => {
    await store.getVocaList();
    updateWord();
    // setInterval을 사용하여 5초마다 updateWord 함수 호출
    setInterval(updateWord, 5000);
});

</script>

<style scoped>
.finance-vocabulary {
  height: 386.39px;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
  overflow: hidden;
}

.vocabulary-heading {
  font-size: 24px;
  margin-bottom: 20px;
  text-align: center;
}

.vocabulary-content {
  text-align: center;
  overflow: hidden;
  padding: 10px;
}

.current-word {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
}

.current-description {
  font-size: 16px;
  line-height: 1.5;
  text-overflow: ellipsis;
  max-height: 180px; /* 원하는 최대 높이로 설정하세요 */
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 7; /* 최대 줄 수를 설정하세요 */
}

</style>