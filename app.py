from flask import Flask, render_template, url_for, request, jsonify,send_from_directory
import os
from ollma import model_prompt,model_prompt_vison


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER): 
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        select_option = request.form.get('select_option') 
        text_input = request.form.get('text_input')
        print(f"Selected Option: {select_option}") 

        if select_option == 'llama3.2-vision':
            file_input = request.files['file_input'] 
            # Print data to terminal 
            
            print(f"Text Input: {text_input}")

            # Handle file input 
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_input.filename) 
            file_input.save(file_path) 
        
            print(f"File saved to: {file_path}") 
            output_text = model_prompt_vison(select_option,text_input, f"{file_path}")

        #response_data = model_prompt(select_option,text_input)
        #output_image = f"/{file_path}"
        
        # Dummy response for demonstration 
        if select_option == 'llama3.2-vision':
            response_data = { 
                'output_text': f"{output_text}", 
                'output_image': url_for('uploaded_file', filename = file_input.filename)
                } 
        else:
            output_text = model_prompt(select_option,text_input)
            response_data = { 
                'output_text': f"{output_text}", 
                }
            
        return jsonify(response_data)


    return render_template('index.html')



@app.route('/uploads/<filename>') 
def uploaded_file(filename): 
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)