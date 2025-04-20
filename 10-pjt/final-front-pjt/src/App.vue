<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useMovieStore } from '@/stores/movies'
import { onMounted, ref, watch } from 'vue'
import axios from 'axios'
import FloatingIcon from '@/components/FloatingIcon.vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const store = useMovieStore()
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
    console.error('프로필을 불러오는 중 오류가 발생했습니다:', error)
  }
}

// watch를 사용하여 store.logInUsername의 변경을 감지
watch(() => store.logInUsername, (newProfile) => {
  if (store.isLogin && newProfile) {
    fetchprofile()
  }
})

// 컴포넌트 마운트 시에도 프로필 정보 가져오기
onMounted(() => {
  if (store.isLogin) {
    fetchprofile()
  }
})

const audioPlayer = ref(null)
const isPlaying = ref(false)

const toggleMusic = () => {
  if (audioPlayer.value.paused) {
    audioPlayer.value.play()
    isPlaying.value = true
  } else {
    audioPlayer.value.pause()
    isPlaying.value = false
  }
}

// 배경 애니메이션을 위한 함수 추가
const startBackgroundAnimation = () => {
  const appContainer = document.querySelector('.app-container')
  appContainer.classList.add('animated-gradient')
}

// 컴포넌트가 마운트될 때 배경 애니메이션 시작
onMounted(() => {
  startBackgroundAnimation()
})
</script>

<template>
  
  <div class="app-container">    
    <header>
      <div class="wrapper">
        <nav class="nav-bar">
          <span class="left-nav">
            <RouterLink to="/">
              <img
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/de1b7242c5692312c3aac45e30bb35be4fca5fe191877e6dab001310d0c41137?placeholderIfAbsent=true&apiKey=9ffa259158414706823a4dc2f566041f"
                class="logo"
                alt="Company Logo"
                height="35rem"
                />
              </RouterLink>
          </span>
          <span class="right-nav">
            <template v-if="!store.isLogin">
              <RouterLink
              :to="{ name: 'LogInView' }">
                <h4 style="font-family: 'Nanum Myeongjo';">
                  LOGIN
                </h4>
              </RouterLink> 
            </template>
            <template v-if="store.isLogin">
              <span>
                <RouterLink :to="{ name: 'profileView' }">
                  <h4 style="font-family: 'Nanum Myeongjo';">
                    PROFILE
                  </h4>
                </RouterLink>
              </span>
              <span>
                <RouterLink @click="store.logout" to="#">
                  <h4 style="font-family: 'Nanum Myeongjo';">
                    LOGOUT
                  </h4>
                </RouterLink>
              </span>
          </template>
          </span>
        </nav>
      </div>
    </header>
    <!-- 음악 플레이어 추가 -->
    <div class="music-player">
      <div class="music-info">
        <span>🎵</span>
        <span class="music-progress" style="text-align: center;">0:00 ━━━━🌙───────── 4:00</span>
        <button @click="toggleMusic" class="music-toggle-btn">
          {{ isPlaying ? '❚❚' : '▶' }}
        </button>
      </div>
    </div>
    <!-- 배경 음악 추가 -->
    <audio ref="audioPlayer" loop>
      <source src="@/assets/InvisibleLace.mp3" type="audio/mpeg">
    </audio>
    <h3 style="margin-top: 80px;" class="selection-title" v-if="store.isLogin && route.name === 'home'"> 안녕하세요, <RouterLink :to="{ name: 'profileView' }">{{ profile.username }}</RouterLink>님!</h3>
    <h4 class="selection-title" v-else></h4>
  <RouterView />
  </div>
  <FloatingIcon />
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo&display=swap');
@import url('https://cdn.jsdelivr.net/gh/fonts-archive/NanumGothic/NanumGothic.css');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, .app-container {
  width: 100%;
  height: 100%;
  overflow-x: hidden;
}

.app-container {
  display: flex;
  flex-direction: column;
  background: linear-gradient(0deg, #bbccf240, #eeb9c340);
  background-attachment: fixed;
  font-family: 'Nanum Myeongjo', serif;
  color: #595959;
  min-height: 100vh;
  z-index: -1;
}

.nav-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 30px 35px;
  width: 100%;
}

.selection-title {
  color: #595959;
  text-align: center;
  margin: 40px 0 40px;
  font: 700 20px 'Nanum Myeongjo', sans-serif;
}

span a,
span h4 {
  text-decoration: none;
  color: #595959;
  font-family: 'Nanum Gothic', sans-serif;
  font-weight: bold;
}

.app-container a {
  text-decoration: none;
}

.animated-gradient {
  background: linear-gradient(90deg, #bbccf265, #eeb9c310, #bbccf280);
  background-size: 200% 200%;
  animation: gradient-animation 15s ease infinite;
}

@keyframes gradient-animation {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.music-player-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin: 20px 0;
}

.music-player {
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 10px 20px;
  border-radius: 50px;
  width: 100%;
  max-width: 500px;
  margin: 20px auto;
  font-weight: 600;
}

.music-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  gap: 10px;
  font-family: 'Nanum Gothic', sans-serif;
}

.music-progress {
  flex-grow: 1;
  text-align: center;
  font-weight: 800; /* 중앙 텍스트 굵게 설정 */
}

.music-toggle-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.5em;
  color: #595959;
  font-family: 'Nanum Gothic', sans-serif;
  transition: all 0.3s ease;
}

.music-toggle-btn:hover {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  transform: scale(1.3);
}

/* 우측 하단 아이콘 설명 텍스트 스타일 초기화 */
.app-container :deep(.floating-icon-text) {
  font-weight: initial;
}

.right-nav {
  display: flex;
  text-align: center;
  gap: 30px;
}
</style>
