from flask import Flask, request, render_template, send_from_directory
from DP911.Registers import Code
from DP911.Interpreter import run
from gevent import pywsgi
import sys
import os

app = Flask(__name__)


@app.route('/logo.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'Resource'),
                               'logo.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/", methods=['GET', 'POST'])
async def editor():
    if request.method == 'POST':
        code = request.form['code'].replace('\n', '\\n')

        try:
            return render_template("result.html",
                                   code=code,
                                   results_msg=run(Code.sim_storage_space(request.form['code']), web_mode=True),
                                   address=Code.sim_storage_space(request.form['code']))
        except Exception:
            return render_template("result.html",
                                   code=code,
                                   data=sys.exc_info(),
                                   address=Code.sim_storage_space(request.form['code']),
                                   mode=0)
    else:
        if str(request.args.get("code")) == "None":
            code = ""
        else:
            code = request.args.get("code").replace('\\n', '\n')

        return render_template("editor.html", code=code)


def start_server(ip='0.0.0.0', port=5000):
    server = pywsgi.WSGIServer((ip, port), app)
    server.serve_forever()
