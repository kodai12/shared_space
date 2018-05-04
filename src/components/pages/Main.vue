<template>
  <article class="main-article">
    <UploadButton></UploadButton>
    <FileList></FileList>
    <PreviewModal v-if="isPreviewOn"></PreviewModal>
  </article>
</template>

<script>
import { mapState } from 'vuex';

import UploadButton from '@/components/UploadButton';
import FileList from '@/components/FileList';
import PreviewModal from '@/components/Preview';

export default {
  components: {
    UploadButton,
    FileList,
    PreviewModal
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
