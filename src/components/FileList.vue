<template>
<el-row class="files-list">
  <el-col
    :span="8"
    v-for="file in filesSortedByAuthor"
    :key="file.id"
    class="files-list-item">
    <el-card :body-style="{ padding: '0px' }">
      <embed
        v-if="file.data.split('.').pop() === 'pdf'"
        :src="file.data"
        type="application/pdf"
        class="file-object">
      <img
        v-else
        :src="file.data"
        class="file-image">
      <div style="padding: 14px;">
        <h2 class="title">{{ file.title }}</h2>
        <span class="author">By {{ file.author }}</span>
        <div class="bottom clearfix">
          <time class="time">{{ file.created_at }}</time>
          <el-button
            type="info"
            plain
            @click="previewOn(file)"
            class="preview-button">
            Preview
          </el-button>
        </div>
      </div>
    </el-card>
  </el-col>
</el-row>
</template>

<script>
import axios from 'axios';
import { mapState, mapMutations } from 'vuex';

export default {
  data() {
    return {
      files: [
        {
          data: '.static/files/arupaka.jpg',
          title: 'test',
          author: 'sakochi',
          created_at: '2018-01-01 00:00:00'
        }
      ],
    };
  },
  computed: mapState({
    filesSortedByAuthor(state) {
      if(state.selectedAuthor === 'all') {
        return this.files;
      }
      return this.files.filter((el) => el.author === state.selectedAuthor);
    }
  }),
  created() {
    this.fetchAllFileData();
  },
  methods: {
    ...mapMutations([
      'togglePreviewModal',
      'selectFile'
    ]),
    fetchAllFileData() {
      const url = '/api/files';
      axios.get(url).then((res) => {
        this.files = res.data;
      }).catch((err) => {
        /* eslint-disable no-console */
        console.error(err.message);
      });
    },
    previewOn(file) {
      console.log(file);
      this.togglePreviewModal({ isPreviewOn: true });
      this.selectFile({ selectedFile: file });
    }
  }
};
</script>

<style lang="scss" scoped>
.files-list {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  margin-top: 30px;
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

.preview-button {
  margin-left: auto;
}

.files-list-item-link {
  margin-left: auto;
}

.file-object,
.file-image {
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
