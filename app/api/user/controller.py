from app import app


@app.route('/user', methods=['GET'])
def get():
    return 'fff'
