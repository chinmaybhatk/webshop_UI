// Organic Webshop Theme JavaScript
// Enhanced functionality for the organic webshop UI

(function() {
    'use strict';

    // Wait for DOM to be ready
    document.addEventListener('DOMContentLoaded', function() {
        initOrganicTheme();
    });

    function initOrganicTheme() {
        // Initialize all theme components
        initNavbar();
        initProductCards();
        initCategoryCards();
        initScrollAnimations();
        initCartFunctionality();
        initSearchFunctionality();
        initMobileMenu();
        initImageLazyLoading();
    }

    // Navbar functionality
    function initNavbar() {
        const navbar = document.querySelector('.navbar');
        if (!navbar) return;

        let scrolled = false;

        window.addEventListener('scroll', function() {
            const shouldBeScrolled = window.scrollY > 100;
            
            if (shouldBeScrolled && !scrolled) {
                navbar.classList.add('scrolled');
                scrolled = true;
            } else if (!shouldBeScrolled && scrolled) {
                navbar.classList.remove('scrolled');
                scrolled = false;
            }
        });

        // Smooth scroll for anchor links
        const anchorLinks = document.querySelectorAll('a[href^="#"]');
        anchorLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    // Product card enhancements
    function initProductCards() {
        const productCards = document.querySelectorAll('.product-card');
        
        productCards.forEach(card => {
            // Add to cart functionality
            const addToCartBtn = card.querySelector('.add-to-cart');
            if (addToCartBtn) {
                addToCartBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    handleAddToCart(this);
                });
            }

            // Quick view functionality
            const quickViewBtn = card.querySelector('.quick-view');
            if (quickViewBtn) {
                quickViewBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    showQuickView(card);
                });
            }

            // Wishlist functionality
            const wishlistBtn = card.querySelector('.wishlist-btn');
            if (wishlistBtn) {
                wishlistBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    toggleWishlist(this);
                });
            }
        });
    }

    // Category card interactions
    function initCategoryCards() {
        const categoryCards = document.querySelectorAll('.category-card');
        
        categoryCards.forEach(card => {
            card.addEventListener('click', function() {
                const categoryUrl = this.dataset.category;
                if (categoryUrl) {
                    window.location.href = categoryUrl;
                }
            });
        });
    }

    // Scroll animations
    function initScrollAnimations() {
        const animatedElements = document.querySelectorAll('.fade-in-up, .product-card, .feature-card');
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        animatedElements.forEach(el => {
            observer.observe(el);
        });
    }

    // Cart functionality
    function initCartFunctionality() {
        // Update cart count
        updateCartCount();

        // Cart toggle
        const cartToggle = document.querySelector('.cart-toggle');
        const cartSidebar = document.querySelector('.cart-sidebar');
        
        if (cartToggle && cartSidebar) {
            cartToggle.addEventListener('click', function(e) {
                e.preventDefault();
                cartSidebar.classList.toggle('open');
            });
        }

        // Quantity controls
        const quantityControls = document.querySelectorAll('.quantity-control');
        quantityControls.forEach(control => {
            const minusBtn = control.querySelector('.qty-minus');
            const plusBtn = control.querySelector('.qty-plus');
            const input = control.querySelector('.qty-input');

            if (minusBtn && plusBtn && input) {
                minusBtn.addEventListener('click', function() {
                    const currentVal = parseInt(input.value) || 1;
                    if (currentVal > 1) {
                        input.value = currentVal - 1;
                        updateCartItem(input);
                    }
                });

                plusBtn.addEventListener('click', function() {
                    const currentVal = parseInt(input.value) || 1;
                    input.value = currentVal + 1;
                    updateCartItem(input);
                });

                input.addEventListener('change', function() {
                    const val = parseInt(this.value) || 1;
                    this.value = Math.max(1, val);
                    updateCartItem(this);
                });
            }
        });
    }

    // Search functionality
    function initSearchFunctionality() {
        const searchInput = document.querySelector('.search-input');
        const searchResults = document.querySelector('.search-results');
        
        if (searchInput) {
            let searchTimeout;
            
            searchInput.addEventListener('input', function() {
                clearTimeout(searchTimeout);
                const query = this.value.trim();
                
                if (query.length >= 2) {
                    searchTimeout = setTimeout(() => {
                        performSearch(query);
                    }, 300);
                } else if (searchResults) {
                    searchResults.style.display = 'none';
                }
            });

            // Hide search results when clicking outside
            document.addEventListener('click', function(e) {
                if (!searchInput.contains(e.target) && searchResults) {
                    searchResults.style.display = 'none';
                }
            });
        }
    }

    // Mobile menu
    function initMobileMenu() {
        const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
        const mobileMenu = document.querySelector('.mobile-menu');
        
        if (mobileMenuToggle && mobileMenu) {
            mobileMenuToggle.addEventListener('click', function() {
                mobileMenu.classList.toggle('open');
                this.classList.toggle('active');
            });

            // Close menu when clicking on links
            const mobileLinks = mobileMenu.querySelectorAll('a');
            mobileLinks.forEach(link => {
                link.addEventListener('click', function() {
                    mobileMenu.classList.remove('open');
                    mobileMenuToggle.classList.remove('active');
                });
            });
        }
    }

    // Image lazy loading
    function initImageLazyLoading() {
        const images = document.querySelectorAll('img[data-src]');
        
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        images.forEach(img => {
            imageObserver.observe(img);
        });
    }

    // Add to cart handler
    function handleAddToCart(button) {
        const productCard = button.closest('.product-card');
        const productId = productCard.dataset.productId;
        const productName = productCard.querySelector('.product-title').textContent;
        const productPrice = productCard.querySelector('.product-price').textContent;
        
        // Show loading state
        button.innerHTML = '<span class="loading-spinner"></span> Adding...';
        button.disabled = true;

        // Simulate API call
        setTimeout(() => {
            // Reset button
            button.innerHTML = 'Add to Cart';
            button.disabled = false;
            
            // Show success message
            showNotification('Product added to cart!', 'success');
            
            // Update cart count
            updateCartCount();
            
            // Add bounce animation to cart icon
            const cartIcon = document.querySelector('.cart-icon');
            if (cartIcon) {
                cartIcon.classList.add('bounce');
                setTimeout(() => {
                    cartIcon.classList.remove('bounce');
                }, 600);
            }
        }, 1000);
    }

    // Quick view modal
    function showQuickView(productCard) {
        const productData = {
            id: productCard.dataset.productId,
            name: productCard.querySelector('.product-title').textContent,
            price: productCard.querySelector('.product-price').textContent,
            image: productCard.querySelector('.product-image img').src,
            description: productCard.dataset.description || 'No description available.'
        };

        // Create modal HTML
        const modalHTML = `
            <div class="quick-view-modal" id="quickViewModal">
                <div class="modal-overlay"></div>
                <div class="modal-content">
                    <button class="modal-close">&times;</button>
                    <div class="row">
                        <div class="col-md-6">
                            <img src="${productData.image}" alt="${productData.name}" class="img-fluid">
                        </div>
                        <div class="col-md-6">
                            <h3>${productData.name}</h3>
                            <p class="price">${productData.price}</p>
                            <p class="description">${productData.description}</p>
                            <button class="btn btn-organic add-to-cart" data-product-id="${productData.id}">
                                Add to Cart
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;

        // Add modal to page
        document.body.insertAdjacentHTML('beforeend', modalHTML);
        
        const modal = document.getElementById('quickViewModal');
        const closeBtn = modal.querySelector('.modal-close');
        const overlay = modal.querySelector('.modal-overlay');
        
        // Show modal
        setTimeout(() => {
            modal.classList.add('show');
        }, 10);

        // Close modal handlers
        function closeModal() {
            modal.classList.remove('show');
            setTimeout(() => {
                modal.remove();
            }, 300);
        }

        closeBtn.addEventListener('click', closeModal);
        overlay.addEventListener('click', closeModal);
        
        // Handle add to cart in modal
        const modalAddToCartBtn = modal.querySelector('.add-to-cart');
        modalAddToCartBtn.addEventListener('click', function() {
            handleAddToCart(this);
        });
    }

    // Wishlist toggle
    function toggleWishlist(button) {
        const isActive = button.classList.contains('active');
        
        if (isActive) {
            button.classList.remove('active');
            button.innerHTML = '<i class="far fa-heart"></i>';
            showNotification('Removed from wishlist', 'info');
        } else {
            button.classList.add('active');
            button.innerHTML = '<i class="fas fa-heart"></i>';
            showNotification('Added to wishlist!', 'success');
        }
    }

    // Search function
    function performSearch(query) {
        // This would typically make an API call to your search endpoint
        console.log('Searching for:', query);
        
        // Simulate search results
        const searchResults = document.querySelector('.search-results');
        if (searchResults) {
            searchResults.innerHTML = `
                <div class="search-result-item">
                    <img src="/assets/webshop_ui/images/product-placeholder.jpg" alt="Product">
                    <div class="result-info">
                        <h6>Search result for "${query}"</h6>
                        <p class="price">$12.99</p>
                    </div>
                </div>
            `;
            searchResults.style.display = 'block';
        }
    }

    // Update cart count
    function updateCartCount() {
        const cartCount = document.querySelector('.cart-count');
        if (cartCount) {
            // This would typically get the count from your cart system
            const currentCount = parseInt(cartCount.textContent) || 0;
            cartCount.textContent = currentCount + 1;
            
            if (currentCount === 0) {
                cartCount.style.display = 'inline-block';
            }
        }
    }

    // Update cart item
    function updateCartItem(input) {
        const quantity = parseInt(input.value);
        const cartItem = input.closest('.cart-item');
        const itemId = cartItem.dataset.itemId;
        
        // This would typically make an API call to update the cart
        console.log(`Updating item ${itemId} to quantity ${quantity}`);
    }

    // Show notification
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <span>${message}</span>
            <button class="notification-close">&times;</button>
        `;

        // Add to page
        document.body.appendChild(notification);

        // Show notification
        setTimeout(() => {
            notification.classList.add('show');
        }, 10);

        // Auto hide after 3 seconds
        setTimeout(() => {
            hideNotification(notification);
        }, 3000);

        // Close button handler
        const closeBtn = notification.querySelector('.notification-close');
        closeBtn.addEventListener('click', () => {
            hideNotification(notification);
        });
    }

    // Hide notification
    function hideNotification(notification) {
        notification.classList.remove('show');
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }

    // Utility functions
    window.OrganicTheme = {
        showNotification,
        handleAddToCart,
        toggleWishlist,
        updateCartCount
    };

})();