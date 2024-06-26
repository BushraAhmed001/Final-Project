from flask import Flask, Blueprint, redirect, render_template, url_for, request
from .models import Overview
from . import db
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from io import BytesIO
import base64
app = Flask(__name__, static_url_path='/static')

feature = Blueprint("feature", __name__)

def base_to_frame(db_query):
    if len(db_query) > 0:
        df = pd.DataFrame([(
            i.id,
            i.db_total_income,
            i.db_highest_spend,
            i.db_bestseller,
            i.db_worstseller,
            i.db_mvp

        )for i in db_query],columns=["id",
                                        "total_income",
                                        "highest_spend",
                                        "best_seller",
                                        "worst_seller",
                                        "mvp"  ])
        return df


@feature.route("/")
def home():
    overview_list = Overview.query.all()    # returns list of objects
    overview = Overview.query.all()
    if overview:
        df = base_to_frame(overview)
        er_message = request.args.get("er_message", None)
        # df = pd.read_sql(Overview.query.all())
        max_total_income = df['total_income'].sum()
        max_highest_spend = df["highest_spend"].max()
        mode_bestseller = df["best_seller"].mode()[0]
        mode_worst_seller = df["worst_seller"].mode()[0]
        mode_mvp = df["mvp"].mode()[0]
        s = df["total_income"]
        x = df["id"]
        plt.style.use('ggplot')
        plt.figure(figsize=(9,7)) 
        plt.plot()
        plt.title("Total Income by Day")
        plt.xlabel("Day")
        plt.ylabel("Total Income")
        plt.tight_layout()
        plt.savefig('./website/static/images/my_plot.png')

        return render_template("home.html",
                            max_total_income=max_total_income,
                            max_highest_spend=max_highest_spend,
                            mode_bestseller=mode_bestseller,
                            mode_worst_seller=mode_worst_seller,
                            mode_mvp=mode_mvp,
                            # overview_list = overview_list,
                            er_message=er_message)
    else:
        return render_template("home.html")


@feature.route("/add", methods = ["POST", "GET"])
def add():
    try:
        # request form contents by 'name' of form - task
        db_day = request.form.get("day") 
        db_total_income = request.form.get("total_income")
        db_highest_spend = request.form.get("highest_spend")
        db_bestseller = request.form.get("best_selling_item")
        db_worstseller = request.form.get("least_selling_item")
        db_mvp = request.form.get("mvp")
        new_overview = Overview(db_total_income = db_total_income,
                                db_highest_spend=db_highest_spend,
                                db_bestseller= db_bestseller,
                                db_worstseller=db_worstseller,
                                db_mvp=db_mvp,
                                db_day=db_day
                                )
        db.session.add(new_overview)
        db.session.commit()
        return redirect(url_for("feature.home"))
    except:
        er_message = "There was an error adding your item"
        return redirect(url_for("feature.home", er_message=er_message))
 
    
    
@feature.route("/mon")
def mon():
    # mon_income = df["total_income"][0]
    # overview = Overview.query.all()
    monday_data = Overview.query.filter_by(db_day="Monday").first() 
    if monday_data:
        income = monday_data.db_total_income
        highest_spend = monday_data.db_highest_spend
        best_seller = monday_data.db_bestseller
        worst_seller = monday_data.db_worstseller
        mvp = monday_data.db_mvp
        # print(df)
        # print(income)
        return render_template("mon.html",
                                income=income,
                                highest_spend=highest_spend,
                                best_seller=best_seller,
                                worst_seller=worst_seller,
                                mvp=mvp)
    else:
        return render_template("mon.html")
                                
                            # best_seller=best_seller,
                            # worst_seller=worst_seller)
                            # mvp=mvp)
    
@feature.route("/tues")
def tues():
    # mon_income = df["total_income"][0]
    # overview = Overview.query.all()
    tuesday_data = Overview.query.filter_by(db_day="Tuesday").first() 
    if tuesday_data:
        income = tuesday_data.db_total_income
        highest_spend = tuesday_data.db_highest_spend
        best_seller = tuesday_data.db_bestseller
        worst_seller = tuesday_data.db_worstseller
        mvp = tuesday_data.db_mvp
        # print(df)
        # print(income)
        return render_template("tues.html",
                                income=income,
                                highest_spend=highest_spend,
                                best_seller=best_seller,
                                worst_seller=worst_seller,
                                mvp=mvp)
    else:
        return render_template("tues.html")
                                






# @feature.route("/tues")
# def tues():
#     overview = Overview.query.all()
#     exists = Overview.query.filter_by(id=2).first() is not None
#     if exists:
#         df = base_to_frame(overview)
#         income = df["total_income"][1]
#         highest_spend = df["highest_spend"][1]
#         best_seller = df["best_seller"][1]
#         worst_seller = df["worst_seller"][1]
#         mvp = df["mvp_staff"][1]
#         # print(df)
#         # print(income)
#         return render_template("tues.html",
#                                 income=income,
#                                 highest_spend=highest_spend,
#                                 best_seller=best_seller,
#                                 worst_seller=worst_seller,
#                                 mvp=mvp)
#     else:
#         return render_template("tues.html")
                            
@feature.route("/wed")
def wed():
    # mon_income = df["total_income"][0]
    # overview = Overview.query.all()
    wednesday_data = Overview.query.filter_by(db_day="Wednesday").first() 
    if wednesday_data:
        income = wednesday_data.db_total_income
        highest_spend = wednesday_data.db_highest_spend
        best_seller = wednesday_data.db_bestseller
        worst_seller = wednesday_data.db_worstseller
        mvp = wednesday_data.db_mvp
        # print(df)
        # print(income)
        return render_template("wed.html",
                                income=income,
                                highest_spend=highest_spend,
                                best_seller=best_seller,
                                worst_seller=worst_seller,
                                mvp=mvp)
    else:
        return render_template("wed.html")
# @feature.route("/wed")
# def wed():
#     overview = Overview.query.all()
#     exists = Overview.query.filter_by(id=3).first() is not None
#     if exists:
#         df = base_to_frame(overview)
#         income = df["total_income"][2]
#         highest_spend = df["highest_spend"][2]
#         best_seller = df["best_seller"][2]
#         worst_seller = df["worst_seller"][2]
#         mvp = df["mvp_staff"][2]
#         # print(df)
#         # print(income)
#         return render_template("wed.html",
#                                 income=income,
#                                 highest_spend=highest_spend,
#                                 best_seller=best_seller,
#                                 worst_seller=worst_seller,
#                                 mvp=mvp)
#     else:
#         return render_template("wed.html")
    
@feature.route("/thurs")
def thurs():
    # mon_income = df["total_income"][0]
    # overview = Overview.query.all()
    thursday_data = Overview.query.filter_by(db_day="Thursday").first() 
    if thursday_data:
        income = thursday_data.db_total_income
        highest_spend = thursday_data.db_highest_spend
        best_seller = thursday_data.db_bestseller
        worst_seller = thursday_data.db_worstseller
        mvp = thursday_data.db_mvp
        # print(df)
        # print(income)
        return render_template("thurs.html",
                                income=income,
                                highest_spend=highest_spend,
                                best_seller=best_seller,
                                worst_seller=worst_seller,
                                mvp=mvp)
    else:
        return render_template("thurs.html")
    
# @feature.route("/thurs")
# def thurs():
#     overview = Overview.query.all()
#     exists = Overview.query.filter_by(id=4).first() is not None
#     if exists:
#         df = base_to_frame(overview)
#         income = df["total_income"][3]
#         highest_spend = df["highest_spend"][3]
#         best_seller = df["best_seller"][3]
#         worst_seller = df["worst_seller"][3]
#         mvp = df["mvp_staff"][3]
#         # print(df)
#         # print(income)
#         return render_template("thurs.html",
#                                 income=income,
#                                 highest_spend=highest_spend,
#                                 best_seller=best_seller,
#                                 worst_seller=worst_seller,
#                                 mvp=mvp)
#     else:
#         return render_template("thurs.html")

@feature.route("/fri")
def fri():
    # mon_income = df["total_income"][0]
    # overview = Overview.query.all()
    friday_data = Overview.query.filter_by(db_day="Friday").first() 
    if friday_data:
        income = friday_data.db_total_income
        highest_spend = friday_data.db_highest_spend
        best_seller = friday_data.db_bestseller
        worst_seller = friday_data.db_worstseller
        mvp = friday_data.db_mvp
        # print(df)
        # print(income)
        return render_template("fri.html",
                                income=income,
                                highest_spend=highest_spend,
                                best_seller=best_seller,
                                worst_seller=worst_seller,
                                mvp=mvp)
    else:
        return render_template("fri.html")
# @feature.route("/fri")
# def fri():
#     overview = Overview.query.all()
#     exists = Overview.query.filter_by(id=5).first() is not None
#     if exists:
#         df = base_to_frame(overview)
#         income = df["total_income"][4]
#         highest_spend = df["highest_spend"][4]
#         best_seller = df["best_seller"][4]
#         worst_seller = df["worst_seller"][4]
#         mvp = df["mvp_staff"][4]
#         # print(df)
#         # print(income)
#         return render_template("fri.html",
#                                 income=income,
#                                 highest_spend=highest_spend,
#                                 best_seller=best_seller,
#                                 worst_seller=worst_seller,
#                                 mvp=mvp)
#     else:
#         return render_template("fri.html")
@feature.route("/sat")
def sat():
    # mon_income = df["total_income"][0]
    # overview = Overview.query.all()
    saturday_data = Overview.query.filter_by(db_day="Saturday").first() 
    if saturday_data:
        income = saturday_data.db_total_income
        highest_spend = saturday_data.db_highest_spend
        best_seller = saturday_data.db_bestseller
        worst_seller = saturday_data.db_worstseller
        mvp = saturday_data.db_mvp
        # print(df)
        # print(income)
        return render_template("sat.html",
                                income=income,
                                highest_spend=highest_spend,
                                best_seller=best_seller,
                                worst_seller=worst_seller,
                                mvp=mvp)
    else:
        return render_template("sat.html")

# @feature.route("/sat")
# def sat():
#     overview = Overview.query.all()
#     exists = Overview.query.filter_by(id=6).first() is not None
#     if exists:
#         df = base_to_frame(overview)
#         income = df["total_income"][5]
#         highest_spend = df["highest_spend"][5]
#         best_seller = df["best_seller"][5]
#         worst_seller = df["worst_seller"][5]
#         mvp = df["mvp_staff"][5]
#         # print(df)
#         # print(income)
#         return render_template("sat.html",
#                                 income=income,
#                                 highest_spend=highest_spend,
#                                 best_seller=best_seller,
#                                 worst_seller=worst_seller,
#                                 mvp=mvp)
#     else:
#         return render_template("sat.html")
@feature.route("/sun")
def sun():
    # mon_income = df["total_income"][0]
    # overview = Overview.query.all()
    sunday_data = Overview.query.filter_by(db_day="Sunday").first() 
    if sunday_data:
        income = sunday_data.db_total_income
        highest_spend = sunday_data.db_highest_spend
        best_seller = sunday_data.db_bestseller
        worst_seller = sunday_data.db_worstseller
        mvp = sunday_data.db_mvp
        # print(df)
        # print(income)
        return render_template("sun.html",
                                income=income,
                                highest_spend=highest_spend,
                                best_seller=best_seller,
                                worst_seller=worst_seller,
                                mvp=mvp)
    else:
        return render_template("sun.html")
# @feature.route("/sun")
# def sun():
#     overview = Overview.query.all()
#     exists = Overview.query.filter_by(id=7).first() is not None
#     if exists:
#         df = base_to_frame(overview)
#         income = df["total_income"][6]
#         highest_spend = df["highest_spend"][6]
#         best_seller = df["best_seller"][6]
#         worst_seller = df["worst_seller"][6]
#         mvp = df["mvp_staff"][6]
#         # print(df)
#         # print(income)
#         return render_template("sun.html",
#                                 income=income,
#                                 highest_spend=highest_spend,
#                                 best_seller=best_seller,
#                                 worst_seller=worst_seller,
#                                 mvp=mvp)
#     else:
#         return render_template("sun.html")
