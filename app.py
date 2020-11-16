# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, render_template
from flask_bootstrap import Bootstrap

from config import app_config, app_active

from admin.Admin import start_views

from controller.User import UserController
from controller.Product import ProductController

config = app_config[app_active]

from flask_sqlalchemy import SQLAlchemy

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'paper'

    db = SQLAlchemy(config.APP)
    Bootstrap(app)
    db.init_app(app)

    start_views(app,db)

    @app.route('/')
    def index():
        return 'Hello World!'
    
    @app.route('/login/')
    def login():
        return render_template('login.html', message="Essa é uma mensagem que veio da rota")
    
    @app.route('/login/', methods=['POST'])
    def login_post():
        user = UserController()
        email = request.form['email']
        password = request.form['password']
        result = user.login(email, password)
        if result:
            return redirect('/admin')
        else:
            return render_template('login.html', data={'status': 401, 'msg': 'Dados de usuário incorretos', 'type': None})
    
    @app.route('/recovery-password/')
    def recovery_password():
        return 'Aqui entrará a tela de recuperar senha'
    
    @app.route('/recovery-password/', methods=['POST'])
    def send_recovery_password():
        user = UserController()
        result = user.recovery(request.form['email'])        
        if result:
            return render_template('recovery.html', data={'status': 200, 'msg': 'E-mail de recuperação enviado com sucesso'})
        else:
            return render_template('recovery.html', data={'status': 401, 'msg': 'Erro ao enviar e-mail de recuperação'})

    @app.route('/product', methods=['POST'])
    def save_products():
        product = ProductController()
        result = product.save_product(request.form)
        if result:
            message = "Inserido"
        else:
            message = "Não inserido"
        return message
    
    @app.route('/product', methods=['PUT'])
    def update_products():
        product = ProductController()
        result = product.update_product(request.form)
        if result:
            message = "Editado"
        else:
            message = "Não Editado"
        return message
    
    @app.route('/product', methods=['DELETE'])
    def delete_products():
        product = ProductController()
        result = product.delete_product(request.form)
        if result:
            message = "Deletado"
        else:
            message = "Não deletado"
        return message

    return app    