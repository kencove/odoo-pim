{
    "name": "Product Catalog",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Kencove, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/odoo-pim",
    "depends": [
        "web",
        "product",
        "sale",
    ],
    "data": [
        "views/sale_order_views.xml",
        "views/product_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "product_catalog/static/src/product_catalog/search/search_panel.xml",
            "product_catalog/static/src/product_catalog/search/search_panel.js",
            "product_catalog/static/src/product_catalog/kanban_model.js",
            "product_catalog/static/src/product_catalog/kanban_view.js",
        ],
    },
    "installable": True,
    "application": True,
}
