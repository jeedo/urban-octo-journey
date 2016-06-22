from git import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import subprocess
import json

app = Flask(__name__)

repo = Repo('/root/host')

format = '\'{%n  "commit": "%H",%n  "abbreviated_commit": "%h",%n  "tree": "%T",%n  "abbreviated_tree": "%t",%n  "parent": "%P",%n  "abbreviated_parent": "%p",%n  "refs": "%D",%n  "encoding": "%e",%n  "subject": "%s",%n  "sanitized_subject_line": "%f",%n  "body": "%b",%n  "commit_notes": "%N",%n  "verification_flag": "%G?",%n  "signer": "%GS",%n  "signer_key": "%GK",%n  "author": {%n    "name": "%aN",%n    "email": "%aE",%n    "date": "%aD"%n  },%n  "commiter": {%n    "name": "%cN",%n    "email": "%cE",%n    "date": "%cD"%n  }%n},\''

@app.route("/")
def showlog():
    output = subprocess.Popen(["git log --pretty=format:" + format], shell=True, stdout=subprocess.PIPE).communicate()[0]
    #return output
    output = '['+ output[:-1]+']'
    print output
    logdata = json.loads(output)
    return render_template('showlog.html', logdata=logdata)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
