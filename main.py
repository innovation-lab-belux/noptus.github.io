import fetch_emails
import generate_rss
import subprocess
import time

if __name__ == "__main__":
    while True:
        email_addresses = fetch_emails.get_emails()
        
        rss_feed = generate_rss.generate_rss(email_addresses)

        with open('emails_rss.rss', 'w') as file:
            file.write(rss_feed.decode('utf-8'))
        
        # Wait for 1 minute before running again
        time.sleep(60)