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

resource "google_cloudfunctions2_function_iam_binding" "default-cloudrun" {
  cloud_function = google_cloudfunctions2_function.function-slack-bot-3.name
  role           = "roles/run.invoker"
  members        = ["allUsers"]  # This makes the function public
}
