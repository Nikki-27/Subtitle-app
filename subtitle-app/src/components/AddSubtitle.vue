<template>
  <div>
    <div class="form-group">
      <label for="timestamp">Timestamp (in seconds)</label>
      <input v-model="timestamp" class="form-control" />
    </div>
    <div class="form-group">
      <label for="subtitleText">Subtitle text</label>
      <input v-model="subtitleText" class="form-control" />
    </div>
    <button @click="addSubtitle" class="btn btn-primary">Add Subtitle</button>
  </div>
</template>

<script>
export default {
  props: ['subtitles'],
  data() {
    return {
      timestamp: '',
      subtitleText: '',
    };
  },
  methods: {
    addSubtitle() {
      const newSubtitle = {
        timestamp: parseFloat(this.timestamp),
        text: this.subtitleText,
      };

      // Emit an event to send the new subtitle to the parent component
      this.$emit('new-subtitle', newSubtitle);

      // Clear input fields
      this.timestamp = '';
      this.subtitleText = '';
    },
  },
};
</script>
