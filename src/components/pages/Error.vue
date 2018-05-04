<template>
  <div class="error-block">
    <h1 class="error-title">PAGE IS NOT FOUND</h1>
    <p class="error-message">The URL may incorrect and you can return to home.</p>
    <a href="/" class="back-home-link">
      <el-button type="info" plain>
        BACK TO HOME
      </el-button>
    </a>
  </div>
</template>

<style lang="scss" scoped>
.error-block {
  padding: 30px;
  text-align: center;
}
.error-title {
  margin-bottom: 10px;
  font-size: 20px;
}
.error-message {
  margin-bottom: 20px;
  font-size: 15px;
}
</style>
