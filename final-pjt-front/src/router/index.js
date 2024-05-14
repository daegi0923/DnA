import { createRouter, createWebHistory } from 'vue-router'
import MyPageView from '@/views/MyPageView.vue'
import StartPageView from '@/views/StartPageView.vue'
import MainPageView from '@/views/MainPageView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import CommunityDetailView from '@/views/community/CommunityDetailView.vue'
import CommunityView from '@/views/community/CommunityView.vue'
import DepositDetailView from '@/views/comparisonview/DepositDetailView.vue'
import DepositView from '@/views/comparisonview/DepositView.vue'
import SavingDetailView from '@/views/comparisonview/SavingDetailView.vue'
import SavingView from '@/views/comparisonview/SavingView.vue'
import PlanDetail from '@/views/savingplaner/PlanDetail.vue'
import SavingPlanerView from '@/views/savingplaner/SavingPlanerView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import SearchBankView from '@/views/SearchBankView.vue'
import DepositSavingComparisonView from '@/views/DepositSavingComparisonView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'start',
      component: StartPageView ,
      children: [
        {path: 'login', name: 'login', component: LoginView},
        {path: 'signup', name: 'signup', component: SignUpView},
      ]
    },
    {
      path: '/main',
      name: 'main',
      component: MainPageView,
    },
    {
      path: '/mypage',
      name: 'mypage',
      component: MyPageView,
    },
    {
      path: '/searchbank',
      name:'searchbank',
      component: SearchBankView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView,
      child: [
        {path: 'community/:id', name: 'communitydetail', component: CommunityDetailView},
      ]
    },
    {
      path: '/comparison',
      name: 'comparison',
      component: DepositSavingComparisonView,
      children: [
        {path: 'deposit', name: 'deposit', component: DepositView},
        {path: 'deposit/:id', name: 'depositdetail', component: DepositDetailView},
        {path: 'saving', name:'saving', component: SavingView},
        {path: 'saving/:id', name:'savingdetail', component: SavingDetailView},
      ]
    },
    { path: '/community',
      name: 'community',
      component: CommunityView,
      children: [
        {path: 'community/:id', name: 'communitydetail', component: CommunityDetailView}
      ]
    },
    {
      path: '/plan',
      name: 'plan',
      component: SavingPlanerView,
      children: [
        {path: 'plan/:id', name: 'plandetail', component: PlanDetail},
      ]
    }
  ]
})

export default router
