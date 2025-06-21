from llama_cpp import Llama

# Path to your quantized model
MODEL_PATH  = "models/mistral-7b-instruct-v0.1.Q4_0.gguf"


# Initialize the model (you can tweak n_ctx for larger input)
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=8096,
    n_threads=40,
    n_gpu_layers=-1,  # 👉 runs first 20 layers on GPU, rest on CPU
    n_batch=512,           # adjust if running into memory issues
    verbose=True
)

# Example SEO JSON data
seo_data = {
    "status": "success",
    "data": {
        "traffic_data": {
            "estimated_visitors": "12",
            "page_views": "24",
            "bounce_rate": "47%",
            "avg_session_duration": "1m 38s"
        },
        "performance_metrics": {
            "error": None,
            "performanceMetrics": {
                "First Contentful Paint": "1.2 s",
                "Fully Loaded Time": "5.7 s",
                "Time to Interactive": "2.9 s",
                "Total Blocking Time": "50 ms",
                "Cumulative Layout Shift": "0.053",
                "Largest Contentful Paint": "2.8 s",
                "Onload Time": "N/A",
                "Redirect Time": "Potential savings of 230 ms"
            },
            "seoMetrics": {
                "Mobile Friendly": "Yes",
                "Structured Data": "Missing",
                "Meta Description": "Missing",
                "Title Tags": "Missing",
                "Alt Text": "Missing",
                "Mobile Usability": "Good",
                "SEO-Friendly URL": "No"
            }
        },
        "social_data": {
            "facebook": {
                "url": "https://www.facebook.com/4IMIWEBSEO/",
                "followers": 1000,
                "image": "https://scontent.fdad1-4.fna.fbcdn.net/v/t39.30808-1/327240841_1198861440749397_5364104914200004751_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=FWjXxLN5j6AQ7kNvwEwh096&_nc_oc=AdkmXL8w9bbcND0pC6dZRnMRT1OViGKQBBM_BZXFhjDdgihpQDos2yOdpQeOcschITk&_nc_zt=24&_nc_ht=scontent.fdad1-4.fna&_nc_gid=PyTBTcraLwyaAIHd5ZEfZQ&oh=00_AfHWcuTYiKUV4FQhiu6wZG69GUjOHTNa6wzALUudomMwGQ&oe=680F43DC",
                "name": "Internet Marketing Images, Inc.",
                "likes": 1000,
                "phone": "+1 877-469-9322",
                "email": "sales@4imi.com",
                "website": "4imi.com",
                "intro": "Dallas-based internet marketing agency specializing in web design and search engine optimization (SEO).We pride ourselves on remarkable, meaningful, and memorable development solutions that demand recognition from potential and current customers."
            },
            "twitter": {
                "url": None,
                "followers": "N/A",
                "image": ""
            },
            "linkedin": {
                "url": "https://www.linkedin.com/company/856564/ ",
                "followers": 74,
                "image": "https://media.licdn.com/dms/image/v2/C4D0BAQEpkIkD4VB98Q/company-logo_400_400/company-logo_400_400/0/1631329558610?e=1750896000&v=beta&t=pIFzFv9TX9nG1DKT1cVNy0HGoAv0j0AM2H2QXfrHtmw"
            }
        },
        "backlink_data": {
            "total_backlinks": 0,
            "unique_domains": 0,
            "toxic_backlinks": 0,
            "backlinks": [],
            "error": "API Error: Client error: `GET https://best-backlink-checker-api.p.rapidapi.com/backlinks.php?domain=https://4imi.com` resulted in a `429 Too Many Requests` response:\n{\"message\":\"You have exceeded the MONTHLY quota for Requests on your current plan, BASIC. Upgrade your plan at https:\\/\\ (truncated...)\n"
        },
        "meta_tags": {
            "title": "Website Design Experts & SEO Specialist | Dallas, TX | IMI",
            "description": "About IMI IMI – Marketing with a Personal Touch IMI is not a one size fits all marketing company. We work within your budget to make digital marketing work for you. We are experts in the multifaceted world of internet marketing from award winning web design and search engine optimization to social media and online",
            "keywords": "dallas seo company,search engine optimization dallas,seo dallas,seo dallas texas,dallas seo,search engine optimization,web,site,website,design,designs,in,seo,social media,mobile,graphic,internet,marketing,dallas,texas,tx,75070",
            "headings": {
                "h2": [
                    "24",
                    "Get a FREE SEO website analysis report online 24/7",
                    "MARKETING STRATEGY",
                    "GOVERNMENT PROJECTS",
                    "WEB DESIGN SERVICES",
                    "SEARCH ENGINE OPTIMIZATION",
                    "SOCIAL MEDIA MARKETING",
                    "LEAD GENERATION",
                    "3D RENEDERING",
                    "REPUTATION REPAIR",
                    "POSITIVE REVIEWS",
                    "Need Web Design, SEO solution, or a Marketing Strategy?"
                ],
                "h3": [
                    "IMI – Marketing with a Personal Touch",
                    "Our Services",
                    "RECENT PROJECTS",
                    "Our Services",
                    "Contact Info."
                ],
                "h4": [
                    "About IMI",
                    "WHAT WE DO FOR YOU"
                ]
            },
            "duplicate_content": [],
            "duplicate_links": [
                {
                    "href": "https://www.facebook.com/4IMIWEBSEO/",
                    "anchor_text": "",
                    "occurrences": 2
                },
                {
                    "href": "https://www.linkedin.com/company/856564/",
                    "anchor_text": "",
                    "occurrences": 2
                },
                {
                    "href": "https://www.4imi.com/website-design-frisco-mckinney-plano-dallas-seo-company/",
                    "anchor_text": "SEO",
                    "occurrences": 2
                },
                {
                    "href": "https://www.4imi.com/web-design/",
                    "anchor_text": "Web Design",
                    "occurrences": 2
                },
                {
                    "href": "https://www.4imi.com/dallas-social-media-marketing-consultants/",
                    "anchor_text": "Social Media",
                    "occurrences": 2
                },
                {
                    "href": "https://www.4imi.com/dallas-lead-generation-seo-ppc-email-marketing/",
                    "anchor_text": "Lead Generation",
                    "occurrences": 2
                },
                {
                    "href": "https://www.4imi.com/dallas-reputation-repair-online-reputation-management-tx/",
                    "anchor_text": "Reputation Repair",
                    "occurrences": 2
                },
                {
                    "href": "https://www.4imi.com/non-profit-business/",
                    "anchor_text": "Non Profit",
                    "occurrences": 2
                },
                {
                    "href": "https://www.4imi.com/3d-rendering/",
                    "anchor_text": "3D Rendering",
                    "occurrences": 2
                },
                {
                    "href": "https://www.4imi.com/government-projects/",
                    "anchor_text": "Government Projects",
                    "occurrences": 3
                }
            ],
            "broken_links": [
                {
                    "href": "https://www.facebook.com/4IMIWEBSEO/",
                    "status": "HTTP/1.1 302 Found"
                },
                {
                    "href": "https://www.linkedin.com/company/856564/",
                    "status": "HTTP/1.1 999 Request denied"
                },
                {
                    "href": "https://www.facebook.com/4IMIWEBSEO/",
                    "status": "HTTP/1.1 302 Found"
                },
                {
                    "href": "https://www.linkedin.com/company/856564/",
                    "status": "HTTP/1.1 999 Request denied"
                }
            ]
        },
        "domain_info": {
            "age": "16 Years",
            "expiration": "2025-11-08T17:08:46Z",
            "registrar": "GoDaddy.com, LLC",
            "ssl_status": "Valid until 2025-07-18",
            "hosting_provider": "Detected IP: 192.249.120.197 (Provider lookup not available without API)",
            "dns_status": "Properly Configured"
        },
        "dns_records": {
            "A": [],
            "MX": "No MX records found.",
            "NS": [],
            "SOA": "SOA record is missing or improperly configured.",
            "TXT": [],
            "CNAME": [],
            "PTR": [
                {
                    "Reverse Lookup": "ded4547.inmotionhosting.com"
                }
            ],
            "NS_Performance": [
                {
                    "Server": "ns58.domaincontrol.com",
                    "Resolved IP": "173.201.76.29",
                    "TTL": 3600,
                    "Response Time (ms)": 10,
                    "Status": "OK"
                },
                {
                    "Server": "ns57.domaincontrol.com",
                    "Resolved IP": "97.74.108.29",
                    "TTL": 3600,
                    "Response Time (ms)": 10,
                    "Status": "OK"
                }
            ]
        },
        "ssl_details": {
            "status": "Valid",
            "days_left": 85,
            "details": {
                "domain": "4imi.com",
                "ip_address": "192.249.120.197",
                "issuer_organization": "Let's Encrypt",
                "issuer_common_name": "R10",
                "issuer_locality": "Unknown",
                "issuer_country": "US",
                "common_name": "www.4imi.com",
                "sans": "DNS:4imi.com, DNS:cpanel.4imi.com, DNS:mail.4imi.com, DNS:webdisk.4imi.com, DNS:webmail.4imi.com, DNS:www.4imi.com",
                "valid_from": "April 19, 2025",
                "valid_to": "July 18, 2025",
                "days_remaining": "85 days",
                "serial_number": "06D8CEAFF46A9FE1617552AA7B17FFAED3E4",
                "signature_algorithm": "RSA-SHA256",
                "version": 3
            }
        },
        "whois_data": {
            "raw": None,
            "expiration_date": "Not found",
            "registrar": "Not found"
        },
        "sitemap_exists": "https://4imi.com/sitemap.xml",
        "performance_data": {
            "website_performance": 72,
            "performance_grade": "C",
            "seo_performance": 77,
            "seo_grade": "B",
            "speed_index": "5.1 s",
            "Redirect Duration": "Potential savings of 230 ms",
            "Time to First Byte (TTFB)": "Root document took 290 ms",
            "DOM Content Loaded Time": "N/A",
            "Connection Duration": "952.5 ms",
            "First Paint": "N/A",
            "Onload Time": "N/A",
            "Backend Duration": "Root document took 290 ms",
            "DOM Interactive Time": "N/A",
            "Fully Loaded Time": "5.1 s",
            "Performance Score (%)": 72,
            "Performance Grade": "C",
            "SEO Score (%)": 77,
            "SEO Grade": "B",
            "first_contentful_paint": "1.2 s",
            "fully_loaded_time": "5.1 s",
            "time_to_interactive": "2.8 s",
            "total_blocking_time": "30 ms",
            "backend_time": "Root document took 290 ms",
            "connect_time": "938.99 ms",
            "regional_performance": {
                "USA": "919.31 ms",
                "Canada": "975.31 ms",
                "France": "952.31 ms"
            },
            "cumulative_layout_shift": "0.058",
            "largest_contentful_paint": "2.7 s",
            "onload_time": "N/A",
            "redirect_time": "Potential savings of 230 ms",
            "ttfb": "Root document took 290 ms"
        },
        "sitemap_analysis": {
            "sitemap_found": True,
            "total_pages": 0,
            "pages": []
        },
        "crawl_data": {
            "index_pages": 16,
            "pages_crawled": 27,
            "pages_list": {
                "0": "https://www.4imi.com//request-quote/",
                "1": "https://www.4imi.com/",
                "3": "https://www.4imi.com/about-us/",
                "4": "https://www.4imi.com/services/",
                "5": "https://www.4imi.com/website-design-frisco-mckinney-plano-dallas-seo-company/",
                "6": "https://www.4imi.com/web-design/",
                "8": "https://www.4imi.com/e-commerce-website-dallas-ft-worth-texas/",
                "9": "https://www.4imi.com/dallas-mobile-web-design-apps-tx-internet-company/",
                "10": "https://www.4imi.com/dallas-social-media-marketing-consultants/",
                "11": "https://www.4imi.com/dallas-lead-generation-seo-ppc-email-marketing/",
                "12": "https://www.4imi.com/dallas-reputation-repair-online-reputation-management-tx/",
                "13": "https://www.4imi.com/non-profit-business/",
                "14": "https://www.4imi.com/3d-rendering/",
                "15": "https://www.4imi.com/government-projects/",
                "17": "https://www.4imi.com/government-projects/compliance-compatibility-and-accessibility/",
                "18": "https://www.4imi.com/request-quote/"
            }
        },
        "search_ranking": {
            "total_indexed": "16",
            "top_result": "https://www.4imi.com/"
        },
        "local_search_data": {
            "gmb_status": "Not Verified",
            "local_pack_ranking": "Not Ranked"
        },
        "blacklist_check": [
            "4imi.com is listed on zen.spamhaus.org",
            "4imi.com is listed on bl.spamcop.net",
            "4imi.com is listed on b.barracudacentral.org",
            "4imi.com is listed on dnsbl.sorbs.net",
            "4imi.com is listed on spam.dnsbl.sorbs.net"
        ],
        "schema_data": {
            "organization": "Missing",
            "article": "Missing",
            "product": "Missing"
        },
        "keywords": {
            "marketing": 14,
            "online": 7,
            "design": 6,
            "social": 5,
            "company": 4,
            "work": 4,
            "search": 4,
            "engine": 4,
            "optimization": 4,
            "media": 4,
            "website": 3,
            "experts": 3,
            "internet": 3,
            "services": 3,
            "repair": 3,
            "positive": 3,
            "need": 3,
            "business": 3,
            "personal": 2,
            "touch": 2
        },
        "url": "https://4imi.com"
    }
}

# Get all keys in the dictionary
data_keys = seo_data["data"].keys()

# for key in data_keys:
#     value = seo_data["data"][key]
#     if isinstance(value, dict):        
#         data = {key: value}
#         # Format your prompt
#         prompt = f"""
#         Analyze this SEO data and list the area of improvement and what should be improved

#         SEO JSON:
#         {data}

#         Suggestions:
#         """

#         # Run the model
#         output = llm(prompt, max_tokens=512,stop=["\n\n", "###"])

#         # Print output
#         print("🔍 Suggestions:")
#         print(output)

prompt = f"""
You are an experienced SEO expert with deep knowledge of on-page SEO, technical SEO, content optimization, and keyword strategy.

You will be given an SEO analysis of a webpage in JSON format. Your task is to:
1. Read and interpret the JSON data.
2. Identify SEO issues, inefficiencies, or areas for improvement.
3. Suggest specific, actionable recommendations in clear bullet points.
4. Prioritize the suggestions in order of impact on SEO.

Respond in a professional tone.

Here is the SEO analysis in JSON format:
{seo_data}

Please begin your analysis.

"""

 # Run the model
output = llm(prompt, max_tokens=8096,stop=["\n\n", "###"])

 # Print output
print("🔍 Suggestions:")
print(output)