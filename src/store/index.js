import Vue from 'vue';
import Vuex from 'vuex';
import process from 'process';

Vue.use(Vuex);

export default new Vuex.Store({
  strict: process.env.NODE_ENV !== 'production',
  state: {
    isPreviewOn: false,
    selectedFile: {},
    selectedAuthor: 'all',
    searchWord: '',
  },
  mutations: {
    togglePreviewModal(state, payload) {
      state.isPreviewOn = payload.isPreviewOn;
    },
    selectFile(state, payload) {
      state.selectedFile = payload.selectedFile;
    },
    sortByAuthor(state, payload) {
      state.selectedAuthor = payload.selectedAuthor;
    },
    searchByInputWord(state, payload) {
      state.searchWord = payload.searchWord;
    }
  },
  getters: {},
  actions: {},
});
