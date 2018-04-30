<template>
<el-row class="files-list">
  <el-col
    :span="8"
    v-for="file in files"
    :key="file.id"
    class="files-list-item">
    <el-card :body-style="{ padding: '0px' }">
      <img
        :src="file.data"
        class="image">
      <div style="padding: 14px;">
        <h2 class="title">{{ file.title }}</h2>
        <span class="author">By {{ file.author }}</span>
        <div class="bottom clearfix">
          <time class="time">{{ file.created_at }}</time>
          <a
            :href="`./file/${file.id}`"
            class="files-list-item-link">
            <el-button
                type="info"
                plain
                class="button">
              More Info
            </el-button>
          </a>
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
.files-list {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  &::after { // 3カラムの最終行で左揃えになるように調整
    content: '';
    display: block;
    width: 33.33333%;
  }
}

.files-list-item {
  margin-bottom: 30px;
}

.time {
  font-size: 13px;
  color: #999;
}

.author {
  display: block;
  margin-top: 10px;
}

.bottom {
  display: flex;
  align-items: center;
  margin-top: 12px;
  line-height: 12px;
}

.files-list-item-link {
  margin-left: auto;
}

.image {
  object-fit: cover;
  width: 100%;
  height: 250px;
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
