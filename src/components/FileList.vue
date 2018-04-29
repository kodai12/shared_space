<template>
<el-row>
  <el-col :span="8" v-for="(file, index) in files" :key="file.id" :offset="index">
    <el-card :body-style="{ padding: '0px' }">
      <img
        :src="file.data"
        class="image">
      <div style="padding: 14px;">
        <h2 class="title">{{ file.title }}</h2>
        <div class="bottom clearfix">
          <time class="time">{{ file.created_at }}</time>
          <span class="author">{{ file.author }}</span>
          <el-button type="text" class="button">Operating button</el-button>
        </div>
      </div>
    </el-card>
  </el-col>
</el-row>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      files: [],
    };
  },
  created() {
    this.fetchAllFileData();
  },
  methods: {
    fetchAllFileData() {
      const url = '/api/files';
      axios.get(url).then((res) => {
        this.files = res.data;
      }).catch((err) => {
        /* eslint-disable */
        console.error(err.message);
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both
}
</style>
