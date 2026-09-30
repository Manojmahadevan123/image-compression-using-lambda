import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

OUTPUT_BUCKET = "output-bucket-m4"

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    image_content = response['Body'].read()

    image = Image.open(io.BytesIO(image_content))

    buffer = io.BytesIO()

    image.save(
        buffer,
        "JPEG",
        quality=50
    )

    buffer.seek(0)

    s3.put_object(
        Bucket=OUTPUT_BUCKET,
        Key="compressed-" + key,
        Body=buffer,
        ContentType='image/jpeg'
    )

    return "Success"
