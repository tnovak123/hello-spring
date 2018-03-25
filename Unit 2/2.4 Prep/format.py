markup = """
<!Doctyp html>
<html>
    <head>
        <title>{0}</title>
    </head>
    <body>
        <h1>{1}</h1>
    </body>
</html>
"""
# an alternate way is to name the insertion points which requires a "name='my page title'" association
markup = markup.format('My Page Title', 'Page Heading')
print(markup)