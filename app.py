# YouTube SEO AI Agent Engine
# Created for Tech with Prince Hub

def generate_seo_package(topic_name):
    clean_topic = topic_name.strip().title()
    
    seo_data = {
        "title": f"Master {clean_topic} Step by Step | Complete Hindi Guide (2026)",
        "description": f"Welcome to Tech with Prince Hub! In this video, we cover complete details about {clean_topic}. Watch till the end to master it easily.",
        "tags": f"{clean_topic}, {clean_topic} tutorial, {clean_topic} in hindi, learn {clean_topic}",
        "hashtags": f"#{clean_topic.replace(' ', '')} #TechWithPrinceHub #LearnInHindi"
    }
    return seo_data

if __name__ == "__main__":
    print("=== YouTube SEO AI Agent ===")
    user_input = input("Enter video topic: ")
    result = generate_seo_package(user_input)
    print("\n[Generated Title]:", result["title"])
    print("[Generated Tags]:", result["tags"])
