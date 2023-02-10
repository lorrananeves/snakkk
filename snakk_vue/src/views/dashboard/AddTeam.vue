<template>
    <div class="add-team">
        <Navbar />

        <section class="section landing-page">
            <div class="container">
                <div class="collumns is-multiline">
                    <div class="columns is-4 is-offset-4">
                        <h1 class="title has-text-white">add team</h1>

                        <form @submit.prevent="submitForm" class="mb-6">
                            <div class="field">
                                <label class="has-text-white">Name</label>

                                <div class="control">
                                    <input type="text" name="name" class="input" v-model="name">
                                </div>
                            </div>

                            <div class="notification is-danger" v-if="errors.length">
                                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                            </div>

                            <div class="field">
                                <div class="control">
                                    <button class="button is-success">Submit</button>
                                </div>
                            </div>
                        </form>
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
    name: 'AddTeam',
    components: {
    Navbar,
    Footer
    },
    data() {
        return {
            name: '',
            errors: [],
        }
    },
    mounted() {
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.name.length > 0) {
                const formData = {
                    name: this.name
                }

                axios
                    .post("/api/v1/teams/created_team", formData)
                    .then(response => {
                        this.$router.push('/dashboard')
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
            } else {
                this.errors.push('The team name ir missing!')
            }
        }
    },  
}
</script>