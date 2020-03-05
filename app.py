# import the Flask class from the flask module
from flask import Flask, request, render_template
import re

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route("/")
def home():
    return render_template("index.html")  # return a string


@app.route("/", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        input_dict = {k: v for k, v in request.form.items()}

        if input_dict["numberInput"]:
            try:
                if input_dict["decimalSwitch"]:
                    # convert decimal to binary here and return new number
                    data = dec_2_bin_converter(input_dict["numberInput"])
            except KeyError:
                # convert binary to decimal here and return new number
                data = bin_2_dec_converter(input_dict["numberInput"])
        else:
            data = "Invalid input! Try again."
        return render_template("index.html", data=data)


def dec_2_bin_converter(num):
    binary = int(float(num))
    return bin(binary).replace("0b", "")


def bin_2_dec_converter(num):
    if re.search(r"[2-9]", num):
        return "Invalid input! Try again."
    else:
        return int(num, 2)


# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=True)
