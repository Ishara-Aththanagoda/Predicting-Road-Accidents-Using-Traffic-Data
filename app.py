from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json.get('inputData')
    response = f"Processed: {data.upper()}"  
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)