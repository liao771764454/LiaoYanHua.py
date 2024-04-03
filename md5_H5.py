from flask import Flask, render_template, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    # 渲染初始HTML页面
    return render_template('md5_H5.html')


@app.route('/encrypt', methods=['POST'])
def encrypt():
    fields = request.form.getlist('fields[]')
    original_string = ''.join(fields)

    md5_temp = hashlib.md5()
    md5_temp.update(original_string.encode("utf-8"))
    md5_result = md5_temp.hexdigest()

    # 返回JSON数据而不是渲染页面
    return jsonify({
        "original_string": original_string,
        "md5_result": md5_result
    })


if __name__ == "__main__":
    app.run(debug=True,use_reloader=False,host='0.0.0.0')