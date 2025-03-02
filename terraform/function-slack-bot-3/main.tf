provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket_object" "function_code" {
  name   = "function-slack-bot-3-source.zip"
  bucket = "infinite-journey-452400-functions"  
  source = "${path.root}/function-slack-bot-3.zip"
}

resource "google_cloudfunctions_function" "function-slack-bot-3" {
  name        = "function-slack-bot-3"
  runtime     = "python39"
  region      = var.region
  entry_point = "hello_http"
  source_archive_bucket = "infinite-journey-452400-functions"  # Bucket existente
  source_archive_object = google_storage_bucket_object.function_code.name
  trigger_http = true
  available_memory_mb = 256

  environment_variables = {
    SLACK_URL = var.slack_url
  }
}
