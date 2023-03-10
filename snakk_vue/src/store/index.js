import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      id: null,
      username: null,
      full_name: null,
      isAuthenticated: false,
      token: null
    },
    team: {
      id: null,
      name: '',
      channels: [],
      members: [],
    },
    currentChannel: {}
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
    },
    setTeam(state, team) {
      state. team = {
        id: null,
        name: '',
        channels: [],
        members: []
      } 

      state.team.id = team.id
      state.team.name = team.name
      state.teammembers = team.members
      state.team.channels = team.channels

      if (localStorage.getItem('currentChannel')) {
        state.currentChannel = JSON.parse(localStorage.getItem('currentChannel'))
      } else {
        state.currentChannel = state.team.channels[0]
      }
    },
    addChannel(state, channel) {
      state.team.channels.push(channel)
    },
    setCurrentChannel(stat, channel) {
      state.currentChannel = channel

      localStorage.setItem('currentChannel', JSON.stringify(channel))
    }
  },
  actions: {
  },
  modules: {
  }
})
