#!/usr/bin/env python3
"""TrackLinks Build — Campaign URL Builder, dark dashboard style"""

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DOMAIN = "tracklinks.net"
OUTPUT = "."

def w(path, content):
    full = os.path.join(OUTPUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def build_page(s):
    title = s["title"]
    desc = s["desc"]
    slug = s["slug"]
    cat = s.get("cat", "scene")
    preset = s.get("preset", {})
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{desc}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title} | TrackLinks">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="https://{DOMAIN}/{slug}/">
    <link rel="canonical" href="https://{DOMAIN}/{slug}/">
    <title>{title} | TrackLinks</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root{{--bg:#0D1117;--card:#111827;--border:#1F2937;--text:#E6EDF3;--muted:#9CA3AF;--primary:#6366F1;--primary-hover:#4F46E5;--radius:12px}}
        *{{box-sizing:border-box;margin:0;padding:0}}
        body{{font-family:'Inter',-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}}
        nav{{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--border);padding:14px 24px;display:flex;justify-content:space-between;z-index:100}}
        .logo{{font-weight:700;color:var(--primary);font-size:1.1rem;text-decoration:none}}
        .nav-links{{display:flex;gap:20px;align-items:center}}
        .nav-links a{{color:var(--muted);text-decoration:none;font-size:0.9rem;font-weight:500}}
        .nav-links a:hover{{color:#fff}}
        .container{{display:flex;min-height:calc(100vh - 60px)}}
        .sidebar{{width:280px;border-right:1px solid var(--border);padding:24px 20px;flex-shrink:0;overflow-y:auto}}
        .sidebar h3{{font-size:0.75rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--muted);margin-bottom:16px}}
        .side-item{{display:block;padding:10px 14px;margin-bottom:6px;border:1px solid var(--border);border-radius:8px;cursor:pointer;background:var(--card);color:var(--text);text-decoration:none;font-size:0.9rem;transition:all .15s}}
        .side-item:hover,.side-item.active{{border-color:var(--primary);background:#1E1B4B}}
        .main{{flex:1;padding:32px 40px}}
        .card{{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:28px;max-width:720px}}
        input,select{{width:100%;padding:12px 14px;margin-bottom:12px;border-radius:10px;border:1px solid var(--border);background:var(--bg);color:var(--text);font-family:inherit;font-size:0.95rem}}
        input:focus,select:focus{{outline:none;border-color:var(--primary)}}
        .btn{{background:var(--primary);color:#fff;padding:12px 24px;border:none;border-radius:10px;cursor:pointer;font-size:1rem;font-weight:600;font-family:inherit;width:100%}}
        .btn:hover{{background:var(--primary-hover)}}
        .output{{margin-top:16px;padding:14px;border-radius:10px;background:var(--bg);border:1px solid var(--border);word-break:break-all;color:#A5B4FC;font-family:monospace;font-size:0.9rem;min-height:44px}}
        h1{{font-size:1.75rem;margin-bottom:8px}}
        .sub{{color:var(--muted);font-size:0.95rem;margin-bottom:24px}}
        .content-section{{max-width:720px;margin-top:40px}}
        .content-section h2{{font-size:1.2rem;margin:24px 0 10px;color:var(--text)}}
        .content-section p{{color:var(--muted);margin-bottom:12px;font-size:0.95rem;line-height:1.7}}
        .cross-link{{margin-top:40px;padding:20px;background:#1E1B4B;border:1px solid var(--primary);border-radius:12px;max-width:720px}}
        .cross-link strong{{color:#A5B4FC}}
        .cross-link a{{color:#C7D2FE;font-weight:500}}
        .breadcrumb{{font-size:0.85rem;color:var(--muted);margin-bottom:24px}}
        .breadcrumb a{{color:var(--primary);text-decoration:none}}
        footer{{background:var(--card);border-top:1px solid var(--border);padding:24px;text-align:center;color:var(--muted);font-size:0.85rem;margin-top:40px}}
        footer a{{color:var(--primary);text-decoration:none}}
        @media(max-width:768px){{.container{{flex-direction:column}}.sidebar{{width:100%;border-right:none;border-bottom:1px solid var(--border)}}.main{{padding:20px}}}}
    </style>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"SoftwareApplication","name":"{title}","url":"https://{DOMAIN}/{slug}/","description":"{desc}","applicationCategory":"BusinessApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"What is a Campaign URL Builder?","acceptedAnswer":{{"@type":"Answer","text":"A tool that creates trackable marketing links by adding UTM parameters so you can measure campaign performance in Google Analytics."}}}},{{"@type":"Question","name":"Is TrackLinks free?","acceptedAnswer":{{"@type":"Answer","text":"Yes, completely free. No sign-up required."}}}},{{"@type":"Question","name":"What platforms does TrackLinks support?","acceptedAnswer":{{"@type":"Answer","text":"Google Ads, Facebook Ads, TikTok, Instagram, Email, and any platform using UTM parameters."}}}}]}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://{DOMAIN}/"}},{{"@type":"ListItem","position":2,"name":"{title}","item":"https://{DOMAIN}/{slug}/"}}]}}
    </script>
</head>
<body>
    <nav>
        <a href="/" class="logo">TrackLinks</a>
        <div class="nav-links">
            <a href="/">Home</a>
            <a href="#builder">Builder</a>
            <a href="#faq">FAQ</a>
        </div>
    </nav>
    <div class="container">
        <div class="sidebar">
            <h3>Platforms</h3>
            {''.join(f'<a href="/{p["slug"]}/" class="side-item{(" active" if p["slug"]==slug else "")}">{p["title"].replace("UTM Builder for ","")}</a>' for p in PLATFORMS[:12])}
        </div>
        <div class="main">
            <div class="breadcrumb"><a href="/">Home</a> / {title}</div>
            <h1>{title}</h1>
            <p class="sub">{desc}</p>
            <div class="card" id="builder">
                <input id="url" placeholder="Landing page URL (e.g. https://example.com)" value="{preset.get('url','')}">
                <input id="source" placeholder="utm_source (e.g. google, facebook)" value="{preset.get('source','')}">
                <input id="medium" placeholder="utm_medium (e.g. cpc, email, social)" value="{preset.get('medium','')}">
                <input id="campaign" placeholder="utm_campaign (campaign name)" value="{preset.get('campaign','')}">
                <input id="term" placeholder="utm_term (optional, for paid keywords)">
                <input id="content" placeholder="utm_content (optional, for A/B testing)">
                <button class="btn" onclick="generate()">Generate Tracking Link</button>
                <div class="output" id="output">Your tracking URL will appear here...</div>
                <button class="btn" style="margin-top:8px;background:var(--card);color:var(--text);border:1px solid var(--border)" onclick="copyLink()">Copy Link</button>
            </div>
            <div class="content-section">
                <h2>What is TrackLinks?</h2>
                <p>TrackLinks is a free campaign URL builder that helps you create trackable marketing links with UTM parameters. Build links for Google Ads, Facebook Ads, TikTok campaigns, email marketing, and more — then measure performance in Google Analytics. Build your campaign links with TrackLinks for precise attribution tracking.</p>
                <h2>How It Works</h2>
                <p>Step 1: Enter your landing page URL. Step 2: Add your traffic source (e.g. google, facebook). Step 3: Choose your medium (cpc, email, social). Step 4: Name your campaign. Step 5: Copy and use the generated tracking link.</p>
                <h2>Common Use Cases</h2>
                <p>TrackLinks is used by marketers and advertisers for Google Ads tracking, Facebook campaign attribution, TikTok ad measurement, email campaign tracking, affiliate link management, and social media traffic analysis.</p>
                <h2>About This Tool</h2>
                <p>{desc} Use TrackLinks to build campaign URLs with UTM parameters for precise marketing attribution.</p>
            </div>
            <div class="cross-link">
                <strong>Pro Tip</strong> — Need to compress images for your campaigns? Try <a href="https://compressnow.net">CompressNow</a>. Resizing ad creatives? Use <a href="https://resizenow.net">ResizeNow</a>. Writing ad copy? <a href="https://messagegen-ai.com">MessageGen-AI</a> helps with email drafts.
            </div>
            <div class="content-section" id="faq">
                <h2>Frequently Asked Questions</h2>
                <p><strong>Q: What are UTM parameters?</strong><br>A: UTM parameters are tags added to URLs that allow Google Analytics to track where your traffic comes from, which medium was used, and which campaign drove the visit.</p>
                <p><strong>Q: Is TrackLinks free?</strong><br>A: Yes, completely free with no sign-up required. Build unlimited campaign URLs.</p>
                <p><strong>Q: Can I use TrackLinks for Facebook Ads?</strong><br>A: Yes — just select Facebook Ads preset and TrackLinks fills the right UTM values.</p>
                <p><strong>Q: How do I see the tracking data?</strong><br>A: After using your TrackLinks-generated URL in campaigns, check Google Analytics under Acquisition > Campaigns.</p>
            </div>
        </div>
    </div>
    <footer>
        <p>TrackLinks — Free Campaign URL Builder. Build tracking links for Google Ads, Facebook, TikTok, email and more.</p>
        <p style="margin-top:8px"><a href="/">Home</a> · <a href="https://compressnow.net">CompressNow</a> · <a href="https://resizenow.net">ResizeNow</a> · <a href="https://tonemodifier.com">ToneModifier</a></p>
    </footer>
    <script>
function generate(){{
    var url=document.getElementById('url').value;
    var source=document.getElementById('source').value;
    var medium=document.getElementById('medium').value;
    var campaign=document.getElementById('campaign').value;
    var term=document.getElementById('term').value;
    var content=document.getElementById('content').value;
    var params=[];
    if(source)params.push('utm_source='+encodeURIComponent(source));
    if(medium)params.push('utm_medium='+encodeURIComponent(medium));
    if(campaign)params.push('utm_campaign='+encodeURIComponent(campaign));
    if(term)params.push('utm_term='+encodeURIComponent(term));
    if(content)params.push('utm_content='+encodeURIComponent(content));
    var result=url+(url.includes('?')?'&':'?')+params.join('&');
    document.getElementById('output').innerText=result;
}}
function copyLink(){{
    var t=document.getElementById('output').innerText;
    navigator.clipboard.writeText(t);
    alert('Copied!');
}}
    </script>
</body>
</html>"""

# ═══ Page Definitions ═══════════════════════════════

HOMEPAGE = {
    "title": "Campaign URL Builder",
    "desc": "Build trackable marketing links with UTM parameters for Google Ads, Facebook, TikTok and email campaigns. Free, no sign-up.",
    "slug": "",
}

PLATFORMS = [
    {"slug":"utm/google-ads","title":"UTM Builder for Google Ads","desc":"Create UTM tracking links for Google Ads campaigns. Track clicks, conversions, and ROI with proper utm_source=google parameters.","cat":"platform","preset":{"source":"google","medium":"cpc","campaign":""}},
    {"slug":"utm/facebook-ads","title":"UTM Builder for Facebook Ads","desc":"Build UTM parameters for Facebook Ads Manager campaigns. Track ad performance with utm_source=facebook and campaign-specific tags.","cat":"platform","preset":{"source":"facebook","medium":"cpc","campaign":""}},
    {"slug":"utm/tiktok-ads","title":"UTM Builder for TikTok Ads","desc":"Generate UTM tracking links for TikTok advertising campaigns. Measure reach and conversion from TikTok traffic.","cat":"platform","preset":{"source":"tiktok","medium":"cpc","campaign":""}},
    {"slug":"utm/instagram-ads","title":"UTM Builder for Instagram Ads","desc":"Create UTM parameters for Instagram ad campaigns. Track link clicks from Stories, Feed, and Reels ads.","cat":"platform","preset":{"source":"instagram","medium":"cpc","campaign":""}},
    {"slug":"utm/linkedin-ads","title":"UTM Builder for LinkedIn Ads","desc":"Build UTM tracking URLs for LinkedIn sponsored content and text ads. Track B2B campaign performance.","cat":"platform","preset":{"source":"linkedin","medium":"cpc","campaign":""}},
    {"slug":"utm/twitter-ads","title":"UTM Builder for Twitter/X Ads","desc":"Create UTM-tagged links for Twitter/X advertising campaigns. Track engagement and conversion from promoted tweets.","cat":"platform","preset":{"source":"twitter","medium":"cpc","campaign":""}},
    {"slug":"utm/pinterest-ads","title":"UTM Builder for Pinterest Ads","desc":"Generate UTM tracking for Pinterest promoted pins and shopping ads. Measure traffic from visual discovery.","cat":"platform","preset":{"source":"pinterest","medium":"cpc","campaign":""}},
    {"slug":"utm/youtube-ads","title":"UTM Builder for YouTube Ads","desc":"Create UTM parameters for YouTube video ad campaigns. Track views, clicks, and conversions from video traffic.","cat":"platform","preset":{"source":"youtube","medium":"cpc","campaign":""}},
    {"slug":"utm/snapchat-ads","title":"UTM Builder for Snapchat Ads","desc":"Build UTM tracking links for Snapchat advertising campaigns.","cat":"platform","preset":{"source":"snapchat","medium":"cpc","campaign":""}},
    {"slug":"utm/email-campaign","title":"UTM Builder for Email Campaigns","desc":"Generate UTM tracking for email marketing campaigns. Track clicks from newsletters, drip sequences, and promotional emails.","cat":"platform","preset":{"source":"email","medium":"email","campaign":""}},
    {"slug":"utm/affiliate","title":"UTM Builder for Affiliate Links","desc":"Create UTM-tagged affiliate links to track which partners and placements drive the most conversions.","cat":"platform","preset":{"source":"affiliate","medium":"referral","campaign":""}},
    {"slug":"utm/sms-marketing","title":"UTM Builder for SMS Marketing","desc":"Build UTM parameters for SMS and text message marketing campaigns.","cat":"platform","preset":{"source":"sms","medium":"text","campaign":""}},
    {"slug":"utm/qr-code","title":"UTM Builder for QR Code Campaigns","desc":"Create UTM links for QR code marketing — perfect for print, flyers, and offline-to-online tracking.","cat":"platform","preset":{"source":"qr","medium":"print","campaign":""}},
    {"slug":"utm/influencer","title":"UTM Builder for Influencer Campaigns","desc":"Generate unique UTM links for each influencer or creator to track individual performance.","cat":"platform","preset":{"source":"influencer","medium":"social","campaign":""}},
    {"slug":"utm/display-ads","title":"UTM Builder for Display Ads","desc":"Create UTM parameters for Google Display Network and programmatic display campaigns.","cat":"platform","preset":{"source":"display","medium":"cpm","campaign":""}},
    {"slug":"utm/retargeting","title":"UTM Builder for Retargeting Campaigns","desc":"Build UTM-tagged URLs for retargeting and remarketing campaigns across platforms.","cat":"platform","preset":{"source":"retargeting","medium":"cpc","campaign":""}},
    {"slug":"utm/podcast","title":"UTM Builder for Podcast Sponsorships","desc":"Create UTM tracking links for podcast ad reads and sponsorship mentions.","cat":"platform","preset":{"source":"podcast","medium":"audio","campaign":""}},
    {"slug":"utm/webinar","title":"UTM Builder for Webinar Promotion","desc":"Generate UTM links for webinar registration pages to track which promotion channels convert best.","cat":"platform","preset":{"source":"webinar","medium":"social","campaign":""}},
    {"slug":"utm/ecommerce","title":"UTM Builder for Ecommerce Campaigns","desc":"Create UTM parameters for ecommerce marketing — track product launches, sales, and seasonal promotions.","cat":"platform","preset":{"source":"ecommerce","medium":"cpc","campaign":""}},
    {"slug":"utm/content-marketing","title":"UTM Builder for Content Marketing","desc":"Build UTM links to track traffic from blog posts, guest posts, and content distribution.","cat":"platform","preset":{"source":"content","medium":"organic","campaign":""}},
    {"slug":"utm/google-analytics","title":"UTM Builder for Google Analytics 4","desc":"Create GA4-compatible UTM parameters to track campaign performance accurately in Google Analytics.","cat":"guide"},
    {"slug":"what-is-utm","title":"What is UTM Tracking? Complete Guide","desc":"Learn what UTM parameters are, how they work, and why every marketer needs them for campaign attribution.","cat":"guide"},
    {"slug":"utm-parameters-explained","title":"UTM Parameters Explained: Source, Medium, Campaign","desc":"Complete guide to all 5 UTM parameters — utm_source, utm_medium, utm_campaign, utm_term, utm_content.","cat":"guide"},
    {"slug":"how-to-track-campaigns","title":"How to Track Marketing Campaigns with UTM Links","desc":"Step-by-step guide to setting up campaign tracking with UTM parameters and Google Analytics.","cat":"guide"},
    {"slug":"utm-best-practices","title":"UTM Best Practices 2026 — Naming Conventions Guide","desc":"Learn UTM naming conventions and best practices to keep your campaign data clean and actionable.","cat":"guide"},
    {"slug":"bulk-utm-generator","title":"Bulk UTM Generator — Create Multiple Links at Once","desc":"Generate multiple UTM tracking links in bulk. Perfect for agencies managing dozens of campaigns.","cat":"tool",},
    {"slug":"url-shortener-with-tracking","title":"URL Shortener with UTM Tracking","desc":"Shorten and track your marketing links. Combine URL shortening with UTM parameters for clean, trackable links.","cat":"tool",},
    {"slug":"campaign-tracking-template","title":"Campaign Tracking Template — UTM Spreadsheet","desc":"Download a free UTM tracking template and spreadsheet to organize your campaign parameters.","cat":"guide",},
    {"slug":"utm-vs-auto-tagging","title":"UTM vs Google Ads Auto-Tagging Comparison","desc":"Learn the difference between manual UTM parameters and Google Ads auto-tagging for campaign tracking.","cat":"guide"},
    {"slug":"facebook-pixel-utm","title":"Facebook Pixel + UTM: Complete Tracking Setup","desc":"How to use UTM parameters together with Facebook Pixel for full-funnel campaign attribution.","cat":"guide"},
]

ALL_SCENARIOS = PLATFORMS

def build_home():
    html = build_page(HOMEPAGE)
    w("index.html", html)
    print("🏠 index.html")

def build_scenes():
    for s in ALL_SCENARIOS:
        html = build_page(s)
        slug_dir = s["slug"]
        w(f"{slug_dir}/index.html" if "/" in slug_dir else f"{slug_dir}.html", html)
        print(f"  📄 {s['slug']}/")

def build_sitemap():
    import os
    urls = [f"https://{DOMAIN}/"]
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f == 'index.html' and root != '.':
                rel = os.path.relpath(root, '.').replace('\\', '/')
                if not rel.startswith('.') and rel != '.git':
                    urls.append(f"https://{DOMAIN}/{rel}/")
        for f in files:
            if f.endswith('.html') and f != 'index.html' and root == '.' and not f.startswith('google'):
                urls.append(f"https://{DOMAIN}/{f}")
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in urls:
        p = "1.0" if u == f"https://{DOMAIN}/" else "0.8"
        lines.append(f'  <url><loc>{u}</loc><changefreq>weekly</changefreq><priority>{p}</priority></url>')
    lines.append('</urlset>')
    with open('sitemap.xml', 'w') as f:
        f.write('\n'.join(lines))
    print(f"📄 sitemap.xml ({len(urls)} URLs)")

def build_robots():
    w("robots.txt", f"User-agent: *\nAllow: /\nSitemap: https://{DOMAIN}/sitemap.xml\n")
    print("🤖 robots.txt")

def build_static():
    w("privacy.html", "<h1>Privacy</h1><p>TrackLinks does not collect or store personal data. Links are generated in your browser.</p>")
    w("terms.html", "<h1>Terms</h1><p>Free tool. Use at your own risk. No warranty.</p>")
    w("contact.html", "<h1>Contact</h1><p>For questions, reach out via the domain contact form.</p>")
    w("404.html", "<h1>404</h1><p>Page not found. <a href='/'>Back to TrackLinks</a></p>")

# ═══ Main ═══════════════════════════════════════════
if __name__ == "__main__":
    build_home()
    print("")
    print(f"📄 {len(ALL_SCENARIOS)} Scenario Pages:")
    build_scenes()
    build_sitemap()
    build_robots()
    build_static()
    print(f"\n✅ Build Complete — {len(ALL_SCENARIOS) + 5} pages")
