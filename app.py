from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# 🔥 CONTACT FORM FUNCTION
@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    # 👉 YAHAN APNI DETAILS DAALNI HAI
    sender = "lakshaylakii2515007@gmail.com"   # 👈 apni gmail id
    password = "kbmh paoc wzzi tmlp"  # 👈 app password

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)

    msg = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    server.sendmail(sender, sender, msg)
    server.quit()

    return "Message Sent Successfully 🚀"

if __name__ == "__main__":
    app.run(debug=True)