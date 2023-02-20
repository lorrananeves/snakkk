<template>
    <div class="login">
        <Navbar />

        <section class="section landing-page">
            <div class="content">
                <div class="columns">
                    <div class="column is-4 is-offset-4">
                        <div class="box form-box has-text-centered">
                            <h1>Log in</h1>

                            <form @submit.prevent="submitForm" class="mb-6">
                                <div class="field">
                                    <label>Username</label>
                                    <div class="control">
                                        <input type="text" name="username" class="input" v-model="username">
                                    </div>
                                </div>

                                <div class="field">
                                    <label>Password</label>
                                    <div class="control">
                                        <input type="password" name="password" class="input" v-model="password">
                                    </div>
                                </div>

                                <div 
                                    class="notification is-danger"
                                    v-if="errors.length"
                                >
                                    <p
                                        v-for="error in errors"
                                        v-bind:key="error"
                                    >
                                        {{ error }}
                                    </p>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <button class="button is-success">Submit</button>
                                    </div>
                                </div>
                            </form>

                            <hr>

                            <h3 class="mt-6">Don't have an account?</h3>

                            <a href="/signup">Click here</a> to sign up for free.
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
    name: 'LogIn',
    components: {
        Navbar, 
        Footer
    },
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods: {
        async submitForm() {
            console.log('submitForm')

            this.errors = []

            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post('/api/v1/token/login/', formData)
                .then(response => {
                    console.log(response)

                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        console.log(JSON.stringify(error))
                    }
                })
            
            if (this.$store.state.user.isAuthenticated) {
                axios
                    .get('/api/v1/userprofile/get_my_information/')
                    .then(response => {
                        console.log(response)

                        this.$store.commit('setUser', {
                            'user_id': response.data.id,
                            'user_username': response.data.username,
                            'user_full_name': response.data.get_full_name
                        })

                        localStorage.setItem('user_id', response.data.id)
                        localStorage.setItem('user_username', response.data.username)
                        localStorage.setItem('user_full_name', response.data.get_full_name)

                        this.$router.push('/dashboard')
                    })
            }
        }
    }
}
</script>