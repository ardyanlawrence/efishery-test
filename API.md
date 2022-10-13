{
  "openapi": "3.0.0",
  "info": {
    "title": "Sensor Node",
    "description": "Sensor Node",
    "version": "0.1.1"
  },
  "servers": [
    {
      "url": "https://api.example.com/v1",
      "description": "Deskripsi mengenai Base URL."
    }
  ],
  "paths": {
    "/connect_bl": {
      "get": {
        "summary": "Connect to Sensor Node",
        "description": "Deskripsi endpoint.",
        "responses": {
          "200": {
            "description": "Bluetooth Connected"
          }
        }
      }
    },
    "/disconnect_bl": {
      "get": {
        "summary": "Disonnect from Sensor Node",
        "description": "Deskripsi endpoint.",
        "responses": {
          "200": {
            "description": "Bluetooth Disonnected"
          }
        }
      }
    },
    "/data_stream": {
      "get": {
        "summary": "Get Data from Sensor Node",
        "description": "Deskripsi endpoint.",
        "responses": {
          "200": {
            "description": "Data Streamed to HTTP"
          }
        }
      }
    }
  }
}