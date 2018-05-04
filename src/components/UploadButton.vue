<template>
  <el-upload
    class="uploader"
    action="/api/file"
    name="uploadFile"
    accept=".jpg, .jpeg, .png, .bmp, .pdf"
    :on-preview="handlePreview"
    :on-remove="handleRemove"
    :on-error="handleUploadError"
    :on-change="handleChange"
    :file-list="fileList"
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
</template>

<script>
export default {
  data() {
    return {
      fileList: [],
    };
  },
  methods: {
    /* eslint-disable */
    handleRemove(file, fileList) {
    },
    handlePreview(file) {
    },
    handleUploadError(err) {
      console.error(`error is ${err}`);
    },
    handleChange(file, fileList) {
      console.log(file);
      console.log(fileList);
      this.fileList = fileList;
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
    flex-direction: column;
    align-items: center;
  }
  .el-upload-list__item {
    width: 30%;
  }
}
</style>
