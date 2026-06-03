\"\"\"
E-Labs Fine-Tuning — RunPod Serverless Handler
Powered by Axolotl — fine-tune any HuggingFace LLM with LoRA/QLoRA/DPO/SFT.
\"\"\"

import os, runpod, yaml
from huggingface_hub._login import login

BASE_VOLUME = os.environ.get("BASE_VOLUME", "/runpod-volume")
if not os.path.exists(BASE_VOLUME):
    os.makedirs(BASE_VOLUME)
logger = runpod.RunPodLogger()

async def handler(job):
    job_id = job["id"]
    inputs = job["input"]
    run_id = inputs.get("run_id", "default_run_id")
    args = inputs.get("args", {})

    output_dir = os.path.join(BASE_VOLUME, f"fine-tuning/{run_id}")
    os.makedirs(output_dir, exist_ok=True)
    args["output_dir"] = output_dir
    args["run_name"] = run_id
    args["runpod_job_id"] = job_id

    config_path = "/workspace/config.yaml"
    os.makedirs("/workspace", exist_ok=True)
    with open(config_path, "w") as f:
        yaml.dump(args, f, default_flow_style=False)

    creds = inputs.get("credentials", {})
    if "wandb_api_key" in creds:
        os.environ["WANDB_API_KEY"] = creds["wandb_api_key"]
    if "hf_token" in creds:
        os.environ["HF_TOKEN"] = creds["hf_token"]
    if os.environ.get("HF_TOKEN"):
        login(token=os.environ["HF_TOKEN"])

    from train import train
    async for line in train(config_path):
        yield line

    yield f"Job {job_id} complete — output at {output_dir}"

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
