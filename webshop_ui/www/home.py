import frappe
from frappe import _
from frappe.website.page_renderers.template_page import TemplatePage


def get_context(context):
    """Get context for organic webshop homepage"""
    
    # Set page metadata
    context.title = _("Fresh Organic Products Delivered")
    context.description = _(
        "Discover the finest selection of organic fruits, vegetables, and natural products. "
        "Sourced directly from local farms, delivered fresh to your doorstep."
    )
    
    # Get featured categories
    context.categories = get_featured_categories()
    
    # Get featured products
    context.featured_products = get_featured_products()
    
    # Brand information
    website_settings = frappe.get_cached_doc("Website Settings")
    context.brand_name = website_settings.brand_name or "Organic Store"
    context.brand_logo = website_settings.brand_logo
    
    return context


def get_featured_categories():
    """Get featured product categories for homepage display"""
    try:
        categories = frappe.get_all(
            "Item Group",
            filters={
                "is_group": 0,  # Get leaf categories only
                "show_in_website": 1
            },
            fields=["name", "route", "image", "description"],
            limit=6,
            order_by="weightage desc, name asc"
        )
        
        # Add item count for each category
        for category in categories:
            category.item_count = frappe.db.count(
                "Item",
                filters={
                    "item_group": category.name,
                    "published": 1,
                    "disabled": 0
                }
            )
            
        return categories
    except Exception:
        return []


def get_featured_products():
    """Get featured products for homepage display"""
    try:
        # Get items that are featured or have high weightage
        products = frappe.get_all(
            "Item",
            filters={
                "published": 1,
                "disabled": 0,
                "has_variants": 0
            },
            fields=[
                "name", "item_name", "route", "website_image", 
                "formatted_price", "description", "item_group"
            ],
            limit=8,
            order_by="weightage desc, modified desc"
        )
        
        # Add additional product info
        for product in products:
            product.web_item_name = product.item_name
            
            # Add rating (placeholder - you can integrate with actual rating system)
            product.rating = 4.5
            product.rating_count = frappe.utils.random.randint(10, 100)
            
        return products
    except Exception:
        return []
