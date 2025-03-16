import pandas as pd
import streamlit as st
import ast
from bs4 import BeautifulSoup
import pickle
import requests
import re
import plotly.express as px
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
from rapidfuzz import fuzz
from rapidfuzz import process
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import os

