# from flask import Flask, render_template, request
# from PIL import Image, ImageEnhance
# import os


# app = Flask(__name__)


# UPLOAD_FOLDER = "uploads"
# ENHANCED_FOLDER = "enhanced"


# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(ENHANCED_FOLDER, exist_ok=True)


# @app.route("/", methods=["GET", "POST"])
# def home():

#     enhanced_image = None

#     if request.method == "POST":

#         image = request.files["image"]

#         if image:

#             upload_path = os.path.join(
#                 UPLOAD_FOLDER,
#                 image.filename
#             )

#             image.save(upload_path)


#             img = Image.open(upload_path)


#             # Improve sharpness
#             sharpness = ImageEnhance.Sharpness(img)
#             img = sharpness.enhance(2)


#             # Improve contrast
#             contrast = ImageEnhance.Contrast(img)
#             img = contrast.enhance(1.5)


#             enhanced_path = os.path.join(
#                 ENHANCED_FOLDER,
#                 image.filename
#             )


#             img.save(enhanced_path)


#             enhanced_image = enhanced_path


#     return render_template(
#         "index.html",
#         enhanced_image=enhanced_image
#     )


# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, send_from_directory
from PIL import Image, ImageEnhance
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ENHANCED_FOLDER = "enhanced"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENHANCED_FOLDER, exist_ok=True)


@app.route('/enhanced/<filename>')
def enhanced_file(filename):
    return send_from_directory(ENHANCED_FOLDER, filename)


@app.route("/", methods=["GET", "POST"])
def home():

    enhanced_image = None

    if request.method == "POST":

        image = request.files.get("image")

        if image and image.filename:

            upload_path = os.path.join(
                UPLOAD_FOLDER,
                image.filename
            )

            image.save(upload_path)

            img = Image.open(upload_path)

            # Improve sharpness
            sharpness = ImageEnhance.Sharpness(img)
            img = sharpness.enhance(2)

            # Improve contrast
            contrast = ImageEnhance.Contrast(img)
            img = contrast.enhance(1.5)

            enhanced_path = os.path.join(
                ENHANCED_FOLDER,
                image.filename
            )

            img.save(enhanced_path)

            enhanced_image = image.filename

    return render_template(
        "index.html",
        enhanced_image=enhanced_image
    )


if __name__ == "__main__":
    app.run(debug=True)