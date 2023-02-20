<template>
    <div class="chat">
        <div class="columns">
            <div class="column is-2">
                <div class="sidebar">
                    <SidebarInfo />

                    <SidebarMenu />
                </div>
            </div>

            <div class="column is-10">
                <div class="main-content">
                    <div class="messages" id="messages">
                        <article 
                            class="media"
                            v-for="message in messages"
                            v-bind:key="message.id"
                        >
                            <figure class="media-left">
                                <p class="image is-64x64">
                                    <img src="https://bulma.io/images/placeholders/128x128.png">
                                </p>
                            </figure>

                            <div class="media-content">
                                <div class="content">
                                    <p>
                                        <strong>{{ message.created_by.username }}</strong>
                                        &nbsp;
                                        <small>10 minutes ago</small>
                                        <br>
                                        {{ message.content }}
                                    </p>
                                </div>
                            </div>
                        </article>
                    </div>

                    <div class="messages-form">
                        <form>
                            <div class="field has-addons">
                                <div class="control control-input">
                                    <input type="text" class="input" placeholder="Message...">
                                </div>

                                <div class="control">
                                    <button class="button is-dark">Send</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import SidebarInfo from '@/components/Chat/SidebarInfo'
import SidebarMenu from '@/components/Chat/SidebarMenu'

export default {
    name: 'Chat',
    components: {
        SidebarInfo,
        SidebarMenu
    },
    data() {
        return {
            team_id: null,
            connection: null,
            messages: []
        }
    },
    created() {
        this.team_id = this.$route.params.team_id

        axios
            .get(`/api/v1/teams/get_team/${this.team_id}/`)
            .then(response => {
                console.log(response.data)

                this.$store.commit('setTeam', response.data)
            })
            .catch(error => {
                console.log(error)
            })
    },
    mounted() {
        this.connection = new WebSocket("ws://127.0.0.1:8000/ws/roomname/?token=" + this.$store.state.user.token)

        this.connection.onmessage = (event) => {
            console.log(event)
        }

        this.connection.onopen = (event) => {
            console.log('successfully connected')

            this.getMessages()
        }

        this.connection.onclose = (event) => {
            console.log('successfully disconnected')
        }
    },
    methods: {
        getMessages() {
            axios
                .get('/api/v1/messages/get_messages/' + this.$route.params.team_id + '/')
                .then(response => {
                    console.log(response.data)
                    this.messages = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>

<style lang="scss" scoped>
.columns, .column {
    margin: 0 !important;
    padding: 0;
}

.sidebar {
    height: 100vh;
    padding: 10px;
    background: #222;
}

.main-content {
    height: 100vh;
    padding: 10px;
}

    .main-content .messages {
        height: calc(100vh - 90px);
        overflow: auto;
    }

        .main-content .messages .media {
            color: #999;
        }

            .main-content .messages .media+.media {
                border-top: 1px solid #444;
            }

            .main-content .messages .media strong {
                color: #aaa;
            }

    .main-content .messages-form {
        margin-top: 10px;
        padding: 10px;
    }

    .main-content .messages-form .control-input {
        width: 100%;
    }

        .main-content .messages-form .control-input input {
            background: #555;
            border: #555;
            color: #aaa;
        }

        .main-content .messages-form .control-input input::placeholder {
            color: #777;
            opacity: 1;
        }

        .main-content .messages-form .is-valid {
            border-color: #478778;
            background: #478778;
        }
</style>