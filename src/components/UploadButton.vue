<template>
  <el-upload
    class="uploader"
    action="/api/file"
    name="uploadFile"
    drag
    accept=".jpg, .jpeg, .png, .bmp, .pdf"
    :on-error="handleUploadError"
    :on-change="handleChange"
    :file-list="fileList"
    list-type="picture">
    <el-button
      size="small"
      type="primary">
      Click/Drag to upload
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
    handleUploadError(err) {
      alert(`error: ${err.message}`);
    },
    handleChange(file, fileList) {
      this.fileList = fileList;
    }
  }
};
</script>

<style lang="scss" scoped>
.uploader /deep/ {
  margin-bottom: 20px;
  text-align: center;
  .el-upload-list {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .el-upload-list__item {
    width: 30%;
  }
  .el-upload-dragger {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 200px;
    height: 60px;
  }
}
</style>
