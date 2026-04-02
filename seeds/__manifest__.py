{
    "name": "Seeds",
    "category": "Uncategorized",
    "author": "MuchachosDev",
    "application": True,
    "version": "19.0.1.0.0",
    "summary": "A small and simple module to manage and track seed tests",
    "depends": ["base", "mail"],
    "data": [
        # Security
        "security/security.xml",
        "security/ir.model.access.csv",
        # Views
        "views/seed_destinatary_view.xml",
        "views/seed_arrival_order_view.xml",
        "views/seed_company_view.xml",
        "views/seed_deperture_order_view.xml",
        "views/seed_hibrid_view.xml",
        "views/seed_result_order_view.xml",
        "views/seed_result_order_item_view.xml",
        "views/seed_vegetable_view.xml",
        "views/menu.xml",
        # Reports
        "report/report_seed_deperture_order.xml",
        "report/report_seed_result_order.xml",
        # Pre-loaded data
        "data/sequence.xml",
        "data/vegetable.xml",
        "data/experimental_result_template.xml",
    ],
}
