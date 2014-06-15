

class JSONHelper(object):
    """ Helper class for generating JSON response."""

    def __init__(self):
        pass

    def jsonify_response(self, status, result_key, result):

        json = {
                'status' : status,
                'body':
                    {
                      result_key : result
                     }
                }
        return json
