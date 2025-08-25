# weather-mcp
An MCP server to fetch weather from [OpenMeteo](https://open-meteo.com/) based on [this](https://medium.com/neoscoop/step-by-step-building-a-docker-based-mcp-from-scratch-b409da9244d0) instruction

# Running the mcp server

> **Important:** You have to build the referenced docker image first! You can use `uv run poe build-docker` for this.

To use the mcp server in VS Code, add the following to your mcp.json:
```json
...
"servers": {
    "weather_mcp": {
        "command": "docker",
        "args": [
            "run",
            "-i",
            "--rm",
            "cevaude/weather-mcp:0.1.0"
        ]
    }
},
...
```