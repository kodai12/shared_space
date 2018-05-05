<template>
  <div class="login-wrapper">
    <LoginForm></LoginForm>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm';

export default {
  components: {
    LoginForm
  }
};
</script>

<style lang="scss" scoped>
.login-wrapper {
  padding-top: 30px;
}
</style>
