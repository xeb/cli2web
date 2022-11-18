# cli2web
---

This is the start of a utility that will generate Web UIs from simple Python CLIs. Just meant for fun. The goal is to leverage <a href="https://openai.com/blog/openai-codex/">Codex</a> for the HTML and invocation using another CLI program as an input.

## cli_process_pictures Example
In the `cli_process_pictures` example source folder, there is an existing `app.py` file. This would be the input program. Ideally someone would run:

```
$ cli2web app.py --main="process_pictures"
```

Which would call to Codex with the main method invocation (the entry point to the python program, in this case `process_pictures`) and generate the `ui.html` file and the few lines in `backend.py` for `invoke_method`. The backend.py file would be constructed and the sanic server would be started. The user would then have a working Web UI to run their CLI from a web interface without any fuss. 

## Next Steps
My goal would be to have `cli2web` generate Web UIs for all kinds of CLIs, including non-Python binaries. It would do this by reading the `--help` menus and leveraging Codex and GPT.

For now this is just an example until I get around to writing the real `cli2web` interface`