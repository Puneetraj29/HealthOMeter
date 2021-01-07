from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np


def cancer():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)