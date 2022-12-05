import boto3

from s3_version_cleaner.aws import delete_old_versions


def vacuum(
    keep_last: int, bucket: str, object_key: str, endpoint_url: str | None = None
):
    s3 = boto3.client("s3", endpoint_url=endpoint_url)
    delete_old_versions(s3, bucket, object_key, keep_last)
