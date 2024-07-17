const app = Vue.createApp({
    data() {
        return {
            cart: [],
            premium: true
        }
    },
    methods: {
        updateCart(id) {
            id ? this.cart.push(id) : this.cart.pop()
        }
    }
})
