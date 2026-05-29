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
    Obtiene información del problema usando GraphQL.
    """

    query = """
    query selectProblem($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
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
    Genera:
    3121-count-the-number-of-special-characters-ii
    """

    return f"{question_id}-{title_slug}"


def generate_markdown(problem_data: dict, original_url: str) -> str:
    """
    Genera el markdown completo.
    """

    question_id = problem_data["questionId"]
    title = problem_data["title"]
    title_slug = problem_data["titleSlug"]
    difficulty = problem_data["difficulty"]
    content = problem_data["content"]

    markdown = f"""<h1>{question_id} - {title}</h1>
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
            problem_data["questionId"],
            problem_data["titleSlug"]
        )

        markdown = generate_markdown(problem_data, url)

        print("\nGenerated filename:")
        print(filename)

        output_file = f"{filename}.md"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"\nMarkdown saved to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
