news = [
    {
    "title": "Muskan leaves the group",
    "category": "info",
    "content": "Muskan Sharma leaves the group and joining at Charles University, Chez Republic.",
    "link": "Farewel Muskan!"
},

{
    "title": "New member in the group",
    "category": "info",
    "content": "Shaheerah Shahid joins as a JRF in the group.",
    "link": "Welcome Shaheerah!"
},
    {
    "title": "Dr. Chakrabarty receives award",
    "category": "award",
    "content": "Dr. Suman Chakrabarty received the CRSI Bronze medal 2025",
    "link": "https://x.com/ChemResSocIndia/status/1809264682374738052"
},
{
    "title": "Paper published in Chemical Physics Impact",
    "category": "paper",
    "content": "K. Sinha published a paper in Chemical Physics Impact",
    "link": "https://scholar.google.co.in/citations?view_op=view_citation&hl=en&user=dcj-bnsAAAAJ&sortby=pubdate&citation_for_view=dcj-bnsAAAAJ:2_BaaiyHPJIC"
},
{
    "title": "TRC project position open",
    "category": "position",
    "content": "We have a position open for a project student under the TRC project scheme",
    "link": "https://www.bose.res.in/departments/TRC/index.jsp"
}]



template = open("index_template.html", "r").readlines()
header = template[:114]
tailed = template[114:]

def news_format(title, category, content, link):

    if category=="award":
        return f"""                <div class="packages-item">
                        <div class="packages-content bg-light">
                            <div class="p-4 pb-0" style="border: #198754 1px solid;min-height:175px;">
                            <small class="text-uppercase text-success" style="font-size: smaller; font-weight: 700;">Award</small>
                                <h5 class="mb-0">{title}</h5>
                                <p class="">{content}</p>
                            </div>
                            <div class="row bg-success rounded-bottom mx-0">
                                <div class="text-end text-white px-0">
                                    <a href="{link}" class="btn-hover btn text-white">Know More!</a>
                                </div>
                            </div>
                        </div>
                    </div>"""
    if category=="info":
        return f"""                <div class="packages-item">
                <div class="packages-content bg-light">
                    <div class="p-4 pb-0" style="border: #0dcaf0 1px solid;min-height:175px;">
                        <small class="text-uppercase text-info" style="font-size: smaller; font-weight: 700;">News</small>
                        <h5 class="mb-0">{title}</h5>
                        <p class="">{content}</p>
                    </div>
                    <div class="row bg-info rounded-bottom mx-0">
                        <div class="text-end text-white px-0">
                            <a href="#" class="btn-hover btn text-white">{link}</a>
                        </div>
                    </div>
                </div>
            </div>"""
    
    if category=="paper":
        return f"""                <div class="packages-item">
                <div class="packages-content bg-light">
                    <div class="p-4 pb-0" style="border: #13357b 1px solid; min-height:175px;">
                    <small class="text-uppercase text-primary" style="font-size: smaller; font-weight: 700;">Publication</small>
                        <h5 class="mb-0">{title}</h5>
                        <p class="">{content}</p>
                    </div>
                    <div class="row bg-primary rounded-bottom mx-0">
                        <div class="text-end text-white px-0">
                            <a href="{link}" class="btn-hover btn text-white">Link to article</a>
                        </div>
                    </div>
                </div>
            </div>"""
    if category=="position":
        return f"""                <div class="packages-item">
                <div class="packages-content bg-light">
                    <div class="p-4 pb-0" style="border: #ffc107 1px solid; min-height:175px;">
                    <small class="text-uppercase text-warning" style="font-size: smaller; font-weight: 700;">Positions</small>
                        <h5 class="mb-0">{title}</h5>
        
                        <p class="">{content}</p>
                    </div>
                    <div class="row bg-warning rounded-bottom mx-0">
                        <div class="text-end text-white px-0">
                            <a href="{link}" class="btn-hover btn text-white">Know More!</a>
                        </div>
                    </div>
                </div>
            </div>"""
    
starter = """    <div class="container-fluid packages">
        <div class="container py-5">
            <div class="mx-auto text-center mb-5" style="max-width: 900px;">
                <h5 class="section-title px-3">Announcements</h5>
            </div>
            <div class="packages-carousel owl-carousel">"""
ender = """</div>
        </div>
    </div>"""

my_announcements = "".join(
    news_format(
        news_item["title"],
        news_item["category"],
        news_item["content"],
        news_item["link"],
    )
    for news_item in news
)
with open('index.html', 'w') as f:
    f.write(''.join(header))
    f.write(starter)
    f.write(my_announcements)
    f.write(ender)
    f.write(''.join(tailed))