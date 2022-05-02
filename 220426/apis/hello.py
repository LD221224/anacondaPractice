from flask_restx import Resource, Namespace

Hello = Namespace('hello')  # 첫 번째

@Hello.route('')
class HelloWorld(Resource):  
    def get(self):
        return {"hello" : "world!"}, 201, {"hi":"hello"}
		
@Hello.route('/<string:name>')  # 두 번째
class HelloName(Resource):
    def get(self, name):
        return {'hello': '%s!' % name}, 201, {"hi":"hello"}