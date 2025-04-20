<template>    
  <h4 style="margin-bottom: 30px;">상대방의 성별을 선택해 주세요.</h4>
    <h2 style="margin-bottom: 30px;">1. 성별</h2>
      <form @submit.prevent="selectGender">
        <div style="margin-bottom: 30px;" class="gender-selection">
          <input type="radio" id="man" v-model="selectedGender" value="남성" />
          <label for="man" class="gender-label man-label" :class="{ selected: selectedGender === '남성' }"></label>

          <input type="radio" id="woman" v-model="selectedGender" value="여성" />
          <label for="woman" class="gender-label woman-label" :class="{ selected: selectedGender === '여성' }"></label>
        </div>
      <!-- 선택완료 버튼을 button으로 변경 -->
       <div class="submit-container">
         <button type="submit" class="submit-button">
           <span class="submit-text">
             SELECT
           </span>
         </button>
       </div>
    </form>
  <div>
    <div v-show="isGenderSelected">
      <h4 style="margin-top: 80px; margin-bottom: 30px;">그 사람의 MBTI는 무엇인가요?</h4>
      <h2 style="margin-bottom: 30px;">2. MBTI</h2>
      <form @submit.prevent="filterMovies">
        <div class="mbti-container" :class="mbtiContainerClass">
          <div class="mbti-group">
            <div class="mbti-option">
              <input type="radio" id="E" v-model="selectedMbti.ie" value="E">
              <div class="mbti-label-container">
                <span class="mbti-text top">
                  E
                </span>
                <label class="mbti-label e-label" for="E" :class="{ selected: selectedMbti.ie === 'E' }">
                </label>
              </div>
            </div>
            <div class="mbti-option">
              <input type="radio" id="I" v-model="selectedMbti.ie" value="I">
              <div class="mbti-label-container">                
                <span class="mbti-text bottom">
                  I
                </span>
                <label class="mbti-label i-label" for="I" :class="{ selected: selectedMbti.ie === 'I' }">
                </label>
              </div>
            </div>
          </div>
          <div class="mbti-group">
            <div class="mbti-option">
              <input type="radio" id="S" v-model="selectedMbti.sn" value="S">
              <div class="mbti-label-container">                
                <span class="mbti-text top">
                  S
                </span>
                <label class="mbti-label s-label" for="S" :class="{ selected: selectedMbti.sn === 'S' }">
                </label>
              </div>
            </div>
            <div class="mbti-option">
              <input type="radio" id="N" v-model="selectedMbti.sn" value="N">
              <div class="mbti-label-container">                
                <span class="mbti-text bottom">
                  N
                </span>
                <label class="mbti-label n-label" for="N" :class="{ selected: selectedMbti.sn === 'N' }">
                </label>
              </div>
            </div>
          </div>
          <div class="mbti-group">
            <div class="mbti-option">
              <input type="radio" id="T" v-model="selectedMbti.ft" value="T">
              <div class="mbti-label-container">                
                <span class="mbti-text top">
                  T
                </span>
                <label class="mbti-label t-label" for="T" :class="{ selected: selectedMbti.ft === 'T' }">
                </label>
              </div>
            </div>
            <div class="mbti-option">
              <input type="radio" id="F" v-model="selectedMbti.ft" value="F">
              <div class="mbti-label-container">                
                <span class="mbti-text bottom">
                  F
                </span>
                <label class="mbti-label f-label" for="F" :class="{ selected: selectedMbti.ft === 'F' }">
                </label>
              </div>
            </div>
          </div>
          <div class="mbti-group">
            <div class="mbti-option">
              <input type="radio" id="J" v-model="selectedMbti.pj" value="J">
              <div class="mbti-label-container">                
                <span class="mbti-text top">
                  J
                </span>
                <label class="mbti-label j-label" for="J" :class="{ selected: selectedMbti.pj === 'J' }">
                </label>
              </div>
            </div>
            <div class="mbti-option">
              <input type="radio" id="P" v-model="selectedMbti.pj" value="P">
              <div class="mbti-label-container">                
                <span class="mbti-text bottom">
                  P
                </span>
                <label class="mbti-label p-label" for="P" :class="{ selected: selectedMbti.pj === 'P' }">
                </label>
              </div>
            </div>
          </div>
        </div>
        <h4 style="font-family: 'Nanum Gothic'; font-size: 12px; margin-top: 30px;">SEARCH 버튼을 누르고 하단의 검색 결과를 확인하세요.</h4>
        <!-- SEARCH button -->
       <div class="submit-container button-container">
         <button type="submit" class="submit-button last-button">
            <span class="submit-text" id="mbtibutton" type="submit">
              SEARCH
            </span>
            <!-- <img class="search-icon" src="https://cdn.builder.io/api/v1/image/assets/TEMP/a0d998b767f4973d5b6edd65af22f2faf7a3349363264e6fb41ae1c4944aad2f?placeholderIfAbsent=true&apiKey=9ffa259158414706823a4dc2f566041f" alt="" /> -->
         </button>
       </div>
      </form>
    </div>
  </div>
  <div v-if="isDataLoaded">
    <div v-for="movie in filtered" :key="movie.id" :movie="movie"> 
      <RouterLink :to="{
        name: 'MovieRecommendDetail',
        params: {id: movie.id},
        query: { selectedMbti: mbtiString },
        state: {movie: movie}
      }">
        <img class="img" :src="movie.poster_url" alt="no img">
      </RouterLink>
      <span id="title"><{{ movie.title }}></span>
    </div>
  </div>
</template>



<script setup>
  import { ref, computed } from 'vue'
  import { useMovieStore } from '@/stores/movies'
  import { RouterLink, RouterView } from 'vue-router'

  const store = useMovieStore()
  const mbtiString = ref('')
  const selectedGender = ref('')
  const selectedMbti = ref({
    ie: '',
    sn: '',
    ft: '',
    pj: ''
  })

  const mbtiGroups = [
    ['E', 'I'],
    ['S', 'N'],
    ['T', 'F'],
    ['J', 'P']
  ]

  const mbtiContainerClass = computed(() => {
    return selectedGender.value === '남성' ? 'man-mbti' : 'woman-mbti'
  })

  const isDataLoaded = ref(false)
  const isGenderSelected = ref(false)
  const matchingActorIds = ref([])
  const filtered = ref([])

  const selectGender = () => {
    if (selectedGender.value) {
      isGenderSelected.value = true
      console.log('선택된 성별:', selectedGender.value)
    } else {
      alert('성별을 선택해 주세요.')
    }
  }

  const filterMovies = function () {
    // MBTI가 모두 선택되었는지 확인
    const isMbtiComplete = Object.values(selectedMbti.value).every(value => value !== '')

    if (!isMbtiComplete) {
      alert('MBTI를 모두 선택해 주세요.')
      return
    }

    isDataLoaded.value = false

    return new Promise((resolve, reject) => {
      Promise.all([store.getMovies(), store.getActors(), store.getActresses()])
      .then(() => {
        mbtiString.value = Object.values(selectedMbti.value).join('')
          const relevantActors = (selectedGender.value === '남성' ? store.actors : store.actresses)
          return getMatchingActorIds(relevantActors, mbtiString.value)
        })
        .then((ids) => {
          matchingActorIds.value = new Set(ids)
          filtered.value = store.movies.filter(movie => matchingActorIds.value.has(movie.id))
          
          resolve({
            filtered_movies: filtered,
            is_data_loaded: true,
            matching_actor_ids: Array.from(matchingActorIds.value)
          })
        })
        .catch((error) => {
          console.error('Error in filterMovies:', error)
          reject(error)
        })
        .finally(() => {
          isDataLoaded.value = true
        })
    })
  }

  const getMatchingActorIds = (actors, mbtiString) => {
    return new Promise((resolve) => {
      if (actors && Array.isArray(actors)) {
        const matchingIds = actors
          .filter(actor => actor.mbti === mbtiString)
          .map(actor => actor.id)
        resolve(matchingIds)
      } else {
        resolve([])
      }
    })
  }

  
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo&display=swap');

  * {
    text-align: center;
  }

  img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    height: auto;
    width: 200px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }

  .img:hover {
    transform: scale(1.05) translateY(-5px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
  }

  .img:active {
    transform: scale(1.02) translateY(-2px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
  }

  #title {
    margin-top: 25px;
    margin-bottom: 80px;
    font-weight: bold;
    font-size: larger;
    text-align: center;
    display: block;
  }

  .mbti-container {
    display: flex;
    justify-content: space-around;
    width: 100%;
    max-width: 300px;
    margin: 0 auto;
  }

  .mbti-group {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 10px;
  }

  .mbti-option {
    display: inline-block;
  }

  .mbti-option input[type="radio"] {
    margin-right: 5px;
  }

  .mbti-option label {
    cursor: pointer;
  }

  .gender-selection {
    display: flex;
    flex-direction: row; /* 수직 정렬 */
    align-items: center; /* 이미지 아래에 라벨이 오도록 */
    justify-content: center; /* 수평 중앙 정렬 */
    gap: 20px; /* 이미지 간의 간격 */
  }

  .gender-label {
    display: block;
    width: 145px;
    height: 200px;
    background-size: cover;
    background-repeat: no-repeat;
    transition: transform 0.2s ease; /* Smooth transition */
  }

  .gender-label:active {
      transform: scale(0.95); /* Scale down on click */
  }

  /* 라디오 버튼 숨기기 */
  input[type="radio"] {
    display: none; /* 라디오 버튼 숨기기 */
  }

  .man-label {
    background-image: url('@/assets/male.png'); /* 남성 이미지 경로 */
  }

  .woman-label {
    background-image: url('@/assets/female.png'); /* 여성 이미지 경로 */
  }

  /* 선택된 상태에서 이미지 변경 */
  .selected.man-label {
    background-image: url('@/assets/male-selected.png'); /* 남성 선택 시 이미지 경로 */
  }

  .selected.woman-label {
    background-image: url('@/assets/female-selected.png'); /* 여성 선택 시 이미지 경로 */
  }

  .submit-container {
    width: 100%;
    display: flex;
    justify-content: center;
  }

  .submit-button {
    border-radius: 175px;
    background: #fff;
    box-shadow: 0 4px 10px #a4abbd;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    width: 210px;
    max-width: 100%;
    gap: 11px;
    font: 800 25px NanumMyeongjo, sans-serif;
    letter-spacing: 1.25px;
    padding: 10px 32px;
    border: 5px solid #595959;
    cursor: pointer;
    transition: transform 0.2s ease;
    margin-top: 30px;
  }

  .submit-button:hover {
    transform: scale(1.05);
    background-color: #bea5a920;
  }

  /* 텍스트와 이미지에 개별 스타일 적용 */
  .submit-text {
    color: #595959;
    margin: 0;
    line-height: 1.3; /* 텍스트 높이 조절 */
    text-decoration: none;
  }

  /* search버튼 스타일 적용 */
  .button-container {
    display: flex;
    justify-content: center;
    margin-top: 20px; 
  }

  #mbtibutton {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .mbti-label-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100px; /* 적절한 높이 설정 */
  }

  .mbti-label {
    width: 30px; /* Adjust width as needed */
    height: 30px; /* Adjust height as needed */
    background-size: cover;
    background-repeat: no-repeat;
    transition: transform 0.2s ease; /* Smooth transition */
  }

  .mbti-label:active {
      transform: scale(0.95); /* Scale down on click */
  }

  /* 기본 MBTI 이미지 (성별 선택 전) */
  .e-label { background-image: url('@/assets/mbti.png'); }
  .i-label { background-image: url('@/assets/mbti.png'); }
  .s-label { background-image: url('@/assets/mbti.png'); }
  .n-label { background-image: url('@/assets/mbti.png'); }
  .t-label { background-image: url('@/assets/mbti.png'); }
  .f-label { background-image: url('@/assets/mbti.png'); }
  .j-label { background-image: url('@/assets/mbti.png'); }
  .p-label { background-image: url('@/assets/mbti.png'); }

  /* 남성 선택 상태 이미지 */
  .man-mbti .selected.e-label { background-image: url('@/assets/male-mbti-selected.png'); }
  .man-mbti .selected.i-label { background-image: url('@/assets/male-mbti-selected.png'); }
  .man-mbti .selected.s-label { background-image: url('@/assets/male-mbti-selected.png'); }
  .man-mbti .selected.n-label { background-image: url('@/assets/male-mbti-selected.png'); }
  .man-mbti .selected.t-label { background-image: url('@/assets/male-mbti-selected.png'); }
  .man-mbti .selected.f-label { background-image: url('@/assets/male-mbti-selected.png'); }
  .man-mbti .selected.j-label { background-image: url('@/assets/male-mbti-selected.png'); }
  .man-mbti .selected.p-label { background-image: url('@/assets/male-mbti-selected.png'); }

  /* 여성 선택 상태 이미지 */
  .woman-mbti .selected.e-label { background-image: url('@/assets/female-mbti-selected.png'); }
  .woman-mbti .selected.i-label { background-image: url('@/assets/female-mbti-selected.png'); }
  .woman-mbti .selected.s-label { background-image: url('@/assets/female-mbti-selected.png'); }
  .woman-mbti .selected.n-label { background-image: url('@/assets/female-mbti-selected.png'); }
  .woman-mbti .selected.t-label { background-image: url('@/assets/female-mbti-selected.png'); }
  .woman-mbti .selected.f-label { background-image: url('@/assets/female-mbti-selected.png'); }
  .woman-mbti .selected.j-label { background-image: url('@/assets/female-mbti-selected.png'); }
  .woman-mbti .selected.p-label { background-image: url('@/assets/female-mbti-selected.png'); }

  .mbti-text {
    font-family: 'Nanum Myeongjo', serif;
    font-weight: 600;
    font-size: 1.3em; /* h3 정도의 크기 */
    text-align: center;
  }

  .mbti-text.top {
    margin-top: -10px;
    margin-bottom: 10px; /* 이미지 위에 위치 */
  }

  .mbti-text.bottom {
    margin-bottom: 10px; /* 이미지 아래에 위치 */
  }

  /* 선택된 MBTI 텍스트 스타일 */
  .man-mbti .mbti-option input[type="radio"]:checked + .mbti-label-container .mbti-text {
    font-weight: bolder;
    color: #6E92E2; /* 남성 선택 시 텍스트 색상 */
  }

  .woman-mbti .mbti-option input[type="radio"]:checked + .mbti-label-container .mbti-text {
    font-weight: bolder;
    color: #F9869B; /* 여성 선택 시 텍스트 색상 */
  }

  .search-icon {
    width: 28px; /* 아이콘 크기 조절 */
    height: auto;
    background-color: transparent;
  }

  .last-button {
    margin-bottom: 80px;
  }
</style>