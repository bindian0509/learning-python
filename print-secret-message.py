import requests
from bs4 import BeautifulSoup


def print_secret_message(url):
    html = requests.get(url, timeout=30).text

    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text("\n")

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    # Find start of data
    start = None
    for i, line in enumerate(lines):
        if line == "x-coordinate":
            start = i + 3
            break

    if start is None:
        raise ValueError("Could not locate data table")

    entries = []

    i = start
    while i + 2 < len(lines):
        try:
            x = int(lines[i])
            ch = lines[i + 1]
            y = int(lines[i + 2])

            entries.append((x, y, ch))
            i += 3

        except ValueError:
            i += 1

    max_x = max(x for x, _, _ in entries)
    max_y = max(y for _, y, _ in entries)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, ch in entries:
        grid[y][x] = ch

    for row in grid:
        print("".join(row))


print_secret_message(
    "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
)
