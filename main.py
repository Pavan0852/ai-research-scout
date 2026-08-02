from app.services.scout_service import generate_daily_digest

response = generate_daily_digest(
    max_results=5,
)

digest = response.digest

print("=" * 80)
print("🔥 SCOUTAI DAILY")
print("=" * 80)

print(f"\n📅 {digest.date}")
print(f"⭐ Research Score : {digest.research_score}/5")
print(f"📊 Total Research : {digest.total_items}")

print("\n📝 Overview")
print(digest.overview)

print("\n📈 Trends")

for trend in digest.top_trends:
    print(f"• {trend.topic}")
    print(f"  {trend.description}")

print("\n🏆 Biggest Breakthrough")
print(digest.biggest_breakthrough.title)

print("\n📄 Featured Papers")

for paper in digest.featured_papers:
    print(f"• {paper.title}")

print("\n🚀 Featured Repositories")

for repo in digest.featured_repositories:
    print(f"• {repo.title}")

print("\n💡 Key Takeaways")

for takeaway in digest.key_takeaways:
    print(f"• {takeaway}")