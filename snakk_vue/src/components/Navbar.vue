<template>
    <nav class="navbar is-dark pt pb-4">
            <div class="navbar-brand">
                <router-link to="/" class="navbar-item is-size-4"><strong>Snakk</strong></router-link>
            </div>

            <div class="navbar-menu">
                <div class="navbar-end">
                    <router-link to="/about" class="navbar-item">About</router-link>

                    <div class="navbar-item">
                        <div class="buttons">
                            <router-link to="/signup" class="button is-primary"><strong>Sign Up</strong></router-link>
                            <router-link to="/login" class ="button is-light">Login</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    </template>

    <style lang="scss" scoped>
    .navbar.is-dark {
    background-color: #222;
    }
    </style>