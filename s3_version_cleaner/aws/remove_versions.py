from typing import Any

# This came from ChatGPT, not tested yet
def delete_old_versions(s3: Any, bucket_name: str, key: str, n: int):
    """Deletes all but the most recent N object versions in an S3 bucket.

    Args:
        s3 (boto3.client or boto3.resource): The S3 client or resource.
        bucket_name (str): The name of the S3 bucket where the object versions are stored.
        key (str): The key of the object for which you want to delete old versions.
        n (int): The number of most recent object versions that you want to keep.
    """
    # List all object versions
    versions = s3.list_object_versions(Bucket=bucket_name, Prefix=key)

    # Delete all but the most recent N object versions
    for version in versions["Versions"][n:]:
        s3.delete_object(Bucket=bucket_name, Key=key, VersionId=version["VersionId"])

    # Delete all but the most recent N versions in the delete marker list
    for marker in versions["DeleteMarkers"][n:]:
        s3.delete_object(Bucket=bucket_name, Key=key, VersionId=marker["VersionId"])
