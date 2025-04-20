<template>
  <h1>댓글 수정 페이지</h1>
  <div>
    <form @submit.prevent="submitComment">
      <div>
        <label for="content">내용:</label>
        <textarea 
          id="content" 
          v-model="comment.content" 
          required
        ></textarea>
      </div>
      <button type="submit">수정하기</button>
    </form>
  </div>
  <RouterLink 
    :to="{ name: 'MovieRecommendDetailView', 
    params: { id: $route.params.id }
  }">
    [뒤로 가기]
  </RouterLink>
</template>

<script setup>
  import { RouterLink, useRoute, useRouter } from 'vue-router'
  import { ref } from 'vue'
  import axios from 'axios'
  import { useMovieStore } from '@/stores/movies'


  const route = useRoute()
  const router = useRouter()
  const store = useMovieStore()

  const comment = ref({
    title: '',
    content: ''
  })
  console.log(route.params)
  const submitComment = () => {
    const movieId = route.params.id
    axios({
      method: 'put',
      url: `http://127.0.0.1:8000/api/v1/movies/${movieId}/reviews/${route.params.review_id}/update_review/`,
      data: {
        title: comment.value.title,
        content: comment.value.content,
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then((res) => router.push({ name: 'ReviewDetailView', params: { id: movieId } }))
    .catch((error) => {
    console.error('댓글 제출 중 오류 발생:', error)
    })
  }
</script>

<style scoped>

</style>