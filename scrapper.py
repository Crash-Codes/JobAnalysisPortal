
from bs4 import BeautifulSoup

# Set up the URL for the job search page
url = "https://www.linkedin.com/jobs/search/?keywords=software%20engineer&location=San%20Francisco%20Bay%20Area&locationId=us%3A3405524&f_TPR=r81C1000000LQsxQAC&position=1&pageNum=0"

# Make an HTTP request to the URL
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the job listings data
job_listings = []
for div in soup.find_all("div", class_="job-card-container"):
    title = div.find("a", class_="job-card-list__title").text.strip()
    company = div.find("h4", class_="job-card-list__company").text.strip()
    location = div.find("div", class_="job-card-list__location").text.strip()
    summary = div.find("div", class_="job-card-list__snippet").text.strip()
    date = div.find("time")["datetime"]
    source = "LinkedIn"
    job_listings.append({"title": title, "company": company, "location": location, "summary": summary, "date": date, "source": source})

# Print the extracted job listings data
for job_listing in job_listings:
    print(job_listing)
