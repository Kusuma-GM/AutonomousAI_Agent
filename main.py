from ai_news_fetcher import fetch_ai_news
from review_handler import extract_smartphone_reviews
from report_generator import generate_renewable_energy_report

def handle_instruction(instruction):
    instruction = instruction.lower()

    if "fetch ai news" in instruction or "ai headlines" in instruction:
        fetch_ai_news()

    elif "smartphone reviews" in instruction or "extract pros/cons" in instruction:
        extract_smartphone_reviews()

    elif "renewable energy" in instruction or "create pdf" in instruction:
        generate_renewable_energy_report()

    else:
        print("❓ Unknown command. Try 'fetch ai news', 'smartphone reviews', or 'renewable energy report'.")

if __name__ == "__main__":
    print(">>")
    while True:
        user_input = input("\nEnter your instruction:\n> ")
        handle_instruction(user_input)
