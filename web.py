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
        try:
            return render_template("result.html",
                                   results_msg=run(Code.sim_storage_space(request.form['code']), web_mode=True),
                                   address=Code.sim_storage_space(request.form['code']))
        except Exception:
            return render_template("result.html",
                                   data=sys.exc_info(),
                                   address=Code.sim_storage_space(request.form['code']),
                                   mode=0)
    else:
        return render_template("editor.html")


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()
