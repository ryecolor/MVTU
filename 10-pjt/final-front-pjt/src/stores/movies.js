import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useMovieStore = defineStore('movie', () => {
  //영화정보를 담을 변수
  const movies = ref([])
  //남자배우를 담을 변수
  const actors = ref([])
  //여자배우를 담을 변수
  const actresses = ref([])
  //인증된 사용자임을 확인하는 토큰을 담는 변수
  const token = ref(null)
  const router = useRouter()
  const selected1 = ref(false)
  const selectedgender = ref('')
  

  // 로그인한 유저 아이디
  const logInUsername = ref(null)
  const profile = ref([])

  // 로그인을 실패했을 때 메시지를 출력할 변수
  const errorMessage = ref('')
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const getMovies = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/movies/',
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      movies.value = res.data
      return movies.value
    })
  }

  const getActors = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/actors/',
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      actors.value = res.data
      return actors.value
    })
  }

  const getActresses = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/actresses/',
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      actresses.value = res.data
      return actresses.value
    })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        const password = password1
        logIn({ username, password })
        console.log('회원가입 완료')
        router.push({ name: 'profileUpdateView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }
  // 프로필 닉네임 조회 함수
  const fetchprofile = async () => {
    try {
      const response = await axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/get-profile/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      profile.value = response.data
      logInUsername.value = response.data.username
      console.log(profile.value)
    } catch (error) {
      console.error('오류가 발생했습니다:', error)
    }
  } 

 // 로그인 요청 액션
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        logInUsername.value = username // 로그인된 사용자 이름 저장
        errorMessage.value = '' // 에러 메시지 제거
      })
      .catch((err) => {
        if (err.response && err.response.status === 400) {
          window.alert('아이디와 비밀번호를 확인하세요.')
        } else {
          window.alert('로그인 중 오류가 발생했습니다.')
        }
      })     
  }

  const logout = function () {
    if (confirm('로그아웃하시겠습니까?')) {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/logout/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
        .then(() => {
          // 로그아웃 성공 시 처리
          token.value = null // 토큰 제거
          logInUsername.value = null // 로그아웃 시 사용자 이름 초기화
          profile.value = []
          console.log('로그아웃 성공')
          router.push({ name: 'home' }) // 로그인 페이지로 리다이렉트
        })
        .catch((err) => {
          console.log(err)
          // 로그아웃 실패 시에도 로컬 상태는 정리
          token.value = null
          profile.value = []
          localStorage.removeItem('token')
          router.push({ name: 'home' }) // 로그인 페이지로 리다이렉트
        })
      }
    }
  return { movies, actors, actresses, selectedgender, fetchprofile, getMovies, getActors, getActresses, signUp, logIn, logout, token, isLogin, logInUsername, errorMessage, selected1}
}, {persist: true})
