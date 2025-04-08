# Noodle Wire

A FastAPI-based graph processing service that accepts and processes graph data.

## Overview
Noodle Wire is a service that provides various graph processing operations through a REST API. The service accepts JGF formatted data and performs requested operations such as graph partitioning and spectral drawing.

## Features
- Graph data processing using JGF (JSON Graph Format) specification
- Supported operations:
  - Graph partitioning
  - Spectral drawing
- RESTful API endpoints
- Error handling and validation using Pydantic models

## Getting Started

### Prerequisites
- Python 3.x
- FastAPI
- Pydantic

### Running the Server
The server can be started with:
```bash
fastapi dev main.py
```

## API Usage

### Request Format
Requests should follow this structure:
```json
{
    "graph": {
        "directed": boolean,
        "label": string,
        "nodes": {
            "node_id": {
                "label": string,
                "metadata": {}
            }
        },
        "edges": [
            {
                "source": string,
                "target": string,
                "metadata": {
                    "weight": integer
                }
            }
        ]
    },
    "metadata": {
        "data_process_operation": {
            "name": string,
            "parameters": {}
        }
    }
}

```

## Technical Details
- Built with FastAPI for high-performance async API handling
- Uses Pydantic models for request validation
- Implements JGF specification for standardized graph data representation
- Modular architecture with separate routing and operation handling
