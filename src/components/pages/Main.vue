<template>
  <div>
    <CustomHeader></CustomHeader>
    <article class="main-article">
      <UploadButton></UploadButton>
      <nav class="top-nav">
        <SortSelect></SortSelect>
        <SearchInput></SearchInput>
      </nav>
      <FileList></FileList>
      <PreviewModal v-if="isPreviewOn"></PreviewModal>
    </article>
  </div>
</template>

<script>
import { mapState } from 'vuex';

import CustomHeader from '@/components/Header';
import UploadButton from '@/components/UploadButton';
import FileList from '@/components/FileList';
import PreviewModal from '@/components/Preview';
import SortSelect from '@/components/SortSelect';
import SearchInput from '@/components/SearchInput';

export default {
  components: {
    CustomHeader,
    UploadButton,
    FileList,
    PreviewModal,
    SortSelect,
    SearchInput
  },
  computed: mapState([
    'isPreviewOn'
  ]),
};
</script>

<style lang="scss" scoped>
.main-article {
  padding: 30px 50px;
  background-color: #e8edee;
}
.top-nav {
  display: flex;
  justify-content: flex-end;
  .el-select + .search-input {
    margin-left: 20px;
  }
}
</style>
