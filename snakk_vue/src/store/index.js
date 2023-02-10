import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      id: null,
      username: null,
      full_name: null,
      isAuthenticated: false,
      token: null
    }
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.user.token = localStorage.getItem('token')
        state.user.user.id = localStorage.getItem('user_id')
        state.user.username = localStorage.getItem('user_username')
        state.user.full_name = localStorage.getItem('user_full_name')
        state.user.isAuthenticated = true
      }
    },
    setToken(state, token) {
      state.user.token = token
      state.user.isAuthenticated = true
    },
    removeToken(state) {
      state.user.token = null
      state.user.id = null
      state.user.username = null
      state.user.full_name = null
      state.user.isAuthenticated = false

      localStorage.setItem('token', '')
      localStorage.setItem('user_id', '')
      localStorage.setItem('user_username', '')
      localStorage.setItem('user_full_name', '')
    },
    setUser(state, user) {
      state.user.id = user.user_id
      state.user.username = user.user_username
      state.user.full_name = user.user_full_name
    }
  },
  actions: {
  },
  modules: {
  }
})
