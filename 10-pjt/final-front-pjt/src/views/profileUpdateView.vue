<template>
    <br>
    <div>
      <h1 class="title">프로필 편집</h1>
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
        <form @submit.prevent="submitMbti">
            <div>
              <span>USERNAME</span>
            </div>
            <div>
              <input 
              type="text"
              class="username"
              id="username" 
              name="username"
              v-model="edit_username" 
              required
            >
            </div>
          <div>
            <span>MBTI</span>
          </div> 
          <select name="mbti" id="mbti" class="custom-select" v-model="mbti">
            <option value="">Select your MBTI</option>
            <option value="ESFP">ESFP</option>
            <option value="ENFP">ENFP</option>
            <option value="ESTP">ESTP</option>
            <option value="ENTP">ENTP</option>
            <option value="ESFJ">ESFJ</option>
            <option value="ENFJ">ENFJ</option>
            <option value="ESTJ">ESTJ</option>
            <option value="ENTJ">ENTJ</option>
            <option value="ISFP">ISFP</option>
            <option value="INFP">INFP</option>
            <option value="ISTP">ISTP</option>
            <option value="INTP">INTP</option>
            <option value="ISFJ">ISFJ</option>
            <option value="INFJ">INFJ</option>
            <option value="ISTJ">ISTJ</option>
            <option value="INTJ">INTJ</option>
          </select>
        <input type="submit" value="SUBMIT" class="submit">
      </form>
    </div>
  </template>
  
  <script setup>
    import { ref, onMounted } from 'vue'
    import { useMovieStore } from '@/stores/movies'
    import axios from 'axios'
    import { useRouter } from 'vue-router';
  
    const store = useMovieStore()
    const router = useRouter()
    const mbti = ref('') // MBTI 선택 상태를 저장할 변수
    const edit_username = ref(store.logInUsername)
    const profile = ref([])
  
    const submitMbti = function () {
      if (mbti && edit_username) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/api/v1/update-userprofile/',
          data: {
            mbti: mbti.value,
            username: edit_username.value
          },
          headers: {
            Authorization: `Token ${store.token}`
          }
        })
        .then((res) => {
          console.log('성공')
          fetchprofile()
          router.push({name:"profileView"})
        })
        .catch((err) => {
          console.log('Error saving MBTI:', err)
          alert('MBTI를 선택해 주세요.')
        });
      } else {
        console.log('MBTI 값이 없습니다.');
      }
    }

    const fetchprofile = async () => {
      if (profile) {
        try {
          const response = await axios({
            method: 'get',
            url: `http://127.0.0.1:8000/api/v1/get-profile/`,
            headers: {
              Authorization: `Token ${store.token}`
            }
          })
          profile.value = response.data
          edit_username.value = response.data.username
        } catch (error) {
          console.error('프로필를 불러오는 중 오류가 발생했습니다:', error)
        }
      }
    } 
    
    if (profile) {
      onMounted(() => {
        fetchprofile()
      })
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

  img {
    margin-bottom: 20px;
  }

  .profile {
    height: 150px;
    width: 150px;
    border: 2px solid white;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  .edit-area {
    margin-bottom: 20px;
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

  form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    /* margin-top: 10px; */
  }

  #mbti {
    color: #595959;
    font-weight: 600;
    margin-bottom: 20px;
  }

  #username {
    padding: 8px 15px;
    border: 3px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
    font-family: 'Nanum Gothic', serif;
    font-weight: 600;
    width: 200px;
    color: #595959;
    margin-bottom: 20px;
  }

  select {
    padding: 8px 15px;
    border: 3px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
    font-family: 'Nanum Gothic', serif;
    font-weight: 500;
    width: 200px;
  }

  .submit {
    margin-top: 40px;
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
    border: none;
    outline: none;
  }

  .submit:focus {
    outline: none;
    box-shadow: none;
  }

  .submit:hover {
    transform: scale(1.05);
    background-color: #59595960;
  }
</style>