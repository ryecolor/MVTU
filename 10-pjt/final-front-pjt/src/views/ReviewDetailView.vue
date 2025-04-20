<template>
  <div>
    <h1>{{ movieTitle }}의 댓글 상세 페이지</h1>
  </div>
  <div>
      <div>
        <h3>제목: {{ review.title }}</h3>
        <p>내용: {{ review.content }}</p>
        <p>작성자 MBTI: {{ userMbti }}</p>
        <p>작성일: {{ review.created_at }}</p>
      </div>
      <div v-if="store.logInUsername === review.username">
        <RouterLink :to="{
          name: 'ReviewUpdateView',
          }">수정하기
          </RouterLink> |
          <RouterLink @click.prevent="deleteReview" to="#">삭제하기</RouterLink>
      </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useMovieStore } from "@/stores/movies"
import { useRoute, useRouter, RouterLink, RouterView } from 'vue-router'

const store = useMovieStore()
const route = useRoute()
const router = useRouter()

const review = ref({})
const movieTitle = ref('')
const userId = ref('')
const userMbti = ref('')

const fetchReviewDetail = async () => {
  try {
    const response = await axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/movies/${route.params.id}/reviews/${route.params.review_id}`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    review.value = response.data
    userId.value = response.data.user
  } catch (error) {
    console.error('리뷰를 불러오는 중 오류가 발생했습니다:', error)
  }
}

const fetchMovieTitle = async () => {
  try {
    const response = await axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/movies/${route.params.id}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    movieTitle.value = response.data.title
  } catch (error) {
    console.error('영화 제목을 불러오는 중 오류가 발생했습니다:', error)
  }
}

const fetchUserProfile = async () => {
  if (!userId.value) {
    console.error('사용자 ID가 없습니다.')
    return
  }
  try {
    const response = await axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/userprofile/${userId.value}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    userMbti.value = response.data.mbti
  } catch (error) {
    console.error('사용자 프로필을 불러오는 중 오류가 발생했습니다:', error)
  }
}

const initializeData = async () => {
  try {
    await Promise.all([fetchReviewDetail(), fetchMovieTitle()])
    await fetchUserProfile()
  } catch (error) {
    console.error('데이터 초기화 중 오류가 발생했습니다:', error)
  }
}

onMounted(() => {
  initializeData()
})

const deleteReview = async () => {
  if (confirm('정말로 이 리뷰를 삭제하시겠습니까?')) {
    try {
      await axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/api/v1/movies/${route.params.id}/reviews/${route.params.review_id}/delete_review/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      console.log('리뷰가 성공적으로 삭제되었습니다.')
      // 삭제 후 영화 상세 페이지로 이동
      router.push({ name: 'MovieRecommendDetail', params: { id: route.params.id } })
    } catch (error) {
      console.error('리뷰 삭제 중 오류가 발생했습니다:', error)
    }
  }
}

</script>

<style scoped>
  *{
      text-align: center;
  }

</style>