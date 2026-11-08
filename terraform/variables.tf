variable "nginx_version" {
  description = "The version of Nginx to install"
  default     = "1.28.3"
  type        = string
}

variable "port" {
  description = "The port on which Nginx will listen"
  default     = 80
  type        = number
}

variable "protocol" {
  description = "The protocol to use for Nginx"
  default     = "http"
  type        = string
}