import { createRouter, createWebHistory } from 'vue-router'
import MyPageView from '@/views/MyPageView.vue'
import StartPageView from '@/views/StartpageView.vue'
import MainPageView from '@/views/MainPageView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/mypage/',
      name: 'mypage',
      component: MyPageView,
    },
    {
      path: '/'
      name: 'startpage',
      component: StartPageView 
      children: [
        {path: '/login', name: 'login', component: LoginView},
        {path: ''}
      ]
    },
    {
      path: '/home',
      name: 'home',
      component: MainPageView,
    }
  ]
})

export default router
