from flask import Flask, request, render_template, send_file
import ai_lt_sum

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', query="")

@app.route('/', methods=['POST'])
def main_post():
    query = request.form['query']
    answer = ai_lt_sum.process_query(query)
    return render_template('index.html', query=query, answer=answer)

@app.route('/style.css')
def style_css():
    return send_file('static/style.css')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  