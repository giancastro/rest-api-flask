
from config import *


@app.route('/api/get/table', methods=['GET'])
def get_table():
    cols, rs = con.query("select * from public.money_control")
    return query.export(cols, rs)


@app.route('/api/get/lenders', methods=['GET'])
def get_lenders():
    cols, rs = con.query(
        "SELECT DISTINCT lender from public.money_control ORDER BY lender")
    return query.export(cols, rs)


@app.route('/api/get/lender', methods=['GET'])
def get_lender():
    lender = request.args.get('lender')

    if lender:
        params = {"lender": lender}
        cols, rs = con.query(
            "SELECT * from public.money_control where lender='{lender}'".format(**params))
        return query.export(cols, rs)
    else:
        return Response("Please enter the lender.", status=400)


@app.route('/api/get/balance', methods=['GET'])
def get_balance():
    lender = request.args.get('lender')

    if lender:
        params = {"lender": lender}
        cols, rs = con.query(
            """
            select 
                COALESCE(lender.sum,0) - COALESCE(borrower.sum,0) as balance
            from
                (select sum(amount) from public.money_control where lender='{lender}') as lender 
            CROSS JOIN
                (select sum(amount) from public.money_control where borrower='{lender}') as borrower
            """.format(**params))
        return query.export(cols, rs)
    else:
        return Response("Please enter the lender.", status=400)


@app.route('/api/post/add', methods=['POST'])
def add_user():
    lender = request.args.get('lender')
    borrower = request.args.get('borrower')
    amount = request.args.get('amount')

    if lender and borrower and amount:
        params = {
            "lender": lender,
            "borrower": borrower,
            "amount": amount
        }
        con.execute(
            "INSERT INTO public.money_control (lender, borrower, amount) VALUES ('{lender}','{borrower}',{amount})".format(**params))
        return Response("Data sent successfully.", status=200)
    else:
        return Response("Please enter the lender, borrower and amount data.", status=400)


app.run()
