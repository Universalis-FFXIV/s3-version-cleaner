from s3_version_cleaner.config.from_file import parse_credentials_csv


def test_parsing_credentials_file():
    data = [
        "User Name,Access Key Id,Secret Access Key",
        "test-user,AAAAAAAAAAAAAAAAAAAA,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    ]
    credentials = parse_credentials_csv(data)
    assert credentials.user_name == "test-user"
    assert credentials.access_key_id == "AAAAAAAAAAAAAAAAAAAA"
    assert credentials.secret_access_key == "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
