<template>
    <div class="chat">
        <div class="columns">
            <div class="column is-2">
                <div class="sidebar">
                    <div class="sidebar_info">
                        <div class="box">
                            <h2 class="subtitle"><a>{{ $store.state.team.name }}</a></h2>

                            <h3 class="user">
                                <a>
                                    <template v-if="$store.state.user.full_name">
                                        {{ $store.state.user.full_name }}
                                    </template>
                                    <template v-else>
                                        {{ $store.state.user.username }}
                                    </template>
                                </a>
                            </h3>
                        </div>
                    </div>

                    <hr>

                    <aside class="menu">
                        <p class="menu-label">Channels <span>(add)</span></p>

                        <ul class="menu-list">
                            <li><a>channel 1</a></li>
                            <li><a>channel 1</a></li>
                            <li><a>channel 2</a></li>
                        </ul>

                        <hr>

                        <p class="menu-label">Direct messages</p>

                        <ul class="menu-list">
                            <li><a>lolo</a></li>
                            <li><a>lala</a></li>
                            <li><a>piu</a></li>
                        </ul>
                    </aside>
                </div>
            </div>

            <div class="column is-10">
                <div class="main-content">
                    <div class="messages" id="messages">
                        <article class="media">
                            <figure class="media-left">
                                <p class="image is-64x64">
                                    <img src="https://bulma.io/images/placeholders/128x128.png">
                                </p>
                            </figure>

                            <div class="media-content">
                                <div class="content">
                                    <p>
                                        <strong> user name</strong>
                                        &nbsp;
                                        <small>10 minutes ago</small>
                                        <br>
                                        Lorem ipsun dolor sit amet
                                    </p>
                                </div>
                            </div>
                        </article>

                        <article class="media">
                            <figure class="media-left">
                                <p class="image is-64x64">
                                    <img src="https://bulma.io/images/placeholders/128x128.png">
                                </p>
                            </figure>

                            <div class="media-content">
                                <div class="content">
                                    <p>
                                        <strong> user name</strong>
                                        &nbsp;
                                        <small>10 minutes ago</small>
                                        <br>
                                        Lorem ipsun dolor sit amet
                                    </p>
                                </div>
                            </div>
                        </article>

                        <article class="media">
                            <figure class="media-left">
                                <p class="image is-64x64">
                                    <img src="https://bulma.io/images/placeholders/128x128.png">
                                </p>
                            </figure>

                            <div class="media-content">
                                <div class="content">
                                    <p>
                                        <strong> user name</strong>
                                        &nbsp;
                                        <small>10 minutes ago</small>
                                        <br>
                                        Lorem ipsun dolor sit amet
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

export default {
    name: 'Chat',
    data() {
        return {
            team_id: null,
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

    .sidebar .box {
        background: #383838;
    }

    .sidebar .sidebar__info h2 {
        margin-bottom: 10px;
    }

        .sidebar .sidebar__info h2  a {
            color: #fff;
        }
    
    .sidebar .sidebar__info .user {
        font-size: 13px;
    }

        .sidebar .sidebar__info .user a {
            color: #fff;
        }
    
    .sidebar .menu .menu-label {
        color: #aaa;
    }

        .sidebar .menu .menu-label span {
            cursor: pointer;
        }
    
    .sidebar .menu .menu-label a {
        color: #aaa;

        &.new-message {
            font-weight: bold;
        }

        &.is-active {
            background-color: #111;
        }

        &.online {
            position: relative;

            &:before {
                width: 5px;
                height: 5px;
                position: absolute;
                top: 16px;
                left: 3px;
                content: '';
                border-radius: 5px;
                background: #90ee90;
            }
        }
    }

    .sidebar hr {
        background: #333;
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