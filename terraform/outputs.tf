output "json_path" {
  description = "Path to the generated JSON configuration file"
  value = abspath(resource.local_file.json_config.filename)
  
}

