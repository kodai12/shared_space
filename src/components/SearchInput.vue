<template>
  <el-input
    class="search-input"
    placeholder="Search"
    clearable
    v-model="searchWord"
    @change="search"
    @clear="search">
    <i slot="suffix" class="el-input__icon el-icon-search"></i>
  </el-input>
</template>

<script>
import { mapMutations } from 'vuex';

export default {
  data() {
    return {
      searchWord: ''
    };
  },
  methods: {
    ...mapMutations([
      'searchByInputWord'
    ]),
    search() {
      this.searchByInputWord({searchWord: this.searchWord});
    }
  }
};
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
