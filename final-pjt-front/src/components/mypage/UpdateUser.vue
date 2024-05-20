<template>
  <div>
    <h1>회원정보 수정</h1>
    <v-text-field v-model = "emailInput"></v-text-field>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'
const store = useCounterStore()

const router = useRouter()
const route = useRoute()

const emailInput = ref('')

</script>

<style scoped>

</style>