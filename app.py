from flask import Flask, request, jsonify, render_template, redirect, url_for


app = Flask(__name__)

@app.route('/pk_birthday')
def pk_birthday():
    return render_template('index.html')
    # return jsonify({"result" : "successful"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8080)