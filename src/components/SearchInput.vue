<template>
  <el-input
    class="search-input"
    placeholder="Search"
    v-model="searchWord">
    <i slot="suffix" class="el-input__icon el-icon-search"></i>
  </el-input>
</template>

<script>
</script>

<style lang="scss" scoped>
.search-input /deep/ {
  width: 200px;
  input {
    padding: 0 5px;
    border: none;
    border-bottom: 1px solid #bbc1c2;
    background-color: inherit;
    border-radius: 0;
  }
  ::placeholder {
    color: #bbc1c2;
  }
  .el-input__icon {
    font-size: 20px;
  }
}
</style>
