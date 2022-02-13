provider "github" {
  token = "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"
}

resource "github_repository" "repo" {
  name        = "test"
  description = "this is test repo"
}