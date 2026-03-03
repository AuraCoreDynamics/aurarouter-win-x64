# aurarouter-win-x64

**AuraRouter Windows x64 CPU Backend**

This package is a "sidecar" for **AuraRouter**. It contains the pre-compiled binary payload required to run local LLMs on Windows using the CPU.

## What's inside?
- `llama-server.exe`: Compiled for generic x64 architectures.
- `ggml-cpu-*.dll`: A collection of architecture-specific DLLs (AVX2, Zen4, Sapphire Rapids, etc.) that are dynamically loaded for maximum CPU performance.
- `libomp140.x86_64.dll`: OpenMP runtime for efficient multi-threading.

## Requirements
- **OS**: Windows 10/11 x64.
- **CPU**: Modern x64 processor (AVX2 support recommended).
- **AuraRouter**: Must be installed in the same environment.

## Usage
Simply install this package into the same virtual environment as `aurarouter`:

```bash
pip install aurarouter-win-x64
```

AuraRouter's `BinaryManager` will automatically detect this package and use it if no compatible GPU-based backend (like `aurarouter-cuda13`) is found.
