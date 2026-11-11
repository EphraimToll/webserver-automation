variable "nginx_version" {
  description = "The version of Nginx to install"
  default     = "1.28.3-2ubuntu1.12"
  type        = string
}

variable "webserver_port" {
  description = "The port on which Nginx will listen"
  default     = 80
  type        = number
 }

variable "protocol" {
  description = "The protocol to use for Nginx"
  default     = "http"
  type        = string
}


variable "json_path" {
  description = "Path to the generated JSON configuration file"
  default     = "../config.json"
  type        = string
  
}