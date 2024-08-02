from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Koneksi ke MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['sales_database']

# Koleksi
customers_collection = db['customers']
products_collection = db['products']
sales_collection = db['sales']

@app.route('/')
def home():
    return render_template('base.html')

# Customer
@app.route('/customers', methods=['GET', 'POST'])
def customers():
    if request.method == 'POST':
        data = request.form.to_dict()
        customers_collection.insert_one(data)
        return redirect(url_for('customers'))
    
    customers = list(customers_collection.find())
    for customer in customers:
        customer['_id'] = str(customer['_id'])
    return render_template('customers.html', customers=customers)

@app.route('/customers/edit/<id>', methods=['GET', 'POST'])
def edit_customer(id):
    if request.method == 'POST':
        data = request.form.to_dict()
        customers_collection.update_one({'_id': ObjectId(id)}, {'$set': data})
        return redirect(url_for('customers'))
    
    customer = customers_collection.find_one({'_id': ObjectId(id)})
    if customer:
        customer['_id'] = str(customer['_id'])
        return render_template('edit_customer.html', customer=customer)
    return redirect(url_for('customers'))

@app.route('/customers/delete/<id>', methods=['GET'])
def delete_customer(id):
    customers_collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('customers'))

# Product 
@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        data = request.form.to_dict()
        data['unit_price'] = float(data['unit_price'])
        data['stock'] = int(data['stock'])
        products_collection.insert_one(data)
        return redirect(url_for('products'))
    
    products = list(products_collection.find())
    for product in products:
        product['_id'] = str(product['_id'])
    return render_template('products.html', products=products)

@app.route('/products/edit/<id>', methods=['GET', 'POST'])
def edit_product(id):
    if request.method == 'POST':
        data = request.form.to_dict()
        data['unit_price'] = float(data['unit_price'])
        data['stock'] = int(data['stock'])
        products_collection.update_one({'_id': ObjectId(id)}, {'$set': data})
        return redirect(url_for('products'))
    
    product = products_collection.find_one({'_id': ObjectId(id)})
    if product:
        product['_id'] = str(product['_id'])
        return render_template('edit_product.html', product=product)
    return redirect(url_for('products'))

@app.route('/products/delete/<id>', methods=['GET'])
def delete_product(id):
    products_collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('products'))

# Sales 
@app.route('/sales', methods=['GET', 'POST'])
def sales():
    customers = list(customers_collection.find())
    products = list(products_collection.find())
    if request.method == 'POST':
        data = request.form.to_dict()
        data['qty'] = int(data['qty'])
        customer = customers_collection.find_one({'_id': ObjectId(data['customer_id'])})
        product = products_collection.find_one({'_id': ObjectId(data['product_id'])})
        if customer and product:
            data['unit_price'] = product['unit_price']
            data['total_price'] = data['unit_price'] * data['qty']
            sales_collection.insert_one(data)
        return redirect(url_for('sales'))
    
    sales = list(sales_collection.find())
    for sale in sales:
        sale['_id'] = str(sale['_id'])
        sale['customer_name'] = customers_collection.find_one({'_id': ObjectId(sale['customer_id'])})['name']
        sale['product_name'] = products_collection.find_one({'_id': ObjectId(sale['product_id'])})['name']
    return render_template('sales.html', sales=sales, customers=customers, products=products)

@app.route('/sales/edit/<id>', methods=['GET', 'POST'])
def edit_sale(id):
    customers = list(customers_collection.find())
    products = list(products_collection.find())
    if request.method == 'POST':
        data = request.form.to_dict()
        data['qty'] = int(data['qty'])
        customer = customers_collection.find_one({'_id': ObjectId(data['customer_id'])})
        product = products_collection.find_one({'_id': ObjectId(data['product_id'])})
        if customer and product:
            data['unit_price'] = product['unit_price']
            data['total_price'] = data['unit_price'] * data['qty']
            sales_collection.update_one({'_id': ObjectId(id)}, {'$set': data})
        return redirect(url_for('sales'))
    
    sale = sales_collection.find_one({'_id': ObjectId(id)})
    if sale:
        sale['_id'] = str(sale['_id'])
        return render_template('edit_sale.html', sale=sale, customers=customers, products=products)
    return redirect(url_for('sales'))

@app.route('/sales/delete/<id>', methods=['GET'])
def delete_sale(id):
    sales_collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('sales'))

if __name__ == '__main__':
    app.run(debug=True)
