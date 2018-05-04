<template>
  <div class="modal-window" @click="hidePreview">
    <div class="modal-container">
      <embed
        v-if="selectedFile.data.split('.').pop() === 'pdf'"
        class="modal-object"
        :src="selectedFile.data">
      <img
        v-else
        class="modal-image"
        :src="selectedFile.data">
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  computed: mapState([
    'selectedFile',
  ]),
  methods: {
    ...mapMutations([
      'togglePreviewModal',
    ]),
    hidePreview(e) {
      if(e.target.className === 'modal-window') {
        this.togglePreviewModal({ isPreviewOn: false });
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.modal-window {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-position: center center;
  background-repeat: no-repeat;
  background-color: rgba(0,0,0,0.85);
  z-index: 100;
}

.modal-container {
  margin: 0 auto;
  width: 1000px;
  height: 100%;
  overflow: auto;
  background-color: #fff;
}

.modal-object,
.modal-image {
  display: block;
  width: 100%;
  height: 100%;
  background-position: center center;
  background-size: contain;
  background-repeat: no-repeat;
}
</style>
