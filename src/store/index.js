import Vue from 'vue';
import Vuex from 'vuex';
import process from 'process';

Vue.use(Vuex);

export default new Vuex.Store({
  strict: process.env.NODE_ENV !== 'production',
  state: {
    isPreviewOn: false,
  },
  mutations: {
    togglePreviewModal(state, payload) {
      state.isPreviewOn = payload.isPreviewOn;
    }
  },
  getters: {},
  actions: {},
});
