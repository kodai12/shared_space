<template>
  <form
    action="/api/file"
    method="post"
    enctype="multipart/form-data"
    class="upload-form">
    <el-upload
      class="uploader"
      action=""
      :http-request="uploadFile"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      list-type="picture">
      <el-button
        size="small"
        type="primary">
        Click to upload
      </el-button>
      <div slot="tip" class="el-upload__tip">
        jpg/png files with a size less than 500kb
      </div>
    </el-upload>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      fileList2: [
        {
          name: 'food.jpeg',
          url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'
        },{
          name: 'food2.jpeg',
          url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'
        }
      ]
    };
  },
  methods: {
    handleRemove(file, fileList) {
      /* eslint-disable no-console */
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    uploadFile() {
      const params = new FormData();
      const file = document.querySelector('[name="file"]');
      params.append('file', file.files[0]);
      console.log(file.files[0]);
      axios.post('/api/file', params, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then((res) => {
        console.log(res);
      }).catch((err) => {
        console.error(err.message);
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.upload-form {
  margin-bottom: 30px;
}
.uploader /deep/ {
  text-align: center;
  .el-upload-list {
    display: flex;
    flex-basis: column;
    align-items: center;
  }
  .el-upload-list__item {
    width: 30%;
  }
}
</style>
