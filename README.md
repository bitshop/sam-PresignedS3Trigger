# sam-PresignedS3Trigger

There are 2 pieces to this:

sam-imageprocessor - The SAM application, this has two functions which will be deployed on an unprotected API Gateway:
* PreSign - Create a presigned URL
* trigger - Trigger when a new file has been uploaded

Upload - The upload script to test the URL published by sam build && sam deploy
