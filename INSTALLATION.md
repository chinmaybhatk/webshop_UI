# Installation and Configuration Guide

## Overview

This custom Frappe webshop UI provides an organic/natural theme based on modern fruit and vegetable store templates. It's designed specifically for Frappe v15 and is compatible with FrappeCloud.

## Quick Installation

### Method 1: Direct Installation from GitHub

1. **Clone the repository to your Frappe bench apps directory:**
```bash
cd ~/frappe-bench/apps
git clone https://github.com/chinmaybhatk/webshop_UI.git
```

2. **Install the app:**
```bash
cd ~/frappe-bench
bench install-app webshop_ui
```

3. **Apply to your site:**
```bash
bench --site your-site-name install-app webshop_ui
```

4. **Build and restart:**
```bash
bench build
bench restart
```

### Method 2: Using bench get-app

```bash
cd ~/frappe-bench
bench get-app https://github.com/chinmaybhatk/webshop_UI.git
bench --site your-site-name install-app webshop_ui
bench build
bench restart
```

## Configuration

### 1. Enable Webshop

Make sure your site has webshop enabled:

```bash
bench --site your-site-name execute "frappe.db.set_value('Website Settings', None, 'enable_shopping_cart', 1)"
```

### 2. Set Homepage

Set the custom homepage as your site's default:

1. Go to **Website Settings** in your Frappe desk
2. Set **Home Page** to: `home`
3. Save the settings

### 3. Upload Brand Assets

1. **Logo**: Upload your organic store logo
   - Go to **Website Settings**
   - Upload your logo in **Brand Logo** field
   - Set **Brand Name** to your store name

2. **Product Images**: Upload category and product images
   - Recommended size: 800x600px for products
   - Use high-quality images of fresh produce

### 4. Configure Categories

1. Create **Item Groups** for your product categories:
   - Fruits
   - Vegetables  
   - Herbs
   - Organic Grains
   - Dairy Products

2. Add category images for better visual appeal

### 5. Setup Products

1. Create **Items** with:
   - Attractive product names
   - High-quality images
   - Detailed descriptions
   - Proper categorization
   - Pricing information

2. Enable **Published** checkbox for items to appear on website

## Customization

### Theme Colors

The organic theme uses these primary colors:
- **Primary Green**: #4CAF50
- **Secondary Green**: #8BC34A  
- **Accent Orange**: #FF9800
- **Earth Brown**: #795548
- **Cream White**: #FFF8E1

To customize colors, edit: `webshop_ui/public/css/organic-theme.css`

### Fonts

The theme uses:
- **Primary Font**: Inter (system font)
- **Heading Font**: Playfair Display (serif)

### Homepage Sections

You can customize homepage sections by editing:
`webshop_ui/templates/pages/home.html`

Available sections:
- Hero section with call-to-action
- Product categories grid
- Featured products
- Benefits/features
- Customer testimonials
- Newsletter signup

### Navigation Menu

Customize the navigation by editing:
`webshop_ui/templates/includes/navbar.html`

### Footer

Customize footer content by editing:
`webshop_ui/templates/includes/footer.html`

## FrappeCloud Deployment

### Before Deployment

1. **Test locally** to ensure everything works
2. **Optimize images** for web (compress/resize)
3. **Check responsive design** on different devices

### Deployment Steps

1. **Push to GitHub** (already done)
2. **In FrappeCloud dashboard:**
   - Go to your site
   - Navigate to **Apps** section
   - Click **Install App**
   - Enter: `https://github.com/chinmaybhatk/webshop_UI.git`
   - Click **Install**

3. **Configure after installation:**
   - Set homepage to `home`
   - Upload brand assets
   - Configure categories and products

## Advanced Configuration

### Custom CSS/JS

Add custom styles to:
- `webshop_ui/public/css/organic-theme.css`

Add custom JavaScript to:
- `webshop_ui/public/js/organic-theme.js`

### Template Overrides

The app overrides these default templates:
- **Navbar**: `templates/includes/navbar.html`
- **Footer**: `templates/includes/footer.html`
- **Homepage**: `templates/pages/home.html`

### Adding New Templates

1. Create new template in: `webshop_ui/templates/pages/`
2. Add route in `hooks.py` if needed
3. Build and restart: `bench build && bench restart`

## Troubleshooting

### Common Issues

1. **App not installing:**
   ```bash
   bench --site your-site-name list-apps
   ```
   If not listed, try:
   ```bash
   bench --site your-site-name reinstall
   ```

2. **Styles not loading:**
   ```bash
   bench build --hard
   bench restart
   ```

3. **Templates not updating:**
   ```bash
   bench clear-cache
   bench restart
   ```

### Getting Help

- Check Frappe documentation: https://frappeframework.com
- Visit Frappe Community: https://discuss.frappe.io
- Review error logs: `bench logs`

## Features Included

### ✅ Frontend Features
- Modern, responsive design
- Organic/natural color scheme
- Product showcase with hover effects
- Category navigation
- Search functionality
- Shopping cart integration
- User account management
- Mobile-optimized design

### ✅ Backend Integration
- Frappe v15 compatibility
- Website Settings integration
- Item and Item Group support
- Shopping Cart functionality
- User authentication
- Order management

### ✅ Performance
- Optimized CSS and JavaScript
- Lazy loading for images
- Mobile-first responsive design
- Fast loading animations
- SEO-friendly structure

## Support

For issues specific to this theme, please create an issue on the GitHub repository:
https://github.com/chinmaybhatk/webshop_UI/issues

---

*Made with ❤️ for organic food lovers and Frappe developers*