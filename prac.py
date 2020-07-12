from flask import Flask, request, json

app = Flask(__name__)
Q = open('BOMBA.txt', 'w')         

with open('file.json') as f:
    file_content = f.read()
    templates = json.loads(file_content)
    
#print(templates)

@app.route('/MANYevents', methods= ["POST"])
def books():
    if request.method == "POST":
        line = ""
        for x in templates:
            line = line + "\n"
            for i,y in x.items():
                line = line + "\n" + str(i) + ": " + str(y)
        print(line)
        Q.write(line)
        Q.close()
        
        return line, 201
    else:
        return "Nothing", 404
        
if __name__ == '__main__':
    app.run()