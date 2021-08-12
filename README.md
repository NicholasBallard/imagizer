# Imagizer

This is an API offering a variety of image utility services.

Doing "stuff" with images is common for most computer users; daily for some; a make-or-break business problem for many organizations.

Imagizer comes into the "picture" (_badum tsss_) letting users perform image manipulation tasks without knowing a thing about the technical mishmash that goes into it.

From resizing an image, to running a picture through pretrained machine learning classifiers, Imagizer is here to capture the complexity and let users just get things done. 

## Features

### Resize image from a file

Upload a file, supply the downscale percentage, and returns the image in the request body.
### Resize image from URL

Resizes an image, but does not require sending the image data in the request body.

Instead, you supply the URL and the service will fetch the image from the web, then return a resized image.

### Make favicon files for website

Returns a set of favicon icon files with an explanation for how to use them and a sample HTML snippet showing how to use them.

```text
generate ico files  
blur image
partial redattion for (credit card numbers)
ml classification of image
    ref:  
        - https://cloud.google.com/vision/pricing  
    labels  
    adult content  
    dominant color  
    face detection  
    celebrity detection  
    object localization  
    crop hints  
    ocr  
        form extraction  
        text recognition  
access: google drive, onedrive, dropbox, s3  
save in s3 bucket
pro mode: all options to send to PIL.Image
chain actions (count as more than one request)
custom workload (inside container)
mri
  nibabel
  pydicom
encoding
```

## Setting Up

## Finishing Up

## Using

## Contributing