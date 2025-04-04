from file_handler import save_to_file

def extract_smartphone_reviews():
    print("🔍 Fetching smartphone reviews...")

    reviews = """
Smartphone: iPhone 15 Pro
Pros:
- Excellent camera quality
- Smooth 120Hz display
- Powerful A17 Bionic chip

Cons:
- Expensive price
- No major design changes

Smartphone: Samsung Galaxy S24 Ultra
Pros:
- Amazing zoom camera
- Large battery life
- Stylus support

Cons:
- Bulky design
- Expensive pricing
    """.strip()

    save_to_file("output/smartphone_reviews.txt", reviews)
    print("✅ Reviews saved to 'output/smartphone_reviews.txt'")
