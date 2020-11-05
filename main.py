from flask import Flask, request
from stringscore import compare

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def compare_page():
    errors = ""
    if request.method == "POST":
        text1 = None
        text2 = None
        try:
            text1 = str(request.form["text1"])
            if text1 == "":
                errors += "<p>Hey now that's not fair. You entered an empty string for text1.</p>\n"
        except:
            errors += "<p>{!r} is breaking things unfortunately.</p>\n".format(request.form["text1"])
        try:
            text2 = str(request.form["text2"])
            if text2 == "":
                errors += "<p>Hey we talked about this. You entered an empty string for text2.</p>\n"
        except:
            errors += "<p>{!r} is breaking things unfortunately.</p>\n".format(request.form["text2"])

        if text1 is not None and text2 is not None and text1 != "" and text2 != "":
            result = compare(text1, text2)
            return '''
                <html>
                    <body>
                        <p>The similarity score (out of 1) is {result}</p>
                        <p><a href="/">Click here to give it another go</a>
                    </body>
                </html>
            '''.format(result=result)
            # return "Similar score is {result}".format(result=result)
    return '''
        <html>
            <body>
                {errors}
                <p>Enter your two texts:</p>
                <form method="post" action=".">
                    <p><input name="text1" /></p>
                    <p><input name="text2" /></p>
                    <p><input type="submit" value="Find Similarity Score" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)
    #return "{errors}".format(errors=errors)


if __name__ == '__main__':
    app.run()