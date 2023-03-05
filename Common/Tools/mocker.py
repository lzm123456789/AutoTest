from flask import Flask, request, jsonify

# 实例化应用
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# 定义响应信息
res1 = {
    'name': 'lzm',
    'sex': '男',
    'job': '测试'
}
res2 = {
    'errcode': 0,
    'errmsg': '操作成功'
}
error = {
    'errcode': 1,
    'errmsg': '失败'
}


# 定义路由
@app.route('/mockserver', methods=['GET', 'POST'])
def mockserver():
    try:
        if request.method == 'GET':
            if request.args.get('test1') == 'a':
                return jsonify(res1)
        else:
            if request.form.get('test2') == 'b':
                return jsonify(res2)
            if request.get_json() == {"username": "lzm", "password": "123456"}:
                return jsonify(res2)
    except IOError:
        return ("Error:报错了！！！")
    else:
        return jsonify(error)


# 启动服务
app.run(host='127.0.0.1', port=80, debug=True)
