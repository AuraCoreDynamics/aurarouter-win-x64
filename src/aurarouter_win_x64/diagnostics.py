import platform
import os
from .logging import get_logger

logger = get_logger(\"diagnostics\")

def run_diagnostic():
    \"\"\"Check CPU capabilities for optimized inference.\"\"\"
    logger.info(\"Starting CPU diagnostics...\")
    
    results = {
        \"arch\": platform.machine(),
        \"processor\": platform.processor(),
        \"system_ram_gb\": 0
    }
    
    try:
        import psutil
        results[\"system_ram_gb\"] = round(psutil.virtual_memory().total / (1024**3), 2)
        logger.debug(f\"System RAM: {results['system_ram_gb']} GB\")
    except ImportError:
        logger.warning(\"psutil not installed, RAM info unavailable.\")
        pass
        
    logger.info(f\"CPU Diagnostic complete: {results['arch']} / {results['processor']}\")
    return results
