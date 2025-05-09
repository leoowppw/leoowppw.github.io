html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Chinese Migration to the U.S. (1880–1945)</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }
        h1 { color: darkred; }
        h2 { margin-top: 30px; }
        p { max-width: 700px; }
    </style>
</head>
<body>
    <h1>Chinese Migration to the U.S. (1880–1945)</h1>
    <p>This page provides a decade-by-decade overview of Chinese migration to the United States, highlighting key events and legislation that shaped this migration.</p>
"""

migration_events = {
    "1880s": "In 1882, the U.S. Congress passed the Chinese Exclusion Act, suspending Chinese labor immigration. This marked the first significant restriction of free immigration in U.S. history.",
    "1890s": "Chinese immigrants faced violence and exclusion. Communities like San Francisco's Chinatown survived despite increasing restrictions.",
    "1900s": "The 1906 San Francisco earthquake led to destroyed birth records, enabling some Chinese immigrants to claim U.S. birth and bring 'paper sons'.",
    "1910s": "The Angel Island Immigration Station was opened in 1910 to enforce exclusion laws. Many Chinese immigrants were detained and interrogated there.",
    "1920s": "The Immigration Act of 1924 further restricted Asian immigration. Chinese communities remained mostly male due to bans on family reunification.",
    "1930s": "The Great Depression worsened discrimination. Few new Chinese migrants arrived, but second-generation Chinese Americans began organizing socially and politically.",
    "1940s": "In 1943, the Chinese Exclusion Act was repealed during WWII as China was a U.S. ally. However, immigration was still limited to 105 people per year until 1965."
}

for decade, summary in migration_events.items():
    html_content += f"<h2>{decade}</h2>\n<p>{summary}</p>\n"

html_content += """
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ index.html has been created!")
with open("index.html", "w", encoding="utf-8") as f:
 f.write("<h1>Chinese Migration to the U.S. (1880–1945)</h1>")
print("✅ index.html has been created!")
print("✅ index.html has been created!")

