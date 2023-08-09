<template>
    <div>
      <video ref="videoPlayer" controls @timeupdate="updateSubtitle">
        <source :src="videoSrc" type="video/mp4" />
      </video>
      <div class="subtitles">
        <p>{{ currentSubtitle }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['videoSrc', 'subtitles'],
    data() {
      return {
        currentTime: 0,
        currentSubtitle: '',
      };
    },
    methods: {
      updateSubtitle(event) {
        this.currentTime = event.target.currentTime;
        const subtitle = this.subtitles.find(
          (subtitle) => subtitle.timestamp <= this.currentTime
        );
        if (subtitle) {
          this.currentSubtitle = subtitle.text;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .subtitles {
    margin-top: 20px;
  }
  </style>
  