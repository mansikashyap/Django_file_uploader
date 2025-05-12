from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile
from django.conf import settings
import boto3 


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_instance = form.save()
            print("Uploaded file path:", uploaded_instance.file.url)
            return redirect('upload_success')
            

            s3 = boto3.client(
                's3',
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            )
            bucket_name = settings.AWS_STORAGE_BUCKET_NAME
            s3_key = f"uploads/{file.name}"

            s3.upload_file(local_file_path, bucket_name, s3_key)
                 
            return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')
