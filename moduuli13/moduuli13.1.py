from flask import Flask, jsonify

app = Flask(__name__)

def onko_alkuluku(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:luku>', methods=['GET'])
def tarkista_alkuluku(luku):
    tulos = onko_alkuluku(luku)
    return jsonify({"Number": luku, "IsPrime": tulos})

if __name__ == '__main__':
    app.run(port=3000)