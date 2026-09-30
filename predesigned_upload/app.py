import boto3
import logging
from botocore.exceptions import ClientError
from botocore.config import Config
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

BUCKET_NAME = "trial-bucket270203"
REGION = "us-east-1"


def create_presigned_post(
    bucket_name,
    object_name,
    region_name,
    fields=None,
    conditions=None,
    expiration=3600,
):

    s3_client = boto3.client(
        "s3",
        region_name=region_name,
        config=Config(
            signature_version="s3v4",
            s3={"addressing_style": "virtual"},
        ),
    )

    try:
        response = s3_client.generate_presigned_post(
            bucket_name,
            object_name,
            Fields=fields,
            Conditions=conditions,
            ExpiresIn=expiration,
        )

    except ClientError as e:
        logging.error(e)
        return None

    return response


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/presigned-post")
def get_presigned_post():

    object_name = "uploads/${filename}"

    response = create_presigned_post(
        BUCKET_NAME,
        object_name,
        REGION
    )

    if response is None:
        return jsonify({"error": "Could not generate presigned POST"}), 500

    return jsonify(response)


app.run(debug=True)