<template>
  <div class="login-container">
    <h1 class="title">로그인 페이지</h1>
    <form @submit.prevent="logIn">
      <div class="form-group">
        <label for="username">ID</label>
        <input type="text" id="username" v-model.trim="username" placeholder="Enter your username">
      </div>
        <br>
      <div class="form-group">
        <label for="password">PASSWORD</label>
        <input type="password" id="password" v-model.trim="password" placeholder="Enter your password"><br>
      </div>
  
        <input type="submit" value="LOGIN" class="submit">
    </form>
    <p class="warning-text">계정이 없으신가요? <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink></p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movies'
import { useRouter } from 'vue-router'

const username = ref(null)
const password = ref(null)
const router = useRouter()
const store = useMovieStore()


const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
  router.push({ name: 'home' })
}
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

  p {
    margin-top: 40px;
  }

  label {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 5px;
    font-family: Nanum Myeongjo, sans-serif;
    font-weight: 600;
  }

  input {
    padding: 10px 3px;
    border: 3px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
    font-family: 'Nanum Gothic', serif;
    font-weight: 600;
    width: 100%;
    height: auto;
    color: #595959;
    margin-top: 5px;
    margin-bottom: 20px;
  }

  ::placeholder {
    font-family: Nanum Myeongjo, sans-serif;
    font-weight: 600;
    color: #59595940;
  }

  .login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }

  form {
    margin-top: 40px;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 300px;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    margin-bottom: 15px;
  }

  input[type="text"],
  input[type="password"] {
    padding: 10px 20px 10px;
    font-family: Nanum Gothic, sans-serif;
    font-weight: 600;
    color: #595959;
  }

  input[type="submit"] {
    margin-top: 20px;
    cursor: pointer;
  }

  .submit {
    margin-top: 20px;
    border-radius: 175px;
    background: #fff;
    box-shadow: 0 4px 10px #a4abbd;
    display: flex;
    justify-content: center;
    width: 180px;
    max-width: 60%;
    gap: 10px;
    font: 800 22px Nanum Gothic, sans-serif;
    letter-spacing: 1.25px;
    padding: 5px 32px;
    border: 5px solid #595959;
    color: #595959;
    cursor: pointer;
    transition: transform 0.2s ease;
    line-height: 1.7; /* 텍스트 높이 조절 */
  }

  .submit:hover {
    transform: scale(1.05);
    background-color: #bea5a920;
  }

  h4,
  .warning-text {
    margin-top: 40px;
    font: 600 14px Nanum Gothic, sans-serif;
  }
</style>
