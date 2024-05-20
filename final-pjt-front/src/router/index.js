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
import SavingPlanerView from '@/views/savingplaner/SavingPlanerView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import SearchBankView from '@/views/SearchBankView.vue'
import DepositSavingComparisonView from '@/views/DepositSavingComparisonView.vue'
import CommunityCreateView from '@/views/community/CommunityCreateView.vue'
import CommunityListView from '@/views/community/CommunityListView.vue'
import Profile from '@/components/mypage/Profile.vue'
import UpdateUser from '@/components/mypage/UpdateUser.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'start',
      component: StartPageView ,
    },
    {
      path: '/main',
      name: 'main',
      component: MainPageView,
    },
    {
      path: '/profile',
      name: 'mypage',
      component: MyPageView,
      children: [
        {path: ':username', name: 'profile', component: Profile},
        {path: 'update', name: 'updateUser', component: UpdateUser},
      ]
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
      path: '/comparison',
      name: 'comparison',
      component: DepositSavingComparisonView,
      children: [
        {path: 'deposit', name: 'deposit', component: DepositView},
        {path: 'deposit/:id', name: 'depositDetail', component: DepositDetailView},
        {path: 'saving', name:'saving', component: SavingView},
        {path: 'saving/:id', name:'savingDetail', component: SavingDetailView},
      ]
    },
    { path: '/community',
      name: 'community',
      component: CommunityView,
      children: [
        {path: 'list', name: 'community-list', component: CommunityListView},
        {path: ':id', name: 'community-detail', component: CommunityDetailView},
        {path: 'create', name: 'community-create', component: CommunityCreateView},
        {path: 'update/:id', name: 'community-update', component: CommunityCreateView, props:true},
      ]
    },
    {
      path: '/plan',
      name: 'plan',
      component: SavingPlanerView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
    },
  ]
})

export default router
