import requests
import json

url = "https://stablediffusionapi.com/api/v3/text2img"

def convert_txt_to_img_url(caption):
    payload = json.dumps({
        "key": "PLBlV1sTv2AtRcRmquFs58W1Iv5qbGdo19KzYpPnBgYXvuc2RYMydtORPUPg",
        "prompt": caption,
        "negative_prompt": None,
        "width": "512",
        "height": "512",
        "samples": "1",
        "num_inference_steps": "20",
        "seed": None,
        "guidance_scale": 7.5,
        "safety_checker": "yes",
        "multi_lingual": "no",
        "panorama": "no",
        "self_attention": "no",
        "upscale": "no",
        "embeddings_model": None,
        "webhook": None,
        "track_id": None
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_data = json.loads(response.text)
    return response_data['output'][0]
