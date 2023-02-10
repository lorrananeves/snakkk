<template>
    <div>
        <router-view/>
    </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';



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

