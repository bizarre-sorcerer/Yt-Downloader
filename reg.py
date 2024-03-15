from flask import Flask, render_template, redirect, url_for, request
from extractor import extractVideoData
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

