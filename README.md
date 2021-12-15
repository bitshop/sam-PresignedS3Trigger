# sam-PresignedS3Trigger

There are 2 pieces to this:

Upload - The upload script
sam-imageprocessor - The SAM application, this has two functions:
    PreSign - Create a presigned URL
    trigger - Trigger when a new file has been uploaded

