from requests import get

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

response = get(f"https://www.indeed.com/jobs?q=python&limit=50")

print(response.status_code)
print(response.text)

# if response.status_code != 200:
#     print("Cant request page")
# else:
#     print(response.text)
