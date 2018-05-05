<template>
  <article class="main-article">
    <UploadButton></UploadButton>
    <SortSelect></SortSelect>
    <FileList></FileList>
    <PreviewModal v-if="isPreviewOn"></PreviewModal>
  </article>
</template>

<script>
import { mapState } from 'vuex';

import UploadButton from '@/components/UploadButton';
import FileList from '@/components/FileList';
import PreviewModal from '@/components/Preview';
import SortSelect from '@/components/SortSelect';

export default {
  components: {
    UploadButton,
    FileList,
    PreviewModal,
    SortSelect
  },
  computed: mapState([
    'isPreviewOn'
  ]),
};
</script>

<style lang="scss" scoped>
.main-article {
  padding: 30px 50px 0;
}
</style>
