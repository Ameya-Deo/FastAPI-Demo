# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:50:32 2021

@author: ameya
"""

import boto3
import requests
#from urllib.parse import urlparse
import keys_config as keys
import cv2
import urllib.request


def flipping_image(url):
    urllib.request.urlretrieve(url, "image.jpg")
    input_image = cv2.imread('image.jpg')
    #print("input_image:.",input_image)
    #cv2.imshow('Original Image:',input_image)
    
    #Flipping Image Horizontally
    flipped_image = cv2.flip(input_image,1)
    cv2.imwrite('image.jpg',flipped_image)
    
    #cv2.imshow("Horizontal Show: ",flipped_image)   
    #cv2.waitKey()
    return flipped_image
    

def upload_file_to_aws_s3(url, file_type):
    print("File is getting executed.")
    file_url = ''
    
    #Get the connection of AWS S3 Bucket
    s3 = boto3.resource(
        's3',
        aws_access_key_id = keys.ACCESS_KEY_ID,
        aws_secret_access_key = keys.ACCESS_SECRET_KEY
    )
    
    response = requests.get(url)
    if response.status_code==200:
        #raw_data = response.content
        #url_parser = urlparse(url)
        #file_name = os.path.basename(url_parser.path)
        file_name = 'image.jpg'
        key = file_name
        flipping_image(url)
        try:
            # Write the raw data as byte in new file_name in the server
            #with open(file_name, 'wb') as new_file:
                #new_file.write(raw_data)                    
            
            # Open the server file as read mode and upload in AWS S3 Bucket.
            data = open(file_name, 'rb')
            s3.Bucket(keys.AWS_BUCKET_NAME).put_object(Key=key, Body=data, ACL='public-read')
            data.close()
            
            # Format the return URL of upload file in S3 Bucket
            file_url = 'https://%s.%s/%s' % (keys.AWS_BUCKET_NAME, keys.AWS_S3_ENDPOINT, key)
            
        except Exception as e:
            print("Error in file upload %s." % (str(e)))
        
        finally:
            # Close and remove file from Server
            #os.remove(file_name)
            print("Attachment Successfully save in S3 Bucket url %s " % (file_url))
    else:
        print("Cannot parse url")
    return file_url


#url = "https://mydemoapi.s3.us-east-2.amazonaws.com/image/Sample.jpg"
#file_type='image'
#upload_file_to_aws_s3(url, file_type)
