

<p align="center">
  <img src="https://pub-796a08821c1c483aaf5e274e0d0359f7.r2.dev/brand/elabs-fine-tune-hero.png" alt="E-Labs Fine-Tune Worker" width="800">
</p>

# E-Labs Fine-Tuning — RunPod Serverless Worker

Fine-tune any HuggingFace LLM using **Axolotl** on RunPod Serverless. Supports LoRA, QLoRA, DPO, SFT, and full fine-tuning.

## Features

- **Any HuggingFace model** — fine-tune Llama, Mistral, Qwen, DeepSeek, etc.
- **Multiple adapters** — LoRA, QLoRA, DoRA, full fine-tuning
- **Objective-based** — SFT, DPO, ORPO, PPO
- **Dataset formats** — Alpaca, ShareGPT, ChatML, raw text
- **Packed training** — sample packing for efficient throughput
- **Flash Attention 2** — supported on compatible GPUs
- **Weights & Biases** — optional experiment tracking

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
| L40S | 48GB | Full fine-tuning 7B models |
| RTX 6000 Ada | 48GB | Full fine-tuning 7B models |
| RTX 4090 | 24GB | QLoRA 7B-13B, LoRA up to 7B |
| L4 | 24GB | QLoRA 7B, LoRA up to 3B |
| A100 | 80GB | Full fine-tuning 13B-70B |

## License

Apache 2.0 — E-Labs AI Studio
