import re
import requests
from pathlib import Path


USERNAME = "Chipes"
LEETCODE_SESSION = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiODYzODkwMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImMwMTNiNGZlM2M0MzM2ZTA1MWZmNmU5MGNiY2M2OGNhZDdmZTZkYzkwZDg1ZTQyZDhkNWJhZWFjNzNiNzAwNzIiLCJzZXNzaW9uX3V1aWQiOiI5NDVmM2FlMCIsImlkIjo4NjM4OTAzLCJlbWFpbCI6ImNhcmxvczEyMjdhQG91dGxvb2suY29tIiwidXNlcm5hbWUiOiJDaGlwZXMiLCJ1c2VyX3NsdWciOiJDaGlwZXMiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY4MzE2OTA5MS5wbmciLCJyZWZyZXNoZWRfYXQiOjE3ODczNTcxOTQsImlwIjoiMTg5LjE3OC4yNDQuODMiLCJpZGVudGl0eSI6IjZiMjIxYWQxYThiMGM2MGRmMThmODY4NmI0ODc2ODc4IiwiZGV2aWNlX3dpdGhfaXAiOlsiNTlmZmI3ODc0MTQxMWQ2YzE5NTQyNTc0NDc3MGQxZjEiLCIxODkuMTc4LjI0NC44MyJdfQ.__fDndavcLHCHXITrNfr5rYQ1t9-qMw5tnq2NPUUGGE"

REPO_PATH = Path(
    "C:/Users/Carlos/Documents/Code/LeetCode/Solutions/"
)

URL = "https://leetcode.com/graphql"


# ============================================================
# 1. Obtener problemas del repo
# ============================================================

def get_repo_problems():
    problems = {}

    for folder in REPO_PATH.iterdir():

        if not folder.is_dir():
            continue

        match = re.match(r"^(\d+)-(.+)$", folder.name)

        if not match:
            continue

        problem_id = int(match.group(1))
        folder_slug = match.group(2)

        problems[problem_id] = {
            "folder": folder,
            "slug": folder_slug,
        }

    return problems


# ============================================================
# 2. Obtener problemas de LeetCode
# ============================================================

def get_leetcode_problems(session):

    query = """
    query problemsetQuestionListV2(
        $limit: Int
        $skip: Int
        $filters: QuestionFilterInput
    ) {
        problemsetQuestionListV2(
            limit: $limit
            skip: $skip
            filters: $filters
        ) {
            questions {
                questionFrontendId
                title
                titleSlug
                status
            }
        }
    }
    """

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://leetcode.com/problemset/",
        "Cookie": f"LEETCODE_SESSION={session}",
    }

    problems = {}

    skip = 0
    limit = 100

    while True:

        variables = {
            "limit": limit,
            "skip": skip,
            "filters": {
                "filterCombineType": "ALL"
            }
        }

        response = requests.post(
            URL,
            json={
                "query": query,
                "variables": variables
            },
            headers=headers,
            timeout=30
        )

        if response.status_code != 200:
            print(response.text)
            response.raise_for_status()

        data = response.json()

        if "errors" in data:
            print(data["errors"])
            raise RuntimeError("Error GraphQL")

        questions = (
            data["data"]
            ["problemsetQuestionListV2"]
            ["questions"]
        )

        if not questions:
            break

        for question in questions:

            problem_id = int(
                question["questionFrontendId"]
            )

            problems[problem_id] = {
                "title": question["title"],
                "slug": question["titleSlug"],
                "status": question["status"],
            }

        print(
            f"Procesados: {skip + len(questions)}"
        )

        if len(questions) < limit:
            break

        skip += limit

    return problems


# ============================================================
# 3. Crear índice por slug
# ============================================================

def create_slug_index(leetcode):

    index = {}

    for problem_id, problem in leetcode.items():

        slug = problem["slug"]

        index[slug] = {
            "id": problem_id,
            "title": problem["title"],
            "slug": slug,
            "status": problem["status"],
        }

    return index


# ============================================================
# 4. Encontrar IDs incorrectos
# ============================================================

def find_corrections(repo, leetcode):

    slug_index = create_slug_index(leetcode)

    corrections = []

    for old_id, problem in repo.items():

        folder = problem["folder"]
        slug = problem["slug"]

        if slug not in slug_index:
            continue

        correct = slug_index[slug]
        new_id = correct["id"]

        if old_id == new_id:
            continue

        corrections.append({
            "old_id": old_id,
            "new_id": new_id,
            "title": correct["title"],
            "slug": slug,
            "folder": folder,
        })

    return corrections


# ============================================================
# 5. Mostrar correcciones
# ============================================================

def print_corrections(corrections):

    print()
    print("=" * 90)
    print("CORRECCIONES")
    print("=" * 90)

    if not corrections:
        print("\nNo se encontraron IDs incorrectos.")
        return

    for correction in sorted(
        corrections,
        key=lambda x: x["old_id"]
    ):

        print(
            f"{correction['old_id']:>5} -> "
            f"{correction['new_id']:<5} | "
            f"{correction['title']}"
        )

    print()
    print(f"Total de correcciones: {len(corrections)}")


# ============================================================
# 6. Renombrar carpetas
# ============================================================

def rename_folders(corrections):

    print()
    print("=" * 90)
    print("RENOMBRANDO CARPETAS")
    print("=" * 90)

    for correction in corrections:

        old_folder = correction["folder"]

        new_name = (
            f"{correction['new_id']}-"
            f"{correction['slug']}"
        )

        new_folder = old_folder.parent / new_name

        if new_folder.exists():
            print(
                f"SKIP: {old_folder.name} -> "
                f"{new_folder.name}"
            )
            print(
                "      La carpeta destino ya existe."
            )
            continue

        print(
            f"{old_folder.name} -> "
            f"{new_folder.name}"
        )

        old_folder.rename(new_folder)


# ============================================================
# MAIN
# ============================================================

repo = get_repo_problems()

leetcode = get_leetcode_problems(
    LEETCODE_SESSION
)

corrections = find_corrections(
    repo,
    leetcode
)

print_corrections(corrections)


# ============================================================
# IMPORTANTE:
# Primero ejecuta el script SIN esta línea.
#
# Cuando revises que las correcciones son correctas,
# descomenta:
#
# rename_folders(corrections)
# ============================================================