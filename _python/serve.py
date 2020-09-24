"""
Use livereload to serve, build, and reload the website when files change.
"""
from livereload import Server, shell


server = Server()
files = ["**/**.md", "_site.yml", "images/", "css/", "js/", "_layouts/", "_python/"]
for filename in files:
    server.watch(filename, "urubu build")
server.serve(root="_build", port="8008", host="localhost", open_url_delay=1)
