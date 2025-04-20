<template>
  <div>
    <h1>로그아웃 페이지</h1>
    <p>로그아웃 하시겠습니까?</p>
    <button @click="logout">Logout</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useMovieStore } from '@/stores/movies'

const router = useRouter()
const store = useMovieStore()

const logout = async function () {
  try {
    await store.logout()
    // 로그아웃 성공 후 로그인 페이지나 홈페이지로 리다이렉트
    router.push({ name: 'home' })
  } catch (error) {
    console.error('Logout failed:', error)
    // 에러 처리 (예: 사용자에게 알림 표시)
  }
}
</script>

<style scoped>

</style>