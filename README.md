# Image Compression Using AWS Lambda

## Overview

This project automatically compresses images uploaded to an Amazon S3 bucket using AWS Lambda and Pillow.

## Architecture

Image Upload
    ↓
S3 Input Bucket
    ↓
S3 PUT Trigger
    ↓
AWS Lambda
    ↓
Pillow
    ↓
S3 Output Bucket

## AWS Services Used

- Amazon S3
- AWS Lambda
- AWS IAM
- AWS Lambda Layers
- Amazon CloudWatch

## Project Flow

1. User uploads an image to the input S3 bucket.
2. S3 PUT event triggers the Lambda function.
3. Lambda reads the uploaded image.
4. Pillow compresses the image.
5. Lambda uploads the compressed image to the output S3 bucket.

## Lambda Layer

A Lambda Layer containing Pillow is attached to the Lambda function.

The layer contains the Pillow package required by:

```python
from PIL import Image
