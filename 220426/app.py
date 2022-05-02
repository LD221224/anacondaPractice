from flask import Flask, request
from flask_restx import Resource, Api
from apis.todo import Todo
from apis.hello import Hello

app = Flask(__name__)
api = Api(
    app,
    version='0.1'
    )
'''
파라미터
- version: API Server의 버전을 명시합니다.
- title: API Server의 이름을 명시합니다.
- description: API Server의 설명을 명시합니다.
- terms_url: API Server의 Base Url을 명시합니다.
- contact: 제작자 E-Mail 등을 삽입합니다.
- license: API Server의 라이센스를 명시 합니다.
- license_url: API Server의 라이센스 링크를 명시 합니다.
'''

api.add_namespace(Todo, '/todos')
api.add_namespace(Hello, '/hello')  

# todos = {}

# @api.route('/hello/<string:name>')
# class HelloWorld(Resource):
#     def get(self, name):
#         return {'hello': '%s!' % name}

# @api.route('/<string:todo_id>')
# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}

#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}



if __name__ == '__main__':
    app.run(debug=True)
