from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    for letter in name1:
        if letter in name2:
            name1 = name1.replace(letter, "", 1)
            name2 = name2.replace(letter, "", 1)
    
    combined_length = len(name1) + len(name2)
    
    categories = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    while len(categories) > 1:
        index = combined_length % len(categories) - 1
        if index >= 0:
            categories = categories[index + 1:] + categories[:index]
        else:
            categories = categories[:len(categories) - 1]
    
    return categories[0]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/flames', methods=['POST'])
def play_flames():
    if request.method == 'POST':
        name1 = request.form['name1']
        name2 = request.form['name2']
        result = calculate_flames(name1, name2)
        return render_template('result.html', name1=name1, name2=name2, result=result)

if __name__ == "__main__":
    app.run(debug=True)
