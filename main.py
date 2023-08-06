from connect_database import Cursor, bd_connect
from flask import Flask, redirect, render_template, request, url_for
import cpuinfo
import platform
import wmi
import psutil

app = Flask(__name__)

my_cpuinfo = cpuinfo.get_cpu_info()
pc = wmi.WMI()
os_info = pc.Win32_OperatingSystem()[0]

Full_Name = platform.node()
Operating_System = platform.platform()
Video_controller = pc.Win32_VideoController()[0].name
Full_CPU_Name = my_cpuinfo['brand_raw']
RAM = psutil.virtual_memory().total / 1024 / 1024 / 1024
Disk = psutil.disk_usage('/').total /1000 /1000 /1000
Free_Disk = psutil.disk_usage('/').free /1000 /1000 /1000
# OPÇÕES DE ALTERAÇÃO DO DATABASE

@app.route('/')
def home():
    Cursor.execute("SELECT * FROM servidores")
    data = Cursor.fetchall() #retornamos todas as linhas obtidas na consulta para uma variável (array)
    return render_template('Servidores_Faitec.html', produtos=data)        

@app.route('/insert', methods=["POST"])
def insert_data():
    Cursor.execute(f"INSERT INTO servidores (Full_Name,Operating_System,Video_Controller, Full_CPU_Name, RAM, Disk, Free_Disk) values ('{Full_Name}','{Operating_System}','{Video_controller}','{Full_CPU_Name}','{RAM:.2f} GB','{Disk:.2f}GB','{Free_Disk:.2f}GB')")
    return redirect(url_for('home'))  

@app.route('/update', methods=["POST"])
def update_data():
    ID = request.form['id']
    Nome = request.form['nome']
    Quantidade = request.form['quantidade']
    Valor= request.form['valor']
    Cursor.execute(f"UPDATE servidores SET Nome='{Nome}', Qt='{Quantidade}', Valor='{Valor}' WHERE id = '{ID}'")
    return redirect(url_for('home'))     

@app.route('/deletar/<string:ID>', methods=["GET"])
def delete_data(ID):
    Cursor.execute(f"DELETE FROM servidores WHERE id = '{ID}'")
    return redirect(url_for('home'))     

#OUTRAS ROTAS

@app.route('/tabelas')
def teste():
        return render_template('tables.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)    