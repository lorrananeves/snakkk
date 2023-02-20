<template>
    <div class="about">
        <Navbar />

        <section class="section landing-page">
            <div class="content">
                <section class="hero is-medium">
                    <div class="hero-body has-text-centered">
                        <h1 class="is-size-1">About</h1>
                        <h2 class="is-size-4">A chat application for teams and individuals...</h2>
                    </div>
                </section>
            </div>
        </section>

        <Footer />
    </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue'
  import Footer from '@/components/Footer.vue'

  export default {
    components: {
      Navbar,
      Footer
    }
  }
</script>