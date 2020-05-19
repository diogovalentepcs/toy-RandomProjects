var app = new Vue({
    el: '#app',
    data: {
        product: 'Socks',
        image: './image-blue.jpg',
        inventory: 0,
        details: ['80% cotton', '20% polyester', 'Gender-Neutral'],
        variants: [{
                variantId: 2234,
                variantColor: 'green',
                variantImage: './image-green.jpg',
            },
            {
                variantId: 2235,
                variantColor: 'blue',
                variantImage: './image-blue.jpg',
            }
        ],
        cart: 0,
    },
    methods: {
        addToCart: function() {
            this.cart += 1
        },
        updateProduct: function(imagePath) {
            this.image = imagePath
        }
    }
})