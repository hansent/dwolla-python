from flask import Flask, url_for, request, redirect, render_template, session
from dwolla import DwollaClientApp, DwollaUser

app = Flask(__name__)
app.config.from_pyfile("settings.cfg", silent=True)
app.config.from_pyfile("settings.cfg.local", silent=True)

dwolla_app = DwollaClientApp(
    app.config['DWOLLA_APP_ID'],
    app.config['DWOLLA_APP_SECRET']
)

@app.route("/")
def index():
    oauth_return_url = url_for('dwolla_oauth_return', _external=True)
    scope = "balance|contacts|transactions|accountinfofull"
    login_url = dwolla_app.init_oauth_url(oauth_return_url, scope=scope)
    return render_template("index.html", login_url=login_url)

@app.route("/dwolla/oauth_return")
def dwolla_oauth_return():
    code = request.args.get("code")
    return_url = url_for('dwolla_oauth_return', _external=True)
    session['access_token'] = dwolla_app.get_oauth_token(code, return_url)
    return redirect(url_for('account'))

@app.route('/account')
def account():
    user = DwollaUser(session['access_token'])
    return render_template("account.html",
        account = user.get_account_info(),
        balance = user.get_balance(),
        transactions = user.get_transaction_list(),
        contacts = user.get_contacts(),
    )

if __name__ == "__main__":
    app.run(debug=True)

