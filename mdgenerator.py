from pathlib import Path
from datetime import datetime
import re
import requests


LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"


def validate_leetcode_url(url: str) -> str:
    """
    Validated leetcode url and gets the title 
    """

    pattern = r"^https?://(www\.)?leetcode\.com/problems/([a-z0-9\-]+)/?"

    match = re.match(pattern, url)

    if not match:
        raise ValueError("Invalid LeetCode problem URL")

    return match.group(2)


def fetch_problem_data(title_slug: str) -> dict:
    """
    Get problem info from leetcode graphql
    """

    query = """
    query selectProblem($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        titleSlug
        difficulty
        content
      }
    }
    """

    variables = {
        "titleSlug": title_slug
    }

    response = requests.post(
        LEETCODE_GRAPHQL_URL,
        json={
            "query": query,
            "variables": variables
        }
    )

    response.raise_for_status()

    data = response.json()

    question = data["data"]["question"]

    if question is None:
        raise ValueError("Problem not found")

    return question


def generate_problem_filename(question_id: str, title_slug: str) -> str:
    """
    Generates:
    number-title_slug
    """

    return f"{question_id}-{title_slug}"


def generate_markdown(problem_data: dict, original_url: str) -> str:
    """
    Get markdown
    """

    question_frontend_id = problem_data["questionFrontendId"]
    title = problem_data["title"]
    title_slug = problem_data["titleSlug"]
    difficulty = problem_data["difficulty"]
    content = problem_data["content"]

    markdown = f"""<h1>{question_frontend_id} - {title}</h1>
<h2>Difficulty: {difficulty} - <a href="{original_url}">{title_slug}</a></h2> 

{content} 
"""

    return markdown


def main():
    url = input("LeetCode URL: ").strip()

    try:
        title_slug = validate_leetcode_url(url)

        problem_data = fetch_problem_data(title_slug)

        filename = generate_problem_filename(
            problem_data["questionFrontendId"],
            problem_data["titleSlug"]
        )

        markdown = generate_markdown(problem_data, url)

        print("\nGenerated filename:")
        print(filename)

        output_dir = Path("./Solutions", filename)
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = Path(output_dir, f"{filename}.md")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"\nMarkdown saved to: {output_file}")

        # Archivo Accepted - YYYY-MM-DD
        today = datetime.now().strftime("%Y-%m-%d")
        accepted_file = Path(output_dir, f"Accepted - {today}.py")
        accepted_file.touch(exist_ok=True)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
