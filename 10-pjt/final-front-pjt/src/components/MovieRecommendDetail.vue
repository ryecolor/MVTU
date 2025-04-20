<template>
  <div class="movie-info" v-if="movie">
    <div class="poster-section">
      <img class="poster" :src="movie.poster_url" alt="영화 포스터">
    </div>
    <div class="info-section">
      <div class="genre-section">
        <span class="genre-tag">{{ movie.category }}</span>
      </div>
      <h3 class="movie-title">{{ movie.title }}</h3>
      <div class="detail-set">
        <div class="detail-row">
          <span class="running-time">러닝 타임</span>
          <span class="detail-info">{{ movie.running_time }}</span>
        </div>
        <div class="detail-row">
          <span class="score">평점</span>
          <span class="detail-info">{{ movie.score }}</span>
        </div>
        <div class="detail-row">
          <span class="released">개봉 연도</span>
          <span class="detail-info">{{ movie.released }}</span>
        </div>
      </div>
    </div>
    <div class="description-section">
      <p class="movie-description">{{ movie.detail }}</p>
    </div>
  </div>
  <br>
  <div class="profile-container">
    <h2 class="title-section">등장인물</h2>
    <div class="profiles">
      <div class="profile" v-if="actress">
        <div class="circular-image">
          <img :src="actress.img" alt="actress">
        </div>
        <h3 style="font-family: 'Nanum Myeongjo'; margin: 10px 0;">{{ actress.name }}</h3>
        <div style="background-color: #EEB9C3;" class="mbti-tag mbti-actress">{{ actress.mbti }}</div>
        <div class="detail-text pink">
          {{ actress.detail }}
        </div>
      </div>
      <div class="profile" v-if="actor">
        <div class="circular-image">
          <img :src="actor.img" alt="actor">
        </div>
        <h3 style="font-family: 'Nanum Myeongjo'; margin: 10px 0;">{{ actor.name }}</h3>
        <div style="background-color: #BBCCF2;" class="mbti-tag mbti-actor">{{ actor.mbti }}</div>
        <div class="detail-text blue">
          {{ actor.detail }}
        </div>
      </div>
    </div>
  </div>
  <br>
  <div v-if="movie">
    <div class="trailer" >
      <h2 class="title-section">예고편</h2>
      <iframe
        width="400"
        height="300"
        :src="`https://www.youtube.com/embed/${youtubeid}`"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
      <br>
      <br>
      <div>
        <h4 style="font-family: 'Nanum Gothic'; color: #59595980; font-size: 14px; margin-bottom: 30px;">Q. 동영상이 재생되지 않는다면?</h4>
        <input
          class="youtube-search"
          type="text"
          placeholder="추가적인 예고편을 유튜브에 바로 검색하기" 
          :value="inputData" 
          @input="onInput"
        />
        <button class="youtube-click" @click="findMovie">SEARCH</button>
        <div v-for="youtube in youtubeList" :key="youtube.id.videoId" class="box">
          <div class="content">
              <!-- Thumbnail (좌측) -->
              <div class="thumbnail">
                  <iframe width="560" height="315" :src="'https://www.youtube.com/embed/'+ youtube.id.videoId" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>            
                  </iframe>
              </div>
              <!-- Title and Description (우측) -->
              <div class="text">
                  <h3 class="youtube-detail">{{ youtube.snippet.title }}</h3>
                  <p class="youtube-detail">{{ youtube.snippet.description }}</p>
              </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="review">
    <br>
    <br>
    <br>
    <br>
    <h1 style="font-family: 'Nanum Myeongjo';">Community</h1>
    <h4 style="font-family: 'Nanum Myeongjo'; margin-top: 10px;">추천 여부를 선택하신 후 리뷰를 작성해 보세요.</h4>
    <div class="community-bar">
      <div class="bar-container">
        <div class="like-section">
          <button @click="toggleLike" :class="{ 'liked': isLiked }">
            {{ isLiked ? '추천' : '추천' }}
          </button>
          <div class="icon-container">
            <img @click="toggleLike" src="@/assets/liked.png" alt="Liked" class="reaction-icon">
          </div>
          <div class="like-count">{{ total_likes }}</div>
        </div>
        <div class="ratio-bar">
          <div class="like-bar" 
              :style="{ 
                width: calculateLikeRatio + '%',
                backgroundColor: hasVotes ? '#ffcdd2' : 'transparent'
              }"
            ></div>
          <div class="dislike-bar"
              :style="{ width: calculateDislikeRatio + '%',
                backgroundColor: hasVotes ? '#e3f2fd' : 'transparent',
                marginLeft: 'auto'
              }"
            ></div>
        </div>
        <div class="dislike-section">
          <button @click="toggleDislike" :class="{ 'disliked': isdisLiked }">
            {{ isdisLiked ? '비추천' : '비추천' }}
          </button>
          <div class="icon-container">
            <img @click="toggleDislike" src="@/assets/disliked.png" alt="Liked" class="reaction-icon">
          </div>
          <div class="dislike-count">{{ total_dislikes }}</div>
        </div>
      </div>
      <div class="count-container">
      </div>
    </div>
    <br>
    <br>
    <div v-if="isLiked || isdisLiked">
    <form @submit.prevent="submitComment">
      <div class="input-container">
        <label for="content"></label>
        <input 
          type="text"
          id="content" 
          v-model="create_review" 
          required
          class="comment-input"
        >
        <button type="submit" class="submit-button">등록</button>
      </div>
    </form>
  </div>
    <h2 style="font-family: 'Nanum Myeongjo';">Review List</h2>  
          <!-- 유저의 mbti정보와 검색하고자 하는 mbti를 화살표로 연결하는 방식을 한번 생각해보자. -->
    <div class="reviews-container">
      <div class="reviews-columns">
        <!-- 추천 댓글 -->
        <div class="like-reviews" v-if="like_reviews.length">
          <h4 style="font-family: 'Nanum Myeongjo'; color: #59595980; margin: 10px 0px;">Recommendation</h4>
          <div v-for="like_review in like_reviews" :key="like_review.id">
            <div class="review-card like">
              <div class="review-header">
                <span class="mbti-tag">{{ like_review.user_mbti }}</span>
                <i class="arrow right"></i>
                <div>
                  <span class="mbti-tag">{{ like_review.partner_mbti }}</span>
                </div>
              </div>
              <div class="review-content">{{ like_review.content }}</div>
              <div class="review-footer">
                <span class="date">{{ like_review.created_at.substring(0, 10) }}</span>
                <div style="font-size: 15px; font-family: 'Nanum Gothic'; margin-top: 5px;" v-if="store.logInUsername === like_review.username">
                  <RouterLink @click.prevent="deleteReview(like_review.id)" to="#"
                  >삭제
                  </RouterLink>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="like-reviews">
          <br>
          <p style="font-family: 'Nanum Myeongjo'; font-size: 14px; font-weight: 600; background-color: #EEB9C320; border-radius: 10px; padding: 10px;">작성된 추천 리뷰가 없습니다.</p>
        </div>
        <!-- 비추천 댓글 -->
        <div class="dislike-reviews" v-if="dislike_reviews.length">
          <h4 style="font-family: 'Nanum Myeongjo'; color: #59595980; margin: 10px 0px;">Non-recommendation</h4>
          <div v-for="dislike_review in dislike_reviews" :key="dislike_review.id">
            <div class="review-card dislike">
              <div class="review-header">
                <span class="mbti-tag">{{ dislike_review.user_mbti }}</span>
                <i class="arrow right"></i>
                <div>
                  <span class="mbti-tag">{{ dislike_review.partner_mbti }}</span>
                </div>
              </div>
              <div class="review-content">{{ dislike_review.content }}</div>
              <div class="review-footer">
                <span class="date">{{ dislike_review.created_at.substring(0, 10) }}</span>
                <div style="font-size: 15px; font-family: 'Nanum Gothic'; margin-top: 5px;" v-if="store.logInUsername === dislike_review.username">
                  <RouterLink @click.prevent="deleteReview(dislike_review.id)" to="#"
                  >삭제
                  </RouterLink>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="dislike-reviews">
          <br>
          <p style="font-family: 'Nanum Myeongjo'; font-size: 14px; font-weight: 600; background-color: #BBCCF220; border-radius: 10px; padding: 10px;">작성된 비추천 리뷰가 없습니다.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import axios from 'axios'
  import {onMounted, ref, computed} from 'vue'
  import {useMovieStore} from "@/stores/movies"
  import {useRoute, useRouter} from 'vue-router'

  const store = useMovieStore()
  const route = useRoute()
  const router = useRouter()

  // 배우, 영화 정보
  const movie = ref(null)
  const actor = ref(null)
  const actress = ref(null)
  // 좋아요한 유저 수
  const total_likes = ref(0)
  const isLiked = ref(false)
  // 싫어요한 유저 수
  const total_dislikes = ref(0)
  const isdisLiked = ref(false)
  const youtubeid = ref('')
  // 댓글을 저장하는 변수
  const reviews = ref([])
  const like_reviews = ref([])
  const dislike_reviews = ref([])
  // 생성할 댓글을 받는 변수
  const create_review = ref('')
  // API정보를 받을 변수
  const inputData = ref('')

  const youtubeList = ref([])
  // 유튜브를 활용하여 검색한 내용을 변수에 담는 함수
  const onInput = function (event) {
    inputData.value = event.currentTarget.value
  }
  const partner_mbti = ref(route.query.selectedMbti)
  console.log(partner_mbti.value)


  // 영화를 찾는 함수
  const findMovie = function () {
    const youtubeAPI = import.meta.env.VITE_YOUTUBE_API_KEY
    const searchWord = inputData.value
    const youtubeURL = `https://www.googleapis.com/youtube/v3/search?key=${youtubeAPI}&part=snippet&type=video&q=${searchWord}`
    axios.get(youtubeURL)
        .then((response) => {
            youtubeList.value = response.data.items
        })
        .catch((error) => {
            console.log(error)
        })
  }
  // 추천 비추천 비율 computed 함수들
  const hasVotes = computed(() => {
    return total_likes.value > 0 || total_dislikes.value > 0;
  })
  const calculateLikeRatio = computed(() => {
    const total = total_likes.value + total_dislikes.value
    return total > 0 ? (total_likes.value / total) * 100 : 50
  })
  const calculateDislikeRatio = computed(() => {
    const total = total_likes.value + total_dislikes.value
    return total > 0 ? (total_dislikes.value / total) * 100 : 50
  })

  onMounted(async() => {
    try {
      const response = await axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/${route.params.id}/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
        movie.value = response.data
        isLiked.value = response.data.is_liked
        youtubeid.value = getYouTubeVideoId(response.data.trailer_url)
        console.log(movie.value)
      } catch (err) {console.log(err)};
    })

  onMounted(async() => {
    try {
      const response = await axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/${route.params.id}/likes`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
        total_likes.value = response.data.total_likes
        isLiked.value = response.data.is_liked
      } catch (err) {console.log(err)};
    })
  
  onMounted(async() => {
    try {
      const response = await axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/${route.params.id}/dislikes`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
        total_dislikes.value = response.data.total_dislikes
        isdisLiked.value = response.data.is_disliked
      } catch (err) {console.log(err)};
    })  
    
  
  const toggleLike = async () => {
    try {
      const response = await axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/movies/${route.params.id}/likes/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      if (response.status === 200) {
        isLiked.value = response.data.is_liked
        isdisLiked.value = response.data.is_disliked
        total_likes.value = response.data.total_likes
        total_dislikes.value = response.data.total_dislikes
        console.log(isLiked.value ? '추천 추가' : '추천 취소')
      }
    } catch (error) {
      console.error('좋아요 처리 중 오류 발생:', error)
    }
  }

  const toggleDislike = async () => {
    try {
      const response = await axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/movies/${route.params.id}/dislikes/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      if (response.status === 200) {
        isdisLiked.value = response.data.is_disliked
        isLiked.value = response.data.is_liked
        total_dislikes.value = response.data.total_dislikes
        total_likes.value = response.data.total_likes
        console.log(isdisLiked.value ? '비추천 추가' : '비추천 취소')
      }
    } catch (error) {
      console.error('좋아요 처리 중 오류 발생:', error);
    }
  }

  function getYouTubeVideoId(url) {
    // 여러 가지 유튜브 URL 형식을 다루기 위한 정규 표현식 배열
    const regexes = [
        /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/,
        /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/,
        /^.*youtube\.com\/shorts\/([^#\&\?]*).*/
    ];
    for (const regex of regexes) {
        const match = url.match(regex);
        if (match && match[7].length === 11) {
            return match[7];
        }
    }
    return null; // 매치되는 비디오 ID가 없을 경우 null 반환
  }

  const fetchReviews = async () => {
    try {
      like_reviews.value = []
      dislike_reviews.value = []
      reviews.value = []
      const response = await axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/${route.params.id}/reviews/`,
        headers: { Authorization: `Token ${store.token}` }
      })
      reviews.value = response.data
      // 리뷰 분류
      reviews.value.forEach(review => {
        if (review.like_review) {
          like_reviews.value.push(review)
        } else if (review.dislike_review) {
          dislike_reviews.value.push(review)
        }
      })
    } catch (error) {
      console.error('리뷰를 불러오는 중 오류가 발생했습니다:', error)
    }
  }

  // 주연배우 데이터를 가져오는 함수
  const fetchactor = async () => {
    try {
      const response = await axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/actors/${route.params.id}/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      actor.value = response.data

    } catch (error) {
      console.error('리뷰를 불러오는 중 오류가 발생했습니다:', error)
    }
  }

  const fetchactress = async () => {
    try {
      const response = await axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/actresses/${route.params.id}/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      actress.value = response.data
    } catch (error) {
      console.error('리뷰를 불러오는 중 오류가 발생했습니다:', error)
    }
  }


  onMounted(() => {
    fetchReviews()
    fetchactor()
    fetchactress()
  })
  // 댓글 생성란을 구성하고 생성을 도와주는 코드
  const submitComment = () => {
      const movieId = route.params.id
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/movies/${movieId}/create_review/`,
        data: {
          content: create_review.value,
          partner_mbti: partner_mbti.value,
          like_review: isLiked.value,
          dislike_review: isdisLiked.value,
        },
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      .then((res) => {
        console.log('댓글 생성 성공')
        create_review.value = ''
        fetchReviews()
      })
      .catch((error) => {
      console.error('댓글 제출 중 오류 발생:', error)
      })
    }

  // 댓글을 삭제하는 함수
  const deleteReview = async (reviewId) => {
  if (confirm('정말로 이 리뷰를 삭제하시겠습니까?')) {
    try {
      await axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/api/v1/movies/${route.params.id}/reviews/${reviewId}/delete_review/`,
        headers: {
          Authorization: `Token ${store.token}`
        },
        params: {
          partner_mbti: partner_mbti.value
        },  
      })
      console.log('리뷰가 성공적으로 삭제되었습니다.')
      await fetchReviews() // 리뷰 목록 새로고침
      router.replace({ query: { ...route.query, selectedMbti: partner_mbti.value } })
    } catch (error) {
      console.error('리뷰 삭제 중 오류가 발생했습니다:', error)
    }
  }
}

</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo&display=swap');

  * {
    text-align: center;
  }
  /* 영화 정보 스타일 */
  .movie-info {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    padding: 20px;
    background-color: #BEA5A940;
    border-radius: 10px;
    margin: 0 30px;
    margin-bottom: 10px;
  }

  .poster-section {
    display: flex;
    justify-content: start;
    align-items: center;
    padding: 20px;
    width: 100%;
    max-width: 200px; /* Ensure this matches the maximum width of the poster */
  }

  .poster {
    width: 100%;
    max-width: 200px; /* Set a maximum width for larger screens */
    height: auto; /* Maintain aspect ratio */
    /* border-radius: 8px; */
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }

  .info-section {
    flex: 0 0 240px;
    padding: 20px 10px;
    /* border-right: 1px solid #595959; */
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  .description-section {
    display: flex;
    justify-content: center; /* Centers content horizontally */
    align-items: center; /* Centers content vertically */
    flex: 1 1 100px;
    padding: 20px;
    max-height: 400px;
    overflow-y: auto;
    font-weight: 600;
    font-family: 'Nanum Myeongjo', serif;
  }

  .movie-title {
    margin: 20px 0 20px;
    font-size: 25px;
    font-weight: bold;
    font-family: 'Nanum Myeongjo', serif;
    color: #595959;
    display: flex;
    gap: 8px;
    text-align: start;
  }

  .genre-section {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  .genre-tag {
    padding: 5px 8px;
    background-color: #595959;
    border-radius: 5px;
    font-family: 'Nanum Gothic';
    font-weight: 300;
    font-size: 14px;
    color: #fff;
  }

  .running-time, .score, .released {
    font-size: 14px;
    color: #595959;
    text-align: left;
    font-weight: bold;
  }

  .detail-set {
    margin-top: auto; /* Pushes the detail-set to the bottom */
  }

  .detail-info {
    margin-right: 30px;
    font-weight: 700;
  }

  .detail-row {
    display: flex;
    justify-content: space-between;
    padding: 6px 0;
  }

  .detail-row span {
    font-size: 14px;
    color: #595959;
  }

  .movie-description {
    font-size: 16px;
    line-height: 1.6;
    color: #595959;
    text-align: start;
  }

  /* 등장인물 스타일 */
  .title-section {
    margin-left: 25px;
    writing-mode: vertical-lr;
    text-orientation: upright;
    position: absolute;
    left: 0px;
    top: 20px;
    font-size: 24px;
    font-family: 'Nanum Myeongjo', serif;
    letter-spacing: 8px;
    display: block;
  }

  .youtube-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
  }

  .youtube-search-box {
    display: flex;
    width: 100%;
    margin-bottom: 20px;
    padding: 15px;
    background-color: white;
    border-radius: 8px;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
  }

  .youtube-search {
    height: 40px;
    width: 400px;
    margin: 0 auto;
    margin-bottom: 40px;
    font-family: 'Nanum Gothic', serif;
    font-size: 14px;
    border-radius: 4px;
    background-color: #00000090;
    color: #fff;
  }

  .youtube-click {
    height: 40px;
    margin-left: 10px;
    padding: 10px 20px;
    background-color: #ff0000;
    color: white;
    border: none;
    border-radius: 4px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
  }

  .youtube-click:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
  }

  ::placeholder {
    color: #ffffff80;
    font-weight: 300;
  }

  .liked {
    background-color: #eeb9c3;
    color: #595959;
    font-family: 'Nanum Gothic';
    font-size: 14px;
    font-weight: bolder;
  }

  .disliked {
    background-color: #bbccf2;
    color: #595959;
    font-family: 'Nanum Gothic';
    font-size: 14px;
    font-weight: bolder;
  }

  button {
    padding: 10px 20px;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    font-family: 'Nanum Gothic';
    font-size: 14px;
    color: #595959;
    background-color: #59595920;
  }

  button:hover {
    opacity: 0.8;
  }

  /* 사진을 원형으로 자르기 */
  .circular-image {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    overflow: hidden;
  }

  .circular-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center center;
  }

  /* 등장인물 페이지 */
  .profile-container {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 20px;
    margin: 40px 0;
    display: auto;
    grid-template-columns: 300px 300px 1fr;
    gap: 30px;
    margin-bottom: 10px;
  }

  .profiles {
    margin-top: 20px;
    display: flex;
    justify-content: center;
    gap: 50px;
    width: 100%;
  }

  .profile {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 300px;
  }

  .circular-image {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    overflow: hidden;
    margin-bottom: 20px;
  }

  .circular-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .mbti-tag {
    margin: 10px 0;
    display: inline-block;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 16px;
    font-family: 'Nanum Myeongjo', serif;
    font-weight: bolder;
    color: #595959;
  }

  .mbti-actress {
    background-color: #EEB9C3;
  }

  .mbti-actor {
    background-color: #BBCCF2;
  }

  .detail-text {
    font-size: 14px;
    font-weight: 600;
    font-family: 'Nanum Myeongjo', serif;
    line-height: 180%;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
    width: fit-content; /* Adjusts width based on content */
    max-width: 100%; /* Prevents overflow beyond container */
  }

  .detail-text.pink {
    background: linear-gradient(to bottom, #eeb9c360, #eeb9c300); /* Define a pink gradient */
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
  }

  .detail-text.blue {
    background: linear-gradient(to bottom, #bbccf260, #bbccf200); /* Define a blue gradient */
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
  }

  /* 예고편 페이지 스타일 */
  .trailer {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 20px;
    padding-top: 40px;
    display: auto;
    grid-template-columns: 300px 300px 1fr;
    gap: 30px;
    padding: 20px;
    margin-top: 40px;
    margin-bottom: 10px;
  }

  /* 댓글 페이지 스타일 */
  .review{
    display: auto;
    grid-template-columns: 300px 300px 1fr;
    gap: 30px;
    padding: 20px;
    background-color: white;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.3);
    margin-bottom: 10px;
  }

  .community-bar {
    width: 100%;
    max-width: 900px;
    margin: 20px auto;
  }

  .bar-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    margin-bottom: 10px;
    margin: 0 20px;
  }

  .ratio-bar {
    flex: 1;
    height: 20px;
    background-color: #e0e0e0;
    border-radius: 10px;
    overflow: hidden;
    /* position: relative; */
    display: flex;
    margin: 0 10px;
  }

  .like-bar {
    height: 100%;
    background-color: #ff9999;
    border-radius: 0;
    transition: width 0.3s ease;
  }

  .dislike-bar {
    height: 100%;
    background-color: #e3f2fd;
    border-radius: 0;
    transition: width 0.3s ease; 
    margin-left: auto;
  }

  .count-container {
    display: flex;
    justify-content: space-between;
    padding: 0 30px;
    margin-top: 10px;
  }

  .like-count, .dislike-count {
    margin-top: 25px;
    font-family: 'Nanum Myeongjo', serif;
    font-size: 18px;
    font-weight: bold;
  }

  .like-section, .dislike-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    font-size: 24px;
  }
  
  .icon-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 30px;
    margin-top: 10px;
  }

  .reaction-icon {
    width: 48px;
    height: 48px;
    object-fit: contain;
    margin: auto 0;
  }

  /* 댓글 생성란 스타일 */
  .comment-form {
    width: 70%;
    margin: 20px auto;
  }

  .input-container {
    display: flex;
    gap: 10px;
    max-width: 750px;
    margin: 0 auto;
    margin-bottom: 40px;
  }

  .comment-input {
    flex: 1;
    height: 40px;
    padding: 0 15px;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    font-size: 14px;
    outline: none;
  }

  .submit-button {
    width: auto;
    height: 40px;
    background-color: #595959;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 12px;
  }

  .submit-button:hover {
    background-color: #555;
  }

  /* 댓글 목록을 출력하는 페이지 스타일 */
  .reviews-container {
    width: 100%;
    max-width: 930px;
    margin: 20px auto;
    /* display: grid;
    grid-auto-rows: 0fr;
    gap: 0; */
  }

  .reviews-columns {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 20px;
  }

  .like-reviews, .dislike-reviews {
    flex: 1 1 calc(50% - 10px);
    min-width: 300px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .review-card {
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 10px;
    width: 100%;
    min-height: 130px; /* 최소 높이 설정 */
    height: auto; /* 높이를 자동으로 조정 */
    display: flex;
    flex-direction: column;
  }

  @media (max-width: 768px) {
    .like-reviews, .dislike-reviews {
      flex: 1 1 100%;
    }
  }

  .review-card.like {
    background-color: #fff0f3;
    text-align: left;
  }

  .review-card.dislike {
    background-color: #f0f8ff;
    text-align: right;
  }

  .review-header {
    white-space: nowrap;
  }

  .review-header > * {
    display: inline-block;
    vertical-align: middle;
    margin-right: 10px;
  }

  .review-header > *:last-child {
    margin-right: 0;
  }

   /* 화살표아이콘 */
  .arrow {
    border: solid #595959;
    border-width: 0 2px 2px 0;
    display: inline-block;
    padding: 3px;
    margin: 10px 8px 10px 3px;
  }

  .right {
    transform: rotate(-45deg);
    -webkit-transform: rotate(-45deg);
  }

  .review-card span.mbti-tag {
    margin: 0;
  }

  .review-content {
    margin: 10px 0;
    font-size: 16px;
    line-height: 1.5;
    overflow: visible; /* 내용이 넘치면 보이도록 설정 */
    text-overflow: clip; /* 텍스트 자르기 제거 */
    display: block; /* -webkit-box 대신 block으로 변경 */
    flex-grow: 1; /* 남은 공간을 채우도록 설정 */
  }

  .review-footer {
    margin-top: 10px;
    font-family: 'Nanum Myeongjo';
    font-size: 10px;
  }

  .date {
    color: #888;
    font-size: 12px;
  }

  /* 추가 리뷰 검색 목록 나열을 위한 스타일 */

  /* 기본 입력 필드 스타일 */
  input {
      width: 50%;
      height: 30px;
      margin-bottom: 10px;
  }

  /* 각 유튜브 영상 박스를 나열하는 스타일 */
  .box {
      display: flex; /*썸네일과 텍스트를 가로로 나열*/
      align-items: flex-start; /* 세로 정렬 */
      border: 1px solid #ddd;
      padding: 10px;
      margin-bottom: 10px;
      height: auto; /* 자동 높이 조정 */
      width: 60%;
      box-sizing: border-box;
      margin-left: auto;
      margin-right: auto;
  }

  /* 썸네일 이미지 스타일 */
  .thumbnail {
      width: 160px; /* 썸네일의 고정된 너비 */
      height: 120px; /* 썸네일의 고정된 높이 */
      margin-right: 15px; /* 썸네일과 텍스트 간의 여백 */
  }

  /* 썸네일 iframe 스타일 */
  .thumbnail iframe {
      width: 100%; /* 썸네일 영역에 꽉 차도록 */
      height: 100%; /* 높이도 꽉 차도록 */
      object-fit: cover; /* 비율을 유지하며 잘리지 않도록 */
  }

  /* 텍스트 박스를 나누는 컨테이너 */
  .text-container {
      display: flex; /* 제목과 설명을 가로로 배치 */
      flex-direction: row; /* 가로로 배치 */
      justify-content: space-between; /* 여백을 고르게 분배 */
      width: calc(100% - 175px); /* 썸네일 영역을 제외한 나머지 공간 */
  }

  /* 제목과 설명 영역 */
  .text {
      display: flex;
      flex-direction: column; /* 제목과 설명을 세로로 나열 */
      justify-content: center; /* 텍스트를 세로로 가운데 정렬 */
      flex: 1; /* 남은 공간을 가득 채우도록 설정 */
      padding-left: 10px; /* 썸네일과 텍스트 간의 여백 */
  }

  /* 제목 스타일 */
  .text h3 {
      margin: 0;
      font-size: 1.1em;
      font-weight: bold;
      margin-bottom: 5px;
  }

  /* 설명 스타일 */
  .text p {
      font-size: 0.9em;
      color: #555;
      margin: 0;
  }

  .content {
      display: flex; /* 제목과 설명을 가로로 배치 */
      flex-direction: row; /* 가로로 배치 */
  }

  h4 {
    text-decoration: none;
    font-family: 'Nanum Gothic', sans-serif;
  }

  .youtube-detail {
    text-align: start;
  }
</style>