<template>
    <div class="signup">
        <Navbar />

        <section class="section landing-page">
            <div class="content">
                <div class="columns">
                    <div class="column is-4 is-offset-4">
                        <div class="box form-box has-text-centered">
                            <h1>Sign Up</h1>

                            <form @submit.prevent="submitForm" class="mb-6">
                                <div class="field">
                                    <label>Usename</label>
                                    <div class="control">
                                    <input type="text" name="username" class="input" v-model="username">
                                    </div>
                                </div>

                                <div class="field">
                                    <label>Password</label>
                                    <div class="control">
                                    <input type="password" name="password1" class="input" v-model="password1">
                                    </div>
                                </div>

                                <div class="field">
                                    <label>Repeat password</label>
                                    <div class="control">
                                    <input type="password" name="password2" class="input" v-model="password2">
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

                            <h3 class="mt-6">Already have an account?</h3>

                            <a href="/login">Click here</a> to log in.
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
    name: 'SignUp',
    components: {
    Navbar,
    Footer
    },
    data() {
        return {
            username: '',
            password1: '',
            password2: '',
            errors: []
        }
    },
    methods: {
        submitForm () {
            console.log('submitForm')

            const formData = {
                username: this.username,
                password: this.password1
            }

            this.errors = []

            axios
                .post('/api/v1/users/', formData)
                .then(response => {
                    console.log(response)

                    this.$router.push('/login')
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
        }
    },
}
</script>
