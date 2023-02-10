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
                                    <label>Usename</label>
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
        submitForm () {
            console.log('submitForm')
        }
    },
}
</script>
