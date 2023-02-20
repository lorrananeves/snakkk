<template>
    <div class="dashboard">
        <Navbar />

        <section class="section landing-page">
            <div class="container">
                <div class="columns is-multiline">
                    <div 
                        class="column is-4"
                        v-for="team in teams"
                        v-bind:key="team.id"
                    >
                        <div class="card">
                            <div class="card-content">
                                <div class="media">
                                    <div class="media-content">
                                        <p class="title is-4">{{ team.name }}</p>
                                        <p class="subtitle is-6">{{ team.members.length }} members</p>
                                    </div>
                                </div>

                                <div class="content">
                                    <router-link :to="{name: 'Chat', params: { team_id: team.id }}" class="button is-info">Join chat</router-link>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <Footer />
    </div>
</template>

<script>
import axios from 'axios'

import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'

export default {
    name: 'Dashboard',
    components: {
        Navbar, 
        Footer
    },
    data() {
        return {
            teams: []
        }
    },
    mounted() {
        this.getTeams()
    },
    methods: {
        async getTeams() {
            axios
                .get('/api/v1/teams/get_teams/')
                .then(response => {
                    console.log(response)

                    this.teams = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>