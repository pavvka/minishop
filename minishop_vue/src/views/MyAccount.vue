<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="subtitle" v-if="this.user_data[0]">Wellcome, {{ this.user_data[0].username }}</h2>
            </div>

            <div class="column is-2">
                <aside class="menu">
                    <ul class="menu-list">
                        <li><a @click="togglemyOrdersComponent">My orders</a></li>
                        <li><a @click="togglemyReturnsComponent">My returns</a></li>
                        <li><a @click="togglemyDetailsComponent">My details</a></li>
                        <li><a @click="toggleadderssBookComponent">Address book</a></li>
                        <li><a @click="togglegiftCardsComponent">Gift cards</a></li>
                        <li><a @click="logout()" class="is-dark">Log out</a></li>
                    </ul>
                </aside>
            </div>

            <div class="column is-10" v-if="myOrdersComponent">
                <h2 class="subtitle">My orders</h2>

                <OrderSummary
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order" />
            </div>
            <div class="column is-10" v-if="myReturnsComponent">
                <h2 class="subtitle">My returns</h2>
            </div>
            <div class="column is-10" v-if="myDetailsComponent">
                <h2 class="subtitle">My details</h2>

                <UserDetails
                    :userdata="this.user_data[0]" />

            </div>
            <div class="column is-10" v-if="adderssBookComponent">
                <h2 class="subtitle">Address book</h2>
            </div>
            <div class="column is-10" v-if="giftCardsComponent">
                <h2 class="subtitle">Gift cards</h2>
            </div>


            <hr>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import OrderSummary from '@/components/OrderSummary.vue'
import UserDetails from '@/components/UserDetails.vue'
export default {
    name: 'MyAccount',
    components: {
        OrderSummary,
        UserDetails
    },
    data() {
        return {
            orders: [],
            user_data: [],
            myOrdersComponent: false,
            myReturnsComponent: false,
            myDetailsComponent: false,
            adderssBookComponent: false,
            giftCardsComponent: false,
        }
    },
    async mounted() {
        document.title = 'My account | Djackets'
        this.getMyOrders(),
        await this.getUserData(),
        console.log("TEST USER DATA: ", this.user_data)
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$store.commit('removeToken')
            this.$router.push('/')
        },
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get('/api/v1/orders/')
                .then(response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },
        async getUserData() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get('/api/v1/users/')
                .then(response => {
                    this.user_data = response.data
                    console.log("User data: ", this.user_data)
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },
        // Components conditional rendering

        // close all windows before show a new one
        closeAllComponents(){
            this.myOrdersComponent = false
            this.myReturnsComponent = false
            this.myDetailsComponent = false
            this.adderssBookComponent = false
            this.giftCardsComponent = false
        },
        togglemyOrdersComponent () {
            this.closeAllComponents()
            this.myOrdersComponent = !this.myOrdersComponent;
        },
        togglemyReturnsComponent () {
            this.closeAllComponents()
            this.myReturnsComponent = !this.myReturnsComponent;
        },
        togglemyDetailsComponent () {
            this.closeAllComponents()
            this.myDetailsComponent = !this.myDetailsComponent;
        },
        toggleadderssBookComponent () {
            this.closeAllComponents()
            this.adderssBookComponent = !this.adderssBookComponent;
        },
        togglegiftCardsComponent () {
            this.closeAllComponents()
            this.giftCardsComponent = !this.giftCardsComponent;
        },
    }
}
</script>