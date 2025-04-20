<template>
  <div>
    <ul>
      <div
        v-for="movie in store.movies"
        :key="movie.pk"
      >
        <h3>{{ movie.pk }}번 게시글</h3>
        <p>제목 : {{ movie.title }}</p>
        <p>내용 : {{ movie.content }}</p>
        <hr>
      </div>
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useMovieStore } from '@/stores/movies'
const store = useMovieStore()

onMounted(() => {
  store.getMovies()
})
</script>

<style lang="scss" scoped>

</style>