<template>
  <main class="login-page">
    <section class="login-container">
      <article class="login-content">
        <RouterLink to="/">
          <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/be70de7ee2350064394fceb481421cfd2c89024437eb917f2bd503e30bc017c3?placeholderIfAbsent=true&apiKey=9ffa259158414706823a4dc2f566041f"
            class="hero-image"
            alt="Movie character illustration"
            height="200rem"
          />
        </RouterLink>
        <div class="text-content">
          <h4 class="fade-in-text" style="margin-bottom: 10px;">내가 알고 싶은 그 사람을</h4>
          <h4 class="fade-in-text">영화 속 인물을 통해 들여다보세요.</h4>
        </div>
        <div class="button-container">
          <button @click="handleLoginClick" @mouseenter="handleHover" @mouseleave="handleMouseLeave" class="login-button">
            <span class="login-text">START</span>
            <img
              loading="lazy"
              src="https://cdn.builder.io/api/v1/image/assets/TEMP/bcb91c1f964283735eef890d5503977f224984631048e0ce24c8de0fbb223fa8?placeholderIfAbsent=true&apiKey=9ffa259158414706823a4dc2f566041f"
              class="login-icon"
              alt=""
            />
          </button>
        </div>
      </article>
    </section>
    <div v-for="n in 10" :key="n" class="cherry-blossom"></div>
  </main>
</template>

<script setup>
  import { onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import { useMovieStore } from '@/stores/movies'
  // import { useSound } from '@vueuse/sound'

  const router = useRouter()
  const store = useMovieStore()

  // const hoverSound = '@/assets/lightBellSound.mp3'
  // const { play, stop } = useSound(hoverSound)

  const handleLoginClick = () => {
    router.push({ name: 'MovieRecommend' })
  }

  onMounted(() => {
    const blossoms = document.querySelectorAll('.cherry-blossom')
    blossoms.forEach(blossom => {
      blossom.style.left = `${Math.random() * 100}vw`
      blossom.style.top = `${Math.random() * 100}vh`
      blossom.style.animationDelay = `${Math.random() * 10}s`
    })
  })
</script>

  <style scoped>
  * {
    text-align: center;
  }

  .login-page {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .login-container {
    width: 100%;
    max-width: 600px;
  }

  .login-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2rem;
  }

  .hero-image {
    margin-top: 30px;
    max-width: 100%;
    animation: floating 3s ease-in-out infinite;
  }

  .text-content {
    margin-top: 2rem;
    margin-bottom: 2rem;
  }

  .button-container {
    width: 100%;
    display: flex;
    justify-content: center;
  }

  .login-button {
    border-radius: 175px;
    background: #fff;
    box-shadow: 0 4px 10px #a4abbd;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    width: 210px;
    max-width: 100%;
    gap: 10px;
    font: 800 25px NanumMyeongjo, sans-serif;
    letter-spacing: 1.25px;
    padding: 5px 32px;
    border: 5px solid #595959;
    cursor: pointer;
    transition: transform 0.2s ease;
  }

  .login-button:hover {
    transform: scale(1.05);
    background-color: #bea5a920;
  }

  /* 텍스트와 이미지에 개별 스타일 적용 */
  .login-text {
    color: #595959;
    margin: 0;
    line-height: 1.7; /* 텍스트 높이 조절 */
    text-decoration: none;
  }

  .login-icon {
    width: 36px; /* 아이콘 크기 조절 */
    height: auto;
    margin-top: 4px;
  }

  /* RouterLink 기본 스타일 초기화 */
  .button-container a {
    text-decoration: none; /* 링크 밑줄 제거 */
  }

  .fade-in-text {
    opacity: 0;
    animation: fadeIn-text 2s ease-in-out forwards;
  }

  @keyframes fadeIn-text {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }

  @keyframes fadeIn {
    0% {
      opacity: 0;
    }
    90% {
      opacity: 0.4;
    }
  }

  @keyframes floating {
    0% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-10px);
    }
    90% {
      transform: translateY(0);
    }
  }

  .cherry-blossom {
    position: absolute;
    width: 40px;
    height: 42px;
    background-image: url('@/assets/cherry-blossom.png');
    background-size: cover;
    pointer-events: none;
    animation: fall 10s linear infinite 2s, sway 4s ease-in-out infinite alternate 2s, fade 10s ease-in-out infinite 2s;
    z-index: -1; /* 화면 맨 뒤로 보냄 */
    opacity: 0; /* 초기 투명도를 0으로 설정 */
  }

  @keyframes fall {
    0% {
      top: -10%;
      opacity: 0;
    }
    10% {
      opacity: 0.4;
    }
    50% {
      opacity: 0.4;
    }
    80% {
      top: 80%;
      opacity: 0;
    }
  }

  @keyframes sway {
    0% {
      transform: translateX(0) rotate(0deg);
    }
    80% {
      transform: translateX(100px) rotate(360deg);
    }
  }

  @keyframes fade {
    0%, 80% {
      opacity: 0;
    }
    50% {
      opacity: 0.4;
    }
  }
</style>