from markupsafe import escape
from werkzeug.utils import secure_filename
import docx
from flask import jsonify


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def save_file():
   if request.method == 'POST':
      f = request.files['file']
      #print(f.read())
      doc = docx.Document(f)
      #f.save(secure_filename(f.filename))
      objTest = []

      for para in doc.paragraphs:
         if len(para.text):
            objTest.append(para.text)
      #return 'file uploaded successfully'
      return jsonify(objTest)

if __name__ == "__main__":
    app.run()
