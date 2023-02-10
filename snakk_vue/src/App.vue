<template>
    <div>
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

        <router-view/>

        <footer>
            <div class="has-text-centered">Copyright (c) 2023</div>
        </footer>
    </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';

.navbar.is-dark {
    background-color: #222;
}

body {
    background: #333;
}

.landing-page {
    min-height: 100vh;

    .content {
        color: #aaa;

        h1 {
            color: #eee
        }

        h2, h3 {
            font-weight: 200;
            color:#bbb;
        }

        label {
            font-size: 13px;
            color: #aaa;
        }

        hr {
            background: #444;
        }

        @media (max-width: 767px) {
            .reverse-coluns {
                flex-direction: column-reverse;
                display: flex;
            }
        }
    }
}

</style>

