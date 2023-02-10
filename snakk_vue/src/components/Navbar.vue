<template>
    <nav class="navbar is-dark pt pb-4">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item is-size-4"><strong>Snakk</strong></router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <template v-if="$store.state.user.isAuthenticated">
                    <router-link to="/dashboard/" class="navbar-item">Dashboard</router-link>

                    <div class="navbar-item">
                        <a class="button is-danger" @click="logout()">Log out</a>
                    </div>
                </template>

                <template v-else>

                    <router-link to="/about" class="navbar-item">About</router-link>

                    <div class="navbar-item">
                        <div class="buttons">
                            <router-link to="/signup" class="button is-primary"><strong>Sign Up</strong></router-link>
                            <router-link to="/login" class ="button is-light">Login</router-link>
                        </div>
                    </div>
                </template>
            </div>
        </div>
    </nav>
</template>

<style lang="scss" scoped>
.navbar.is-dark {
background-color: #222;
}
</style>

<script>
import axios from 'axios'
export default {
    methods: {
        async logout() {
            await axios
                .post("/api/v1/token/logout")
                .then(response => {
                    console.log('Logged out!')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
            axios.defaults.headers.common["Authorization"] = ""

            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}
</script>
    