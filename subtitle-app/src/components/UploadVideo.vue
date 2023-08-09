<template>
  <div>
    <input type="file" @change="handleFileUpload" />
    <video ref="videoPlayer" controls @timeupdate="updateSubtitle">
      <source :src="videoSrc" type="video/mp4" />
    </video>
    <div class="subtitles">
      <p v-for="subtitle in subtitles" :key="subtitle.timestamp">
        {{ subtitle.text }}
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      videoSrc: null,
      subtitles: [],
      subtitleText: '',
      timestamp: '',
      videoPlayer: null,
    };
  },
  mounted() {
    this.videoPlayer = this.$refs.videoPlayer;
  },
/*   methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      this.videoSrc = URL.createObjectURL(file);
    }, */
    methods: {
    async handleFileUpload(event) {
      const file = event.target.files[0];
      const formData = new FormData();
      formData.append('video_file', file);

      try {
        const response = await axios.post('api/uploads/', formData);
        console.log('Video uploaded successfully:', response.data);
        // Handle successful upload
      } catch (error) {
        console.error('Error uploading video:', error);
        // Handle upload error
      }
    },
    updateSubtitle(event) {
      const currentTime = event.target.currentTime;
      const subtitle = this.subtitles.find(
        (subtitle) => subtitle.timestamp <= currentTime
      );
      if (subtitle) {
        this.subtitleText = subtitle.text;
      }
    },
  },
};
</script>

<style scoped>
/* Add Bootstrap classes for styling */
.video-player {
  margin-bottom: 20px;
}

.subtitles {
  margin-top: 20px;
}
</style>
