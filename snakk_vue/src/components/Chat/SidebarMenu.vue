<template>
<div>

    <hr>
    
    <aside class="menu">
        <p class="menu-label">Channels <span @click="showAddChannelModal = !showAddChannelModal">(add)</span></p>

        <ul class="menu-list">
            <li
                v-for="channel in $store.state.team.channels"
                :key="channel.id"
                @click="setCurrentChannel(channel, 'group')"
                >
                    <a
                        :class="{'is-active': channel.name === $store.state.currentChannel.name}"
                    >
                        {{ channel.name }}
                    </a>
            </li>
        </ul>

        <hr>

        <p class="menu-label">Direct messages</p>

        <ul class="menu-list">
            <li
                v-for="member in $store.state.team.members"
                :key="member.id"
                @click="setCurrentChannel(channel, 'dm')"    
            >
                <template v-if="member.full_name">
                    <a>{{ member.full_name }}</a>
                </template>
                <template v-else>
                    <a>{{ member.username }}</a>
                </template>
            </li>
        </ul>
    </aside>

    <div
        class="modal"
        :class="{'is-active': showAddChannelModal}"
    >
        <div class="modal-background"></div>  

        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">Add channhel</p>
                
                <button class="delete" @click="showAddChannelModal = !showAddChannelModal"></button>
            </header>

            <section class="modal-card-body">
                <div class="field">
                    <div class="control">
                        <input type="text" class="input" placeholder="Channel name..." v-model="newChannelName">
                    </div>
                </div>
            </section>

            <footer class="modal-card-foot">
                <button class="button is-succes" @click="submitNewChannel">Submit</button>
            </footer>
        </div> 
    </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            showAddChannelModal: false,
            newChannelName: '',
        }
    },
    mathods : {
        submitNewChannel() {
            console.log('submitNewChannel')

            if (this.newChannelName.length > 0) {
                axios
                    .post('/api/v1/channels/new_channel/', {
                        'team_id': this.$store.state.team.id,
                        'name': this.newChannelName
                    })
                    .then(response => {
                        this.showAddChannelModal = false

                        THIS.$store.commit('addChannel', {
                            'id': response.data.id,
                            'name': response.data.name,
                        })
                    })
                    .catch(error => {
                        console.log('erros', error)
                    })
            }
        },
        setCurrentChannel(channel, channel_type) {
            this.$store.commit('setCurrentChannel', channel)
        }
    }
}
</script>

<style lang="scss" scoped>
.menu .menu-label {
        color: #aaa;
    }

    .menu .menu-label span {
        cursor: pointer;
    }

.menu .menu-label a {
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

.hr {
    background: #333;
}
</style>