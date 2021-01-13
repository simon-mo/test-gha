import requests
import os

sha = os.environ["GITHUB_SHA"]
resp = requests.get("https://api.github.com/repos/ray-project/ray/commits/{}/check-suites".format(sha))
data = resp.json()
for check in data["check_suites"]:
    slug = check["app"]["slug"]
    if slug == "github-actions":
        run_url = check["check_runs_url"]
        html_url = requests.get(run_url).json()["check_runs"][0]["html_url"]
        print(html_url)

