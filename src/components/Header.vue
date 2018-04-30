<template>
  <el-header class="header">
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
  padding: 0 30px;
  background-color: #e8380d;
  color: #fff;
}
.heading1 {
  margin: auto 0;
  font-size: 18px;
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
