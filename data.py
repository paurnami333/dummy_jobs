import random
 

from datetime import datetime, timedelta
 

from typing import List, Dict, Any
 


 

def generate_jobs(num_jobs: int = 20) -> List[Dict[str, Any]]:
 

    """
 

    Generate realistic job listing data with error handling
 

    
 

    Args:
 

        num_jobs: Number of jobs to generate (default: 20)
 

        
 

    Returns:
 

        List of job dictionaries with consistent structure
 

    """
 

    if not isinstance(num_jobs, int) or num_jobs <= 0:
 

        raise ValueError("num_jobs must be a positive integer")
 


 

    job_titles = [
 

        "Frontend Developer", "Backend Engineer", "UX Designer", 
 

        "Data Scientist", "DevOps Engineer", "Product Manager",
 

        "Mobile Developer", "QA Engineer", "Security Specialist"
 

    ]
 

    
 

    companies = [
 

        "TechCorp", "DevSolutions", "DataWorks", 
 

        "CreativeMinds", "CloudNative", "ByteSystems"
 

    ]
 

    
 

    locations = [
 

        "Remote", "New York, NY", "San Francisco, CA", 
 

        "Austin, TX", "Boston, MA", "London, UK"
 

    ]
 

    
 

    tech_skills = [
 

        "JavaScript", "Python", "React", "AWS", "Docker", 
 

        "SQL", "NoSQL", "Kubernetes", "TypeScript", "GraphQL",
 

        "Machine Learning", "TensorFlow", "PyTorch", "Java", "Go"
 

    ]
 

    
 

    soft_skills = [
 

        "Team Leadership", "Agile Methodology", "Problem Solving",
 

        "Communication", "Project Management"
 

    ]
 

    
 

    job_types = ["Full-time", "Part-time", "Contract", "Internship"]
 

    
 

    jobs = []
 

    
 

    for i in range(1, num_jobs + 1):
 

        try:
 

            job_title = random.choice(job_titles)
 

            is_technical = "Engineer" in job_title or "Developer" in job_title
 

            
 

            # Generate appropriate skills based on job type
 

            if is_technical:
 

                skills = random.sample(tech_skills, k=random.randint(2, 5))
 

            else:
 

                skills = random.sample(tech_skills, k=random.randint(1, 3)) 

                random.sample(soft_skills, k=random.randint(1, 2))
 

            
 

            # Create salary range based on position
 

            base_salary = random.randint(60, 120)
 

            if "Senior" in job_title:
 

                base_salary += 30
 

            elif "Junior" in job_title:
 

                base_salary -= 20
 

            
 

            job = {
 

                "id": f"job-{i:03d}",
 

                "title": job_title,
 

                "company": random.choice(companies),
 

                "location": random.choice(locations),
 

                "type": random.choice(job_types),
 

                "salary": f"${base_salary}k - ${base_salary + random.randint(20, 40)}k",
 

                "posted": (datetime.now() - timedelta(days=random.randint(1, 30)))
 

                          .strftime("%Y-%m-%d"),
 

                "description": generate_description(job_title, skills),
 

                "tags": skills,
 

                "featured": random.random() < 0.3  # 30% chance of being featured
 

            }
 

            jobs.append(job)
 

        except Exception as e:
 

            print(f"Error generating job {i}: {str(e)}")
 

            continue
 

            
 

    return jobs
 


 

def generate_description(title: str, skills: List[str]) -> str:
 

    """Generate realistic job description"""
 

    responsibilities = [
 

        f"Design and implement {random.choice(['scalable', 'reliable', 'secure'])} {title.lower()} solutions",
 

        f"Collaborate with {random.choice(['cross-functional', 'product', 'engineering'])} teams",
 

        f"Write {random.choice(['clean', 'maintainable', 'well-documented'])} code",
 

        f"Participate in {random.choice(['code reviews', 'design discussions', 'sprint planning'])}",
 

        f"Optimize {random.choice(['application performance', 'database queries', 'cloud infrastructure'])}"
 

    ]
 

    
 

    requirements = [
 

        f"{random.randint(2, 8)}+ years of experience in {title.split()[0]}",
 

        f"Strong knowledge of {', '.join(random.sample(skills, min(3, len(skills))))}",
 

        f"Experience with {random.choice(['Agile', 'Scrum', 'CI/CD'])} methodologies",
 

        f"{random.choice(['Bachelor\'s', 'Master\'s'])} degree in {random.choice(['CS', 'Engineering', 'related field'])} or equivalent experience"
 

    ]
 

    
 

    return (
 

        f"We are looking for a {title} to join our team. "
 

        f"Key responsibilities include: {'; '.join(random.sample(responsibilities, 3))}. "
 

        f"Requirements: {'; '.join(random.sample(requirements, 3))}. "
 

        f"Nice to have: {random.choice(requirements)}."
 

    )
 


 

# Example usage
 

if __name__ == "__main__":
 

    try:
 

        generated_jobs = generate_jobs(5)
 

        for job in generated_jobs:
 

            print(f"{job['title']} at {job['company']}")
 

    except Exception as e:
 

        print(f"Failed to generate jobs: {str(e)}") 