from flask import Flask, render_template, request, redirect
import subprocess

app = Flask(__name__)

def run(cmd):
    return subprocess.check_output(cmd, shell=True).decode()

@app.route('/')
def index():
    containers = run("docker ps -a --format '{{.Names}}|{{.Status}}'").splitlines()
    data = [c.split("|") for c in containers]
    return render_template("index.html", containers=data)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    port = request.form['port']

    run(f"""
    docker run -d --name {name} -p {port}:80 \
    -v $(pwd)/nginx/index.html:/usr/share/nginx/html/index.html \
    nginx
    """)
    return redirect('/')

@app.route('/start/<name>')
def start(name):
    run(f"docker start {name}")
    return redirect('/')

@app.route('/stop/<name>')
def stop(name):
    run(f"docker stop {name}")
    return redirect('/')

@app.route('/delete/<name>')
def delete(name):
    run(f"docker rm -f {name}")
    return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
