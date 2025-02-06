import fetch_emails
import generate_rss
import subprocess
import time
import logging

logging.basicConfig(level=logging.INFO)

def push_to_github():
    try:
        logging.info("Adding emails_rss.rss to Git")
        subprocess.run(['git', 'add', 'emails_rss.rss'], check=True)
        
        logging.info("Committing changes")
        subprocess.run(['git', 'commit', '-m', 'Update RSS feed'], check=True)
        
        logging.info("Pushing to GitHub")
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        
        logging.info("Successfully pushed to GitHub")
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while pushing to GitHub: {e}")

if __name__ == "__main__":
    while True:
        email_addresses = fetch_emails.get_emails()
        
        rss_feed = generate_rss.generate_rss(email_addresses)

        with open('emails_rss.rss', 'w') as file:
            file.write(rss_feed.decode('utf-8'))
        
        push_to_github()
        
        # Wait for 1 minute before running again
        time.sleep(60)