import fetch_emails
import generate_rss
import subprocess

if __name__ == "__main__":
    email_addresses = fetch_emails.get_emails()
    
    rss_feed = generate_rss.generate_rss(email_addresses)

    with open ('emails_rss.rss', 'w') as file:
        file.write(rss_feed.decode('utf-8'))