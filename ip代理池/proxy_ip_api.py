import time

from prox_redis import Proxyredis
from sanic import Sanic,text
from sanic_cors import CORS
app = Sanic('ip')
CORS(app)
red = Proxyredis()
@app.route('/ip_get')
def erlingqi(req):
    ip =red.get_good_ip()
    print('')
    return text(ip)
def run():
    time.sleep(15)
    app.run(host='127.0.0.1',port=10086)
if __name__ == '__main__':
    run()
