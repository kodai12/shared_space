<template>
  <div class="modal-window">
    <div class="modal-container">
      <object
        class="modal-object"
        :data="selectedImage">
      </object>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedImage: './static/files/arupaka.jpg'
    };
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

.modal-object {
  display: block;
  width: 100%;
  height: 100%;
  background-position: center center;
  background-size: contain;
  background-repeat: no-repeat;
}
</style>
