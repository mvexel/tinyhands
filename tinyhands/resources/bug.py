from flask_restful import Resource

class BugAPI(Resource):
	def get(self, id=None):
		b = None
		if id is None:
			# Get a random bug
			return self
		else:
			pass
		return {'id': str(b.id)}

	def post(self):
		pass
