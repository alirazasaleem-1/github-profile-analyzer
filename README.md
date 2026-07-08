# 📊 GitHub Profile Analyzer

A Python project that analyzes a GitHub user's public profile using the GitHub API and provides useful insights such as programming languages, contribution graph, coding streak, top repositories, and personalized learning suggestions.

---

## ✨ Features

* ✅ Validates GitHub usernames and profile URLs
* 🌐 Checks whether the GitHub account actually exists
* 💻 Displays programming languages used across repositories
* 📈 Generates the user's GitHub contribution graph link
* 🔥 Fetches current and longest contribution streak
* ⭐ Lists the top 3 repositories based on stars
* 🤖 Provides AI-powered learning suggestions based on the user's primary programming language

---

## 📂 Project Structure

```text
GitHub-Profile-Analyzer/
│
├── main.py                      # Main application
├── validate_github_username.py  # Username validation module
└── README.md
```

---

## 🛠 Technologies Used

* Python 3
* Requests Library
* Regular Expressions (Regex)
* GitHub REST API
* GitHub Readme Streak Stats API

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/github-profile-analyzer.git
```

Move into the project folder:

```bash
cd github-profile-analyzer
```

Install the required package:

```bash
pip install requests
```

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

Example:

```text
Enter your GitHub username:

torvalds
```

or

```text
https://github.com/torvalds
```

The program will automatically validate the input and display the analysis.

---

## 📊 Output

The analyzer provides:

### 1. Languages Used

Example:

```text
Python Used in 12 repo(s)
JavaScript Used in 7 repo(s)
HTML Used in 5 repo(s)
```

---

### 2. Contribution Graph

Outputs the user's contribution graph URL:

```text
https://github.com/users/USERNAME/contributions
```

---

### 3. GitHub Streak

Displays:

* Current contribution streak
* Longest contribution streak

Example:

```text
Current Streak: 18 days
Longest Streak: 103 days
```

---

### 4. Top Repositories

Ranks repositories by GitHub stars.

Example:

```text
1. AwesomeProject (152⭐)
2. Portfolio (97⭐)
3. AutomationScripts (61⭐)
```

---

### 5. AI Suggestions

Provides learning recommendations based on the user's most-used language.

Example:

For Python developers:

* Build Flask applications
* Learn FastAPI
* Create automation projects

---

## 🧠 How It Works

### Username Validation

The project first validates the GitHub username using a regular expression.

It also accepts full GitHub profile URLs and extracts the username automatically.

Example:

```text
https://github.com/octocat
```

becomes

```text
octocat
```

---

### Profile Verification

After validating the format, the application sends a request to the GitHub API to verify that the user actually exists.

---

### Repository Analysis

The program retrieves up to **100 public repositories** and analyzes:

* Repository languages
* Star counts
* Repository URLs

---

### Streak Analysis

The project uses the GitHub Readme Streak Stats API to fetch:

* Current streak
* Longest streak

---

## ⚠️ Error Handling

The project safely handles:

* Invalid usernames
* Invalid GitHub URLs
* Network failures
* API errors
* Users with no repositories
* Unexpected API responses

---

## 🚀 Future Improvements

* Repository statistics dashboard
* Charts and graphs
* Commit activity analysis
* Fork and issue statistics
* README quality analyzer
* Export report as PDF
* AI-generated GitHub profile feedback
* Streamlit web interface
* GUI version
* OpenAI-powered repository recommendations

---

## 👨‍💻 Author

**Ali Raza**

BS Computer Science Student

Passionate about Python, Automation, AI, and building real-world projects.

---

## 📄 License

This project is open source and available under the MIT License.
