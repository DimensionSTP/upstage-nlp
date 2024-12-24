#!/bin/bash

path="src/postprocessing"
is_causal=True
is_preprocessed=True
is_tuned="untuned"
strategy="deepspeed_stage_3_offload"
upload_user="beomi"
model_type="OPEN-SOLAR-KO-10.7B"
left_padding=False
quantization_type="origin"
peft_type="origin"
data_max_length=1024
target_max_length=256
precision="bf16"
batch_size=16
model_detail="OPEN-SOLAR-KO-10.7B"

python $path/prepare_upload_all.py \
    is_causal=$is_causal \
    is_preprocessed=$is_preprocessed \
    is_tuned=$is_tuned \
    strategy=$strategy \
    upload_user=$upload_user \
    model_type=$model_type \
    left_padding=$left_padding \
    quantization_type=$quantization_type \
    peft_type=$peft_type \
    data_max_length=$data_max_length \
    target_max_length=$target_max_length \
    precision=$precision \
    batch_size=$batch_size \
    model_detail=$model_detail
