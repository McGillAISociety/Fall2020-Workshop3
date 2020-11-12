from flask import Flask, render_template, request
# Import your models
from gpt2_predictor import Gpt2_predictor
from mnist_predictor import MNIST_predictor

app = Flask(__name__)

# Instantiate your models
gpt2 = Gpt2_predictor()
mnist = MNIST_predictor()


# Base endpoint to perform prediction.
@app.route('/', methods=['POST'])
def make_prediction():
    if request.form['predictor'] == 'mnist':
        prediction = mnist.predict(request)
        return render_template('index.html', prediction=prediction, generated_text=None, tab_to_show='mnist')

    elif request.form['predictor'] == 'gpt2':
        generated_text = gpt2.predict(request)
        return render_template('index.html', prediction=None, generated_text=generated_text, tab_to_show='gpt2')


@app.route('/', methods=['GET'])
def load():
    return render_template('index.html', prediction=None, generated_text=None, tab_to_show='mnist')


@app.route('/predict/image', methods=['POST'])
def make_image_prediction():
    prediction = mnist.predict(request)
    print(prediction)
    return str(prediction)


@app.route('/predict/text', methods=['POST'])
def make_text_prediction():
    prediction = gpt2.predict(request)
    return str(prediction)

if __name__ == '__main__':
    app.run(debug=True)
