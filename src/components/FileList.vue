<template>
<ul class="file-list">
  <li
    class="file-list__item"
    v-for="file in files"
    :key="file.id">
    <img
      class="preview-img"
      :src="file.data"
      alt="">
    <h2 class="title">{{ file.title }}</h2>
    <span class="created-at">{{ file.created_at }}</span>
    <span class="author">{{ file.author }}</span>
    <a class="img-link" href="#">{{ file.id }}</a>
  </li>
</ul>
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
