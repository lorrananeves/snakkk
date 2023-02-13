<template>
    <div class="sidebar_info">
        <div class="box">
            <h2 class="subtitle"><a>{{ $store.state.team.name }}</a></h2>

            <h3 class="user">
                <a>
                    <template v-if="$store.state.user.full_name">
                        {{ $store.state.user.full_name }}
                    </template>
                    <template v-else>
                        {{ $store.state.user.username }}
                    </template>
                </a>
            </h3>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.box {
    background: #383838;
}
.sidebar__info h2 {
    margin-bottom: 10px;
}

    .sidebar__info h2  a {
        color: #fff;
    }

.sidebar__info .user {
    font-size: 13px;
}

    .sidebar__info .user a {
        color: #fff;
    }
</style>