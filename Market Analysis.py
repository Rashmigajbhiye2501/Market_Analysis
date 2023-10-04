# Define data for five products and three companies
products = {
    "Laptop": {
        "Companies": {
            "Company ABC": {
                "Revenue (in millions)": 100,
                "Growth Rate (%)": 8,
            },
            "Company XYZ": {
                "Revenue (in millions)": 80,
                "Growth Rate (%)": 6,
            },
            "Company CBS": {
                "Revenue (in millions)": 150,
                "Growth Rate (%)": 9,
            },
        },
    },
    "Tablet": {
        "Companies": {
            "Company ABC": {
                "Revenue (in millions)": 150,
                "Growth Rate (%)": 5,
            },
            "Company XYZ": {
                "Revenue (in millions)": 100,
                "Growth Rate (%)": 4,
            },
            "Company CBS": {
                "Revenue (in millions)": 150,
                "Growth Rate (%)": 1,
            },
        },
    },
    "MacBook": {
        "Companies": {
            "Company ABC": {
                "Revenue (in millions)": 80,
                "Growth Rate (%)": 4,
            },
            "Company XYZ": {
                "Revenue (in millions)": 120,
                "Growth Rate (%)": 7,
            },
            "Company CBS": {
                "Revenue (in millions)": 100,
                "Growth Rate (%)": 3,
            },
        },
    },
    "iPhone": {
        "Companies": {
            "Company ABC": {
                "Revenue (in millions)": 60,
                "Growth Rate (%)": 3,
            },
            "Company XYZ": {
                "Revenue (in millions)": 90,
                "Growth Rate (%)": 5,
            },
            "Company CBS": {
                "Revenue (in millions)": 120,
                "Growth Rate (%)": 6,
            },
        },
    },
    "Mobile": {
        "Companies": {
            "Company ABC": {
                "Revenue (in millions)": 120,
                "Growth Rate (%)": 6,
            },
            "Company XYZ": {
                "Revenue (in millions)": 80,
                "Growth Rate (%)": 4,
            },
            "Company CBS": {
                "Revenue (in millions)": 70,
                "Growth Rate (%)": 2,
            },
        },
    },
}

# Calculate the total market size for each product
product_market_sizes = {}
for product_name, product_data in products.items():
    total_revenue = sum(company_data["Revenue (in millions)"] for company_data in product_data["Companies"].values())
    product_market_sizes[product_name] = total_revenue

# Calculate the market share percentage and growth rate for each product in each company
for product_name, product_data in products.items():
    for company_name, company_data in product_data["Companies"].items():
        total_revenue = product_market_sizes[product_name]
        market_share = (company_data["Revenue (in millions)"] / total_revenue) * 100
        company_data["Market Share (%)"] = market_share

# Display the product-wise market analysis results across companies
print("Product-wise Market Analysis for Five Products Across Three Companies:")
print("{:<12} {:<12} {:<20} {:<20} {:<20}".format("Product", "Company", "Revenue (in millions)", "Market Share (%)", "Growth Rate (%)"))
for product_name, product_data in products.items():
    for company_name, company_data in product_data["Companies"].items():
        print("{:<12} {:<12} {:<20} {:<20.2f} {:<20}".format(
            product_name,
            company_name,
            company_data["Revenue (in millions)"],
            company_data["Market Share (%)"],
            company_data["Growth Rate (%)"]
        ))
