provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket_object" "function_code" {
  name   = "function-slack-bot-3-source.zip"
  bucket = "infinite-journey-452400-functions"  
  source = "${path.root}/function-slack-bot-3.zip"
}

resource "google_cloudfunctions2_function" "function-slack-bot-3" {
  name        = "function-slack-bot-3"
  location    = var.region
  description = "Slack Bot Function"

  build_config {
    runtime    = "python39"       
    entry_point = "hello_http"    

    source {
      storage_source {
        bucket = "infinite-journey-452400-functions"
        object = google_storage_bucket_object.function_code.name
      }
    }
  }

  service_config {
    available_memory = "256M"  
    max_instance_count = 1      

    environment_variables = {
      SLACK_URL = var.slack_url
    }
  }
}

resource "google_cloud_run_service_iam_member" "public_access" {
  location = google_cloudfunctions2_function.function-slack-bot-3.location
  project  = google_cloudfunctions2_function.function-slack-bot-3.project
  service  = google_cloudfunctions2_function.function-slack-bot-3.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
