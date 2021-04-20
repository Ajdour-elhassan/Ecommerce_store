const app = Vue.createApp({
    data() {
        return {
            cart: 0
        };
    },
    // computed: {
    //     CartNumber() {
    //         return this.cart;
    //     }
    // },
    methods: {

        AddToCart() {
            this.cart += 1;
        },
        RemoveInCart() {
            this.cart -= 1;
        }
    }
});
amount.app("#store");