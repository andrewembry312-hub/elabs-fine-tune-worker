
<p align="center">
  <img src="https://pub-796a08821c1c483aaf5e274e0d03e350.r2.dev/brand/elabs-fine-tune-hero.png" alt="E-Labs Fine-Tune Worker" width="800">
</p>

# E-Labs Fine-Tune Worker

[![Runpod](https://api.runpod.io/badge/andrewembry312-hub/elabs-fine-tune-worker)](https://console.runpod.io/hub/ELABS-AI/elabs-fine-tune-worker)

Fine-tune any HuggingFace LLM on RunPod Serverless. Supports LoRA, QLoRA, DPO, SFT.

## API

```json
{
  "input": {
    "user_id": "user_abc",
    "model_id": "llama-3.2-3b",
    "run_id": "my-first-finetune",
    "credentials": {
      "wandb_api_key": "",
      "hf_token": ""
    },
    "args": {
      "base_model": "meta-llama/Llama-3.2-3B",
      "adapter": "qlora",
      "lora_r": 32,
      "datasets": [{"path": "dataset", "type": "alpaca"}],
      "num_epochs": 3,
      "learning_rate": 2e-4
    }
  }
}
```

## GPU Requirements

| GPU | VRAM | Use Case |
|-----|------|----------|
| A100 | 80GB | Full fine-tuning 13B-70B |
| L40S | 48GB | Full fine-tuning 7B models |
| RTX 6000 Ada | 48GB | Full fine-tuning 7B models |
| RTX 4090 | 24GB | QLoRA 7B-13B |
| L4 | 24GB | LoRA up to 7B |

---

Apache 2.0 — Based on [Axolotl](https://github.com/axolotl-ai-cloud/axolotl). Modifications by E-Labs AI Studio.
