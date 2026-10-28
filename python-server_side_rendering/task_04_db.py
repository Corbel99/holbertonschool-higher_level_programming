#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
    items_list = data.get("items", [])
    return render_template('items.html', items=items_list)


def read_json():
    with open('products.json', 'r') as file:
        products = json.load(file)
    return products


def read_csv():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sql():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        products.append(dict(row))
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    elif source == 'sql':
        try:
            products_list = read_sql()
        except sqlite3.Error:
            return render_template('product_display.html',
                                   error="Database error")
    else:
        return render_template('product_display.html', error="Wrong source")

    product_id = request.args.get('id')
    if product_id:
        filtered = []
        for product in products_list:
            if str(product['id']) == product_id:
                filtered.append(product)
        if not filtered:
            return render_template('product_display.html',
                                   error="Product not found")
        products_list = filtered

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
