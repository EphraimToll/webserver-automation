terraform {
    required_providers {
        local = {
            source  = "hashicorp/local"
            version = "~> 2.1"
        }
    }
}

provider "local" {}

resource "local_file" "json_config"{
    content = jsonencode({
        port_nginx = var.webserver_port,
        nginx_version = var.nginx_version
        protocol = var.protocol
    })
    filename = "${path.module}/${var.json_path}"
}

