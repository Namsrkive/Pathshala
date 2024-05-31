import streamlit as st
from PIL import Image

# Load images
profile_image = Image.open("assets/profile.png")
header_image = Image.open("assets/header.jpeg")

# Page configuration
st.set_page_config(
    page_title="Pathशाला - Navigating Futures",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS Styling
st.markdown("""
    <style>
        .css-1aumxhk {
            padding: 0;
        }
        .css-18e3th9 {
            padding: 0;
        }
        .css-hxt7ib {
            padding-top: 3.5rem;
        }
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem;
            background-color: #f8f9fa;
        }
        .left {
            display: flex;
            align-items: center;
        }
        .logo img {
            height: 50px;
        }
        .links a {
            margin: 0 1rem;
            text-decoration: none;
            color: #000;
            font-weight: bold;
        }
        .buttons a {
            text-decoration: none;
            color: #000;
        }
        .explore {
            text-align: center;
            padding: 2rem;
        }
        .explore h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        .explore p {
            font-size: 1.2rem;
            margin-bottom: 1rem;
        }
        .explore h3 {
            font-size: 1rem;
            margin-bottom: 2rem;
        }
        .register {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            cursor: pointer;
            border-radius: 5px;
        }
        .register:hover {
            background-color: #0056b3;
        }
        .header-image img {
            width: 100%;
            height: auto;
            margin-top: 2rem;
        }
        footer {
            background-color: #f8f9fa;
            padding: 2rem 0;
        }
        .columns {
            display: flex;
            justify-content: space-between;
        }
        .col {
            width: 23%;
        }
        .col h5 {
            margin-bottom: 1rem;
        }
        .col a {
            display: block;
            margin-bottom: 0.5rem;
            text-decoration: none;
            color: #000;
        }
        .col p {
            font-size: 0.9rem;
        }
        .social-links i {
            font-size: 1.5rem;
            margin-right: 1rem;
        }
        .copyright {
            text-align: center;
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown("""
<nav>
    <div class="left">
        <div class="logo">
            <img src="assets/profile.png">
        </div>
        <div class="links">
            <a href="#">Home</a>
            <a href="#sec1">Announcements</a>
            <a href="#">About Us</a>
            <a href="#">Contact Us</a>
        </div>
    </div>
    <div class="buttons">
        <a href="#"><i class='bx bx-user'></i></a>
    </div>
</nav>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<header>
    <div class="explore">
        <h1>Welcome to Pathशाला - Navigating Futures.</h1>
        <p>Get Carrier Guidance with Pathशala!</p>
        <h3>App specially designed to serve as a virtual guide for students navigating the complex terrain of academic choices and future career paths.</h3>
        <a href="login.html" class="button-link">
            <button class="register">Register</button>
        </a>
        <div class="header-image">
            <img src="assets/header.jpeg" alt="Your Image">
        </div>
</header>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<footer>
    <div class="columns">
        <div class="col">
            <h5>Site Links</h5>
            <a href="#">Announcements</a>
            <a href="#">About Us</a>
            <a href="#">Contact Us</a>
        </div>
        <div class="col">
            <h5>Other Pages</h5>
            <a href="#">404 Page</a>
            <a href="#">Login|Register</a>
            <a href="#">Privacy Policy</a>
        </div>
        <div class="col">
            <h5>Collaboration</h5>
            <a href="#">Work With Us</a>
            <a href="#">Affiliate</a>
            <a href="#">Support</a>
        </div>
        <div class="col last">
            <h5>About Us</h5>
            <p>"Pathशाला  - Navigating Futures" is a pioneering online educational platform developed by our dedicated team of four. Our project is designed to serve as a virtual guide for students navigating the complex terrain of academic choices and future career paths.</p>
            <div class="social-links">
                <i class='bx bxl-instagram'></i>
                <i class='bx bxl-dribbble'></i>
                <i class='bx bxl-linkedin'></i>
                <i class='bx bxl-twitter'></i>
            </div>
        </div>
    </div>
    <div class="copyright">
        <p>Copyright © 2024 Pathshala, All Rights Reserved.</p>
    </div>
</footer>
""", unsafe_allow_html=True)
