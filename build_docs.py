"""
build_docs.py

Build documentation for the project.
"""

import os
from subprocess import call
import re

def get_doc_title(fn):
    """
    Gets the document title from an HTML document.
    """
    title = None
    with open(fn, "r") as f:
        for line in f:
            matches = re.match(r'<title>(.*)</title>', line.strip())
            if matches:
                title = matches.group(1)
                break
    return title

def make_index_page(doc_dir_path):
    """
    Makes a HTML tree of documents in the docs in doc_dir_path
    """
    outfn = os.path.join(doc_dir_path,"index.html")

    def format_output(root, fn):
        """
        Makes the html format for the output
        """
        file_path = os.path.join(root, fn)
        src_fn = get_doc_title(file_path)
        args = {
            "root": root.replace(doc_dir_path, "").strip(),
            "path": file_path,
            "file": src_fn,
        }
        html = '%(root)s/<a href="/%(path)s">%(file)s</a><br>' % args 
        return html

    src_paths = []
    for root, dirs, files in os.walk(doc_dir_path):
        if files:
            for fn in sorted(files):
                if fn.endswith("html"):
                    out_html = format_output(root,fn)
                    src_paths.append(out_html)

    with open(outfn, "w") as outf:
        outf.write('''
        <html>
            <head>
                <title>Document Directory</title>
                <link rel="stylesheet" href="pycco.css">
            </head>
            <body>
                <div id="container" class="docs">
                    <h1>Directory of Documentation</h1>
                    <hr>
                    <pre>
        ''')

        outf.write('\n' + '\n'.join(src_paths))

        outf.write('''
                </pre></div>
            </body>
        </html>
        ''')

def create_pycco_docs():
    """
    Uses Pycco to create documentation for the project.
    """

    temp_dir = "docs.tmp"
    final_dir = "docs"

    # Make a temporary docs director
    out = call(["mkdir", temp_dir,])

    # Create the new documentation
    pycco_args = ["pycco",
                    "-p", "*.py",
                    "-p", "tests/js/*.js",
                    "-p", "tests/js/*/*.js",
                    "-p", "tests/py/*.py",#
                    "-p", "tests/py/*/*.py",
                    "-p", "tests/py/*/*.feature",
                    "-p", "src/*.py",
                    "-d", temp_dir,
                ]
    err = call(" ".join(pycco_args), shell=True)
    
    if err:
        # There is a problem creating the documentation stop here
        print "Error!!"
        print err
    else:
        # Remove the existing documentation
        out = call(["rm", "-r", final_dir,])

        # rename the temporary docs dir to the docs dir
        out = call(["mv", temp_dir, final_dir,])

if __name__ == "__main__":
    
    create_pycco_docs()
    make_index_page("docs")
