# Key Concepts
- Running the debugger
    - Run
    - Breakpoints
    - Step
    - Step into
    - Callstack
    - Exploring
- launch.json
    - File
    - Path variables
    - Args
    - Env
    - justMyCode
- Keybindings

# Example launch.json entry
```
{
    "name": "Fizz Buzz 10",
    "type": "python",
    "request": "launch",
    "program": "${workspaceFolder}/explore.py",
    "console": "integratedTerminal",
    "args": [
        "10"
    ],
    "env": {
        "AWS_PROFILE": "alaffia-dev",
        "ENV_PATH": ".env.example"
    },
    "justMyCode": false
}
```

