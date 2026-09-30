# Image Compression Using AWS Lambda

## 📌 Project Overview

This project automatically compresses images uploaded to an Amazon S3 bucket using AWS Lambda and the Pillow library.

When an image is uploaded to the input S3 bucket, an S3 event triggers the Lambda function. The Lambda function reads the image, compresses it, and stores the compressed image in a separate output S3 bucket.

## 🏗️ Architecture

```text
User
  │
  ▼
Input S3 Bucket
  │
  │ S3 PUT Event
  ▼
AWS Lambda
  │
  │ Pillow
  ▼
Compressed Image
  │
  ▼
Output S3 Bucket
☁️ AWS Services Used
Amazon S3
AWS Lambda
AWS IAM
AWS Lambda Layers
Amazon CloudWatch
🔄 How It Works
An image is uploaded to the input S3 bucket.
The S3 PUT event automatically triggers the Lambda function.
Lambda reads the uploaded image from S3.
Pillow processes and compresses the image.
The compressed image is uploaded to the output S3 bucket.
CloudWatch is used for Lambda execution logs.
🧩 Lambda Layer

A custom Lambda Layer is used to provide the Pillow library.

The Lambda function imports Pillow using:

from PIL import Image
🐍 Lambda Function

The function uses Python to:

Read the uploaded image from S3
Process the image using Pillow
Compress the image
Upload the compressed image to the output S3 bucket
🔐 IAM Permissions

The Lambda execution role provides permissions required to:

Read objects from the input S3 bucket
Write objects to the output S3 bucket
Write Lambda execution logs to CloudWatch
📦 Project Structure
image-compression-using-lambda/
│
├── lambda_function.py
├── requirements.txt
└── README.md
🎯 Result

The process is fully automated.

Image Upload
     ↓
S3 Trigger
     ↓
Lambda
     ↓
Image Compression
     ↓
Output S3 Bucket

The compressed image is stored in the output bucket with the prefix:

compressed-
🛠️ Technologies
Python
AWS Lambda
Amazon S3
AWS IAM
AWS Lambda Layers
Pillow
CloudWatch

This README stays consistent with the project you actually built and the architecture documented in your PDF. :contentReference[oaicite:0]{index=0}

After pasting it, click **Commit changes**.

Then your GitHub repository will have the basic professional structure.
