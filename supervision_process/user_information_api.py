from flask import Flask, request, jsonify
from supervision_process.post_request import SupervisionProcess


app = Flask(__name__)


@app.route('/')
def get_user_information():
    if request.method == 'GET':
        isplay = request.args.get('isplay')
        queryType = request.args.get('queryType')
        searchID = request.args.get('searchID')
        # thisPage = request.form['thisPage']
        response = SupervisionProcess(isplay, queryType, searchID)
        result = response.paese_html()
        if result == False:
            return jsonify({
                "status": 13000,
                "data": {
                    "msg": "資料有誤，請重新輸入"
                }})
        else:
            return jsonify(result)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5100,
        debug=True
    )
