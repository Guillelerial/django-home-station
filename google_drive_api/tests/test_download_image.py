from pathlib import Path
from uuid import uuid4

from google_drive_api import utils as google_utils


def test_download_image():
    google_service = google_utils.GoogleService()
    test_file = str(uuid4())
    google_service.download_image(test_file)
    assert Path(test_file + '.png').exists()
    Path(test_file + '.png').unlink()