import requests
 

from bs4 import BeautifulSoup
 

import csv
 

import os
 


 

def scrape_jobs(html_content):
 

    """
 

    Scrape job information from the HTML content using Beautiful Soup
 

    """
 

    # Parse the HTML content
 

    soup = BeautifulSoup(html_content, 'html.parser')
 

    
 

    # Find all job listings
 

    job_cards = soup.find_all('div', class_='job-card')
 

    
 

    jobs = []
 

    
 

    # Extract information from each job card
 

    for job in job_cards:
 

        # Extract basic job details
 

        title = job.find('h3').text.strip()
 

        company = job.find('div', class_='company').text.strip()
 

        location = job.find('div', class_='location').text.strip()
 

        salary = job.find('div', class_='salary').text.strip()
 

        date_posted = job.find('div', class_='date').text.strip()
 

        description = job.find('p').text.strip()
 

        
 

        # Extract job ID from data attribute
 

        job_id = job.get('data-id')
 

        
 

        # Extract tags
 

        tags_elements = job.find_all('span', class_='tag')
 

        tags = [tag.text.strip() for tag in tags_elements]
 

        
 

        # Create a dictionary for this job
 

        job_info = {
 

            'id': job_id,
 

            'title': title,
 

            'company': company,
 

            'location': location,
 

            'salary': salary,
 

            'date_posted': date_posted,
 

            'description': description,
 

            'tags': ', '.join(tags)
 

        }
 

        
 

        jobs.append(job_info)
 

    
 

    return jobs
 


 

def save_to_csv(jobs, filename='scraped_jobs.csv'):
 

    """
 

    Save the scraped job data to a CSV file
 

    """
 

    # Define the CSV columns
 

    fieldnames = ['id', 'title', 'company', 'location', 'salary', 'date_posted', 'description', 'tags']
 

    
 

    # Write to CSV
 

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
 

        writer = csv.DictWriter(file, fieldnames=fieldnames)
 

        writer.writeheader()
 

        writer.writerows(jobs)
 

    
 

    print(f"Successfully saved {len(jobs)} jobs to {filename}")
 


 

def main():
 

    """
 

    Main function to run the scraper
 

    """
 

    # In real scraping, you would use:
 

    # url = "https://example-job-site.com/jobs"
 

    # response = requests.get(url)
 

    # html_content = response.text
 

    
 

    # For our dummy website, we'll read from a local HTML file
 

    html_file = "dummy_jobs.html"  # Save the HTML content to this file
 

    
 

    if os.path.exists(html_file):
 

        with open(html_file, 'r', encoding='utf-8') as file:
 

            html_content = file.read()
 

    else:
 

        print(f"Please save the HTML content to {html_file} first")
 

        return
 

    
 

    # Scrape jobs from the HTML content
 

    jobs = scrape_jobs(html_content)
 

    
 

    # Print summary of scraped data
 

    print(f"Scraped {len(jobs)} job listings")
 

    for i, job in enumerate(jobs, 1):
 

        print(f"{i}. {job['title']} at {job['company']} - {job['location']}")
 

    
 

    # Save data to CSV
 

    save_to_csv(jobs)
 


 

if __name__ == "__main__":
 

    main()