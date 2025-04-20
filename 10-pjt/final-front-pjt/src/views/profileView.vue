<template>
  <div>
    <br>
    <!-- 추후에 프로필 이미지를 업데이트 하면 변경됨 -->
    <div>
      <h1 class="title">프로필 페이지</h1>
      <img v-if="profile.mbti === 'ISFP'" class="profile" src="@/assets/MBTI/ISFP.png" alt="no img">
      <img v-if="profile.mbti === 'INFP'" class="profile" src="@/assets/MBTI/INFP.png" alt="no img">
      <img v-if="profile.mbti === 'ISTP'" class="profile" src="@/assets/MBTI/ISTP.png" alt="no img">
      <img v-if="profile.mbti === 'INTP'" class="profile" src="@/assets/MBTI/INTP.png" alt="no img">
      <img v-if="profile.mbti === 'ISFJ'" class="profile" src="@/assets/MBTI/ISFJ.png" alt="no img">
      <img v-if="profile.mbti === 'INFJ'" class="profile" src="@/assets/MBTI/INFJ.png" alt="no img">
      <img v-if="profile.mbti === 'ISTJ'" class="profile" src="@/assets/MBTI/ISTJ.png" alt="no img">
      <img v-if="profile.mbti === 'INTJ'" class="profile" src="@/assets/MBTI/INTJ.png" alt="no img">
      <img v-if="profile.mbti === 'ESFP'" class="profile" src="@/assets/MBTI/ESFP.png" alt="no img">
      <img v-if="profile.mbti === 'ENFP'" class="profile" src="@/assets/MBTI/ENFP.png" alt="no img">
      <img v-if="profile.mbti === 'ESTP'" class="profile" src="@/assets/MBTI/ESTP.png" alt="no img">
      <img v-if="profile.mbti === 'ENTP'" class="profile" src="@/assets/MBTI/ENTP.png" alt="no img">
      <img v-if="profile.mbti === 'ESFJ'" class="profile" src="@/assets/MBTI/ESFJ.png" alt="no img">
      <img v-if="profile.mbti === 'ENFJ'" class="profile" src="@/assets/MBTI/ENFJ.png" alt="no img">
      <img v-if="profile.mbti === 'ESTJ'" class="profile" src="@/assets/MBTI/ESTJ.png" alt="no img">
      <img v-if="profile.mbti === 'ENTJ'" class="profile" src="@/assets/MBTI/ENTJ.png" alt="no img">
      <img v-if="profile.mbti === ''" class="profile" src="@/assets/profile.jpg" alt="no img">
      <br>
      <div>
        <div>
          <span>USERNAME</span>
        </div>
        <div>
          <p>{{ profile.username }}</p>
        </div>
        <br>
        <div>
          <span>MBTI</span>
        </div>
        <div>
          <p>{{ profile.mbti }}</p>
        </div>  
      </div>
    </div>
    <div>
      <RouterLink class="start" :to="{name: 'home',}">HOME</RouterLink>
    </div>
    <div>
      <RouterLink class="edit" :to="{name: 'profileUpdateView',}">EDIT</RouterLink>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useMovieStore } from '@/stores/movies'
  import axios from 'axios'
  import { useRouter, RouterLink } from 'vue-router';

  const store = useMovieStore()
  const router = useRouter()
  const profile = ref([])

  const fetchprofile = async () => {
    try {
      const response = await axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/get-profile/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      profile.value = response.data
    } catch (error) {
      console.error('리뷰를 불러오는 중 오류가 발생했습니다:', error)
    }
  }

  onMounted(() => {
    fetchprofile()
  })

</script>

<style scoped>

  .title {
    margin-left: 25px;
    writing-mode: vertical-lr;
    text-orientation: upright;
    position: absolute;
    left: 0px;
    top: 350px;
    font-size: 24px;
    font-family: 'Nanum Myeongjo', serif;
    letter-spacing: 8px;
    display: block;
  }

  img {
    margin-bottom: 20px;
  }

  .profile {
    height: 150px;
    width: 150px;
    border: 2px solid white;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  div {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 5px;
    font-family: Nanum Myeongjo, sans-serif;
    font-weight: 600;
  }

  h1 {
    font-size: 24px;
    color: #666;
    margin-bottom: 10px;
    letter-spacing: normal;
  }

  span {
    color: #666;
    margin: 2px 0;
    letter-spacing: normal;
  }

  p {
    color: #333;
    font-size: 25px;
    margin: 5px 0;
    letter-spacing: normal;
    font-weight: 600;
  }

  .start {
    margin-top: 20px;
    border-radius: 175px;
    background: #fff;
    box-shadow: 0 4px 10px #a4abbd;
    display: flex;
    justify-content: center;
    width: 180px;
    max-width: 100%;
    gap: 10px;
    font: 800 20px Nanum Gothic, sans-serif;
    letter-spacing: 1.25px;
    padding: 5px 32px;
    border: 5px solid #595959;
    color: #595959;
    cursor: pointer;
    transition: transform 0.2s ease;
    line-height: 1.7; /* 텍스트 높이 조절 */
  }

  .start:hover {
    transform: scale(1.05);
    background-color: #bea5a920;
  }

  .edit {
    margin-top: 20px;
    border-radius: 175px;
    background: #595959;
    box-shadow: 0 4px 10px #a4abbd;
    display: flex;
    justify-content: center;
    width: 180px;
    max-width: 100%;
    gap: 10px;
    font: 800 20px Nanum Gothic, sans-serif;
    letter-spacing: 1.25px;
    padding: 5px 32px;
    color: #fff;
    cursor: pointer;
    transition: transform 0.2s ease;
    line-height: 1.7; /* 텍스트 높이 조절 */
  }

  .edit:hover {
    transform: scale(1.05);
    background-color: #59595960;
  }

  /* .start {
    background-color: #666;
    color: white;
    border: none;
    padding: 10px 40px;
    border-radius: 20px;
    cursor: pointer;
    margin-top: 10px;
  } */

  /* .edit {
    background-color: #555;
    color: white;
    border: none;
    padding: 10px 46px;
    border-radius: 20px;
    cursor: pointer;
    margin-top: 10px;
  } */

</style>