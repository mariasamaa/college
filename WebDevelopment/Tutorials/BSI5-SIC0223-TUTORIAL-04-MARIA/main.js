const app = Vue.createApp({
    data() {
        return {
            product: 'Socks',
            image: './assets/images/socks_blue.jpg',
            inStock: false,   //new data property
            inventory: 15,
            onSale: true
        }
    }
})