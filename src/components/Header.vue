<template>
  <el-header class="header" :style="customHeight">
    <h1 class="heading1">Shared Space For Aratana 18's</h1>
    <div class="login-info" v-if="loginUser">
      <span class="login-user">Login As {{ loginUser }}</span>
      <a href="#" class="logout-link">Log Out</a>
    </div>
  </el-header>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      loginUser: '',
      customHeight: {
        'height': '700px'
      },
    };
  },
  mounted() {
    this.fetchLoginUser();
  },
  methods: {
    fetchLoginUser() {
      const url = './api/login-user';
      axios.get(url).then((res) => {
        this.loginUser = res.data;
      }).catch((err) => {
        /* eslint-disable no-console */
        console.error(err);
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 30px;
  color: #fff;
  background-image: url('~/static/images/aratana18\'s.jpg');
  background-size: 100vw auto;
  background-position: center center;
  background-repeat: no-repeat;
  opacity: 0.5;
}
.heading1 {
  margin: auto 0;
  font-size: 50px;
}
.login-info {
  display: flex;
  flex-direction: column;
  margin: auto 0 auto auto;
  font-size: 12px;
  text-align: right;
}
.login-user {
  margin-bottom: 5px;
}
.logout-link {
  color: #fff;
}
</style>
