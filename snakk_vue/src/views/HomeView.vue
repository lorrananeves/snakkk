<template>
  <div class="home">
    <Navbar />
    
    <section class="section landing-page">
      <div class="content">
        <section class="hero is-medium">
          <div class="hero-body has-text-centered">
            <h1 class="is-size-1"> Welcome to Snakk</h1>
            <h2 class="is-size-4">Bring your team together</h2>
          </div>
        </section>

        <section class="hero is-small">
          <div class="hero-body">
            <div class="container">
              <div class="columns is-centered">
                <div class="column is-4 is-offset-1">
                  <figure class="image">
                    <img src="@/assets/numero1.png">
                  </figure>
                </div>
                
                <div class="column is5 is-offset-1">
                  <h2 class="title is-2 mb-6"> Group Chats</h2>

                  <h3 class="subtitle is-5">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</h3>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section class="hero is-small">
          <div class="hero-body">
            <div class="container">
              <div class="columns is-centered reverse-columns">
                
                <div class="column is5 is-offset-1">
                  <h2 class="title is-2 mb-6"> Group Chats</h2>

                  <h3 class="subtitle is-5">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</h3>
                </div>

                <div class="column is-4 is-offset-1">
                  <figure class="image">
                    <img src="@/assets/numero1.png">
                  </figure>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section class="hero is-small">
          <div class="hero-body">
            <div class="container">
              <div class="columns is-centered">
                <div class="column is-4 is-offset-1">
                  <figure class="image">
                    <img src="@/assets/numero1.png">
                  </figure>
                </div>
                
                <div class="column is5 is-offset-1">
                  <h2 class="title is-2 mb-6"> Group Chats</h2>

                  <h3 class="subtitle is-5">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</h3>
                </div>
              </div>
            </div>
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