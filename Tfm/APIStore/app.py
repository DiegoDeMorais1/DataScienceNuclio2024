from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, jsonify, render_template, send_from_directory, request
from marshmallow import Schema, fields
from werkzeug.utils import secure_filename
import modelStore

# Cria o app
app = Flask(__name__, template_folder='./swagger/templates')

# Cria rota para o caminho inicial
@app.route('/')
def hello_world():
    return 'API Store'

# Cria as configurações do APISpec
spec = APISpec(
    title='Store API',
    version='1.0.0',
    openapi_version='3.0.2',
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)
# Informa onde está o arquivo de configuração do swagger
@app.route('/api/swagger.json')
def create_swagger_spec():
    return jsonify(spec.to_dict())

# Cria a classe para resposta com sucesso - 200
class TodoResponseSchema(Schema):
    storeName = fields.Str()
    productName = fields.Str()
    stoke = fields.List(fields.Tuple((fields.Str(), fields.Float())))

# Cria a classe para resposta com falha - 404
class NotFoundResponseSchema(Schema):
    message = fields.Str()

# Classe responsavel para gerar a lista de retorno de sucesso
class TodoListResponseSchema(Schema):
    storeProduct = fields.List(fields.Nested(TodoResponseSchema))

# Faz a busca pelos parametros recebidos da api no dataframe
def retrieve_value_from_dataframe(store_name, product_name):
    product_store = product_name + "_" + store_name

    forecast = modelStore.model(product_store)

    return forecast

# Cria uma rota par a api chamada 'predict'
@app.route('/predict')
def todo():
    # Configura a parte visual do swagger: Parameters e Response
    """
    Get List of predict
    ---

    get:
        parameters:
            - in: query
              name: storeName
              required: true
              schema:
                  type: string
              description: Name of the store
            - in: query
              name: productName
              required: true
              schema:
                  type: string
              description: Name of the product

        description: Get List of predicts
        responses:
            200:
                description: Return a predict
                content:
                    application/json:
                        schema: TodoListResponseSchema
            404:
                description: Store or product not found
                content:
                    application/json:
                        schema: NotFoundResponseSchema
        """
    # Recebe os valores repassados na API
    store_name = request.args.get('storeName')
    product_name = request.args.get('productName')

    # Pesquisa o valor de parametro no dataframe
    forcast_list = retrieve_value_from_dataframe(store_name, product_name)

    # Caso não existe, retorna msg e um 404
    if (forcast_list is None):
        return jsonify({"message": "Store or product not found"}), 404

    listValue = []
    i = 1
    for values_list in forcast_list:
        for value in values_list:
            listValue.append(
                (
                    "Day " + str(i),
                    round(float(value),2)
                )
            )
            i += 1
        break

    # Cria um valor de json para resposta com sucesso - 200
    dummy_data = [{
        'storeName': store_name,
        'productName': product_name,
        'stoke': listValue
    }]

    # Envia a resposta
    ret = TodoListResponseSchema().dump({'storeProduct': dummy_data})
    return ret


with app.test_request_context():
    spec.path(view=todo)


@app.route('/docs')
@app.route('/docs/<path:path>')
def swagger_docs(path=None):
    if not path or path == 'index.html':
        return render_template('index.html', base_url='/docs')
    else:
        return send_from_directory('./swagger/static', secure_filename(path))


if __name__ == '__main__':
    app.run(debug=True)


