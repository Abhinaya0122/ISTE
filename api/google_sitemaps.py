from datetime import datetime

# Update this to match your live domain
BASE_URL = "https://kec-iste.vercel.app"

# List your URL paths here
pages = [
    '/',
    '/about',
    '/team',
    '/event',
    '/contact'
]

def generate_sitemap():
    today = datetime.now().date()
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for path in pages:
        sitemap.append(f"""  <url>
    <loc>{BASE_URL}{path}</loc>
    <lastmod>{today}</lastmod>
  </url>""")

    sitemap.append('</urlset>')

    with open('static/sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sitemap))

    print("✅ sitemap.xml generated in /static folder.")

if __name__ == "__main__":
    generate_sitemap()
