<template>
  <div id="app" class="container">
    <upload-video :subtitles="subtitles" />
    <add-subtitle :subtitles="subtitles" />
    <video-player :video-src="videoSrc" :subtitles="subtitles" />
  </div>
</template>

<script>
import UploadVideo from './components/UploadVideo.vue';
import AddSubtitle from './components/AddSubtitle.vue';
import VideoPlayer from './components/VideoPlayer.vue';

export default {
  components: {
    UploadVideo,
    AddSubtitle,
    VideoPlayer,
  },
  methods: {
    handleNewSubtitle(newSubtitle) {
      this.subtitles.push(newSubtitle);
    }},
  
  data() {
    return {
      videoSrc: null,
      subtitles: [],
    };
  },
};
</script>

<style>
/* Add Bootstrap styles globally */
@import '~bootstrap/dist/css/bootstrap.css';
</style>
