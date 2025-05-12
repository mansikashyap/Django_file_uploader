Django File Uploading Task
This project demonstrates a Django-based file uploading system that saves files both locally and to an AWS S3 bucket using the boto3 library. 
The uploaded files are stored in the local MEDIA_ROOT directory and simultaneously uploaded to an S3 using boto3.

Features
Local File Storage: Files are saved in the media directory configured in the MEDIA_ROOT setting.
AWS S3 Integration: Files are uploaded to an S3 bucket using boto3.
Database Storage: The S3 file URL is stored in the database for easy retrieval.
REST API Support: Includes serializers for user authentication and file handling.


Prerequisites
Python 3.x
Django 5.2
boto3 for AWS S3 integration
Django REST Framework for API support


How It Works
Users upload files via a form or API endpoint.
The file is saved locally in the media directory.
The file is uploaded to an S3 bucket.
The S3 URL is saved in the database.


Configuration
Add AWS credentials (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME) in settings.py.
Ensure MEDIA_ROOT is configured for local file storage.
