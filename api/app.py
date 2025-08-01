from flask import Flask, make_response, render_template, request, redirect, jsonify, send_from_directory, url_for
from urllib.parse import quote as url_quote
from datetime import datetime
from flask import Response
app = Flask(__name__)

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    pages = [
        {'loc': '/', 'lastmod': datetime.now().date()},
        {'loc': '/about', 'lastmod': datetime.now().date()},
        {'loc': '/team', 'lastmod': datetime.now().date()},
        {'loc': '/event', 'lastmod': datetime.now().date()},
        {'loc': '/contact', 'lastmod': datetime.now().date()},
    ]

    sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>',
                   '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

    for page in pages:
        sitemap_xml.append(f"""<url>
  <loc>https://kec-iste.vercel.app{page['loc']}</loc>
  <lastmod>{page['lastmod']}</lastmod>
</url>""")

    sitemap_xml.append('</urlset>')
    response = make_response('\n'.join(sitemap_xml))
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/event')
def event():
    return render_template('timeline.html')

@app.route('/contact')
def contact():
    return render_template('contacts.html')

@app.route('/googlee11137f78e34b468.html')
def google_verification():
    return send_from_directory('static', 'googlee11137f78e34b468.html')


if __name__ == '__main__':
    app.run(debug=True)
