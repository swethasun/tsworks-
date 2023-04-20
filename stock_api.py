from flask import Flask, jsonify, request
import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='user', password='password',
                              host='host', database='database')
cursor = cnx.cursor()

app = Flask(__name__)

# Define route for getting all companies' stock data for a particular day
@app.route('/stockdata/date/<date>')
def get_all_stock_data_for_day(date):
    query = "SELECT * FROM stock_data WHERE date=%s"
    cursor.execute(query, (date,))
    data = cursor.fetchall()
    return jsonify(data)

#get all stock data for a particular company for a particular day
@app.route('/stockdata/company/<company_id>/date/<date>')
def get_stock_data_for_company_for_day(company_id, date):
    query = "SELECT * FROM stock_data WHERE company=%s AND date=%s"
    cursor.execute(query, (company_id, date))
    data = cursor.fetchall()
    return jsonify(data)

# get all stock data for a particular company
@app.route('/stockdata/company/<company_id>')
def get_stock_data_for_company(company_id):
    query = "SELECT * FROM stock_data WHERE company=%s"
    cursor.execute(query, (company_id,))
    data = cursor.fetchall()
    return jsonify(data)

# updating stock data for a company by date
@app.route('/stockdata/company/<company_id>/date/<date>', methods=['POST', 'PATCH'])
def update_stock_data_for_company_by_date(company_id, date):
    close = request.json['close']
    volume = request.json['volume']
    query = "UPDATE stock_data SET close=%s, volume=%s WHERE date=%s AND company=%s"
    cursor.execute(query, (close, volume, date, company_id))
    cnx.commit()
    return jsonify({"message": "Stock data updated successfully."})

# Close the connection
cnx.close()

if __name__ == '__main__':
    app.run()
