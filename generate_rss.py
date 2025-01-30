from feedgen.feed import FeedGenerator

# Generate RSS feed from email addresses
def generate_rss(email_addresses):
    fg = FeedGenerator()
    fg.title('Email Addresses RSS Feed')
    fg.link(href='https://yourwebsite.com/rss', rel='self')
    fg.description('Latest email addresses from Firestore')

    for email in email_addresses:
        fe = fg.add_entry()
        fe.title(email)

    rss_feed = fg.rss_str(pretty=True)
    return rss_feed

""" if __name__ == "__main__":
    # Example email addresses (replace with actual retrieval from Firestore)
    email_addresses = 
    
    rss_feed = generate_rss(email_addresses)
    print("Generated RSS feed:", rss_feed) """