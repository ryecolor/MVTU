import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import LogoutView from '@/views/LogoutView.vue'
import MovieRecommend from '@/components/MovieRecommend.vue'
import profileView from '@/views/profileView.vue'
import MovieRecommendDetail from '@/components/MovieRecommendDetail.vue'
import ReviewDetailView from '@/views/ReviewDetailView.vue'
import ReviewUpdateView from '@/views/ReviewUpdateView.vue'
import { useMovieStore } from '@/stores/movies'
import ProfileUpdateView from '@/views/profileUpdateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/logout',
      name: 'LogoutView',
      component: LogoutView
    },
    // mbti에 따른 영화추천을 진행할 페이지
    {
      path: '/recommend',
      name: 'MovieRecommend',
      component: MovieRecommend
    },
    // 로그인된 사용자의 프로필 페이지
    {
      path: '/profile/',
      name: 'profileView',
      component: profileView
    },
    {
      path: '/profileUpdate/',
      name: 'profileUpdateView',
      component: ProfileUpdateView
    },
    {
      path: '/recommend/:id',
      name: 'MovieRecommendDetail',
      component: MovieRecommendDetail
    },
    {
      path: '/recommend/:id/:review_id',
      name: 'ReviewDetailView',
      component: ReviewDetailView
    },
    {
      path: '/recommend/:id/:review_id/update/',
      name: 'ReviewUpdateView',
      component: ReviewUpdateView
    },
  ]
})
// 로그인 전과 후를 구분할 수 있게 해주는 코드
router.beforeEach((to, from) => {
  const store = useMovieStore()
  if (to.name === 'MovieRecommend' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if (to.name === 'profileView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }

})

export default router
