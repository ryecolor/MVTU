<template>
    <div class="floating-icon-container">
        <div class="floating-icon" @click="redirectToKino">
        <span>🎥</span>
        </div>
        <p class="icon-text">OTT 검색</p>
    </div>
  </template>
  
  <script setup>
  const redirectToKino = () => {
    window.location.href = 'https://www.kinolights.com';
  };
  </script>
  
  <style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap'); /* 나눔고딕 폰트 로드 */  

  /* 전체 아이콘 컨테이너 */
  
  .floating-icon {
      position: fixed;
      bottom: 67px;
      right: 40px;
      width: 50px;
      height: 50px;
      background-color: #ffffff;
      border: 4px solid #595959;
      color: #595959;
      font-size: 24px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      transition: transform 0.3s ease, background-color 0.3s ease;
    }
    
  .floating-icon-container {
    position: fixed;
    bottom: 32px;
    right: 42px;
    display: flex;
    flex-direction: column;
    align-items: center; /* 중앙 정렬 */
    text-align: center; /* 텍스트 정렬 */
    }
      
  .floating-icon:hover {
    transform: scale(1.2);
    background-color: #bea5a920;
  }

  .floating-icon span {
    position: relative; /* 위치 조정 가능하도록 설정 */
    top: -3px; /* 이모티콘을 위로 이동 */
    }

  /* 텍스트 스타일 */
  .icon-text {
    margin-bottom: 8px;
    font-family: 'Nanum Gothic', sans-serif; /* 나눔고딕 폰트 */
    font-weight: bold;
    font-size: 12px;
    color: #595959;
    line-height: 1.2; /* 텍스트 간격 */
    }
  </style>
  