# Fork of `OpenBMB/MiniCPM-Llama3-V`

Fork of `OpenBMB/MiniCPM-Llama3-V` with example python scropt for local use.  See [OpenBMB/ollama/examples/minicpm-v2.5/README.md](https://github.com/OpenBMB/ollama/tree/minicpm-v2.5/examples/minicpm-v2.5/README.md) for more information.

## Setup

Contains forked submodules. Clone with:

```
git clone --recurse-submodules https://github.com/mikegoelzer/MiniCPM-Llama3-V.git
```

## Python setup

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

## Build `ollama`

See [OpenBMB/ollama/minicpm-v2.5/examples/minicpm-v2.5/README.md](https://github.com/OpenBMB/ollama/blob/minicpm-v2.5/examples/minicpm-v2.5/README.md) for build instructions.

## Run model `minicpm25`

In one terminal, serve the model locally on port `11435`:

```
./serve-model-minicpm25.sh
```

In another terminal, run the model you are serving:

 - Using the python script:
    ```
    cd [this directory]
    source venv/bin/activate
    ./run-model-minicpm25.py
    ```

 - Using `ollama` cli:
    ```
    OLLAMA_HOST=127.0.0.1:11435 ollama run minicpm-v2.5
    ```

- Using `curl`:
    ```
    curl http://localhost:11435/api/generate -d '{
        "model": "minicpm-v2.5",
        "prompt": "Why is the sky blue?",
        "options": {
            "num_ctx": 4096
        }
    }'
    ```

