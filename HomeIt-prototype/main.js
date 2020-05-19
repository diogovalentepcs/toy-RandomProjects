var app = new Vue({
    el: '#app',
    data: {
        product: 'Socks',
        image: './house1.jpeg',
        imageIndex: 1,
        inventory: 0,
        details: ['./house1.jpeg', './house2.jpeg', './house3.jpeg', './house4.jpeg'],
        variants: [{
                variantId: 1,
                variantImage: './house1.jpeg',
            },
            {
                variantId: 2,
                variantImage: './house2.jpeg',
            },
            {
                variantId: 3,
                variantImage: './house3.jpeg',
            },
            {
                variantId: 4,
                variantImage: './house4.jpeg',
            },
        ],
        cart: 0,
    },
    methods: {
        addToCart: function() {
            this.cart += 1
        },
        updateProduct: function(imagePath) {
            this.image = imagePath
        },
        swipeRight: function(imageIndex) {
            if (this.imageIndex < 4) {
                this.imageIndex += 1
                this.image = this.details[imageIndex]

            } else {
                this.image = this.details[1]
                this.imageIndex = 1
            }
        }
    }
})