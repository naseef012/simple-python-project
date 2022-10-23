
def render_template(template_name='index.html', path="/"):
    html_str = ""
    with open(template_name, 'r') as f:
        html_str = f.read()
    return html_str

def app(environ, start_response):
    path = environ.get("PATH_INFO")
    if path == "/": #index / root of the web app
        data = render_template(template_name = 'index.html', path=path)
    else:
        data = render_template(template_name='404.html', path=path)
    for k, v in environ.items():
        print(k,v)
    # data = "Hello motherfucker!"
    data = render_template()
    data = data.encode("utf-8")
    start_response(
        f"200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ]
    )
    return iter([data])
