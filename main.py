# Github Profile Analyzer
from validate_github_username import verify_github_user
import requests 
import re 
import traceback 

print("Welcome to Ali's Github Profile Analyzer")

print('''After entering username: You'll get these four things:
      1. Languages Used
      2. Contribution Graph
      3. Longest Streak
      4. Top repositories
      5. AI suggestions ''')


def clean_username(username): 
    if "github.com/" in username:
        username = username.split("github.com/")[-1].strip("/")
    return username 

username = input("Enter your github username: ")
username = clean_username(username)

if verify_github_user(username):
    print("Username verified successfully! Fetching Data....")

    repos_url = f"https://api.github.com/users/{username}/repos?per_page=100"
    streak_url = f"https://github-readme-streak-stats-five.vercel.app/api?user={username}&type=json"

    try:
        response = requests.get(repos_url, timeout = 5)
        repos_data = response.json()

        if response.status_code != 200:
            print("GitHub API Error:", response.json().get("message"))
            exit()
        if not isinstance(repos_data, list):
            print("Unexpected response from GitHub:")
            print(repos_data)
            exit()

        if not repos_data:
            print("This user has no repositories to analyze! ")
        else:
            # Feature 1 and 2
            languages_count = {}
            top_repos = []

            for repo in repos_data:
                # Track languages
                lang = repo.get("language")
                if lang:
                    languages_count[lang] = languages_count.get(lang, 0) + 1

                top_repos.append({
                    "name": repo["name"],
                    "stars": repo["stargazers_count"],
                    "url" : repo["html_url"]
                })
            
            if languages_count:
                top_language = max(languages_count, key=languages_count.get)
            else:
                top_language = None 
            top_repos = sorted(top_repos, key = lambda x: x['stars'], reverse=True)[:3]

            # Display Feature 1: Languages used
            print("\n1. LANGUAGES USE: ")
            for lang, count in languages_count.items():
                print(f"    - {lang} Used in {count} repo(s)")
            
            # Display Feature 2: Contribution graph URL
            print("\n2. Contribution graph URL")
            graph_url = f"https://github.com/users/{username}/contributions"
            print(graph_url)

            # Feature 3: Longest Streak
            print("\n3. Longest Streak: ")
            try:
                # We fetch the streak data right when we need it, safely isolated
                # Fetch clean JSON data instead of an image
                streak_data = requests.get(streak_url, timeout=5).json()
                
                # Directly extract the values using dictionary keys!
                current = streak_data["currentStreak"]["length"]
                longest = streak_data["longestStreak"]["length"]
                
                print(f"Current Streak: {current} days")
                print(f"Longest Streak: {longest} days")
            except Exception:
                print("Could not fetch streak details right now. Skipping safely!")


            # Display Feature 4: Top Repositories
            print("\n4. TOP REPOSITORIES: ")
            for i, repo in enumerate(top_repos, 1):
                print(f"    {i}. {repo['name']} ({repo['stars']} stars) -> {repo['url']}")
            
            # Feature 5: AI Suggestions
            print("\n5. AI Suggestions: ")
            if top_language == "JavaScript":
                print("- Learn React")
                print("- Build Full Stack Apps")

            elif top_language == "Python":
                print("- Build Flask Apps")
                print("- Learn FastAPI")
                print("- Start Automation Projects")
            
            elif top_language == "Java":
                print("- Learn Spring Boot")
            
            else:
                print("Can't find languages")
    except Exception:
        traceback.print_exc()
                
