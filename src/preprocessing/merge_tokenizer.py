import dotenv

dotenv.load_dotenv(
    override=True,
)

import os

from transformers import AutoTokenizer
import sentencepiece as spm

import hydra
from omegaconf import DictConfig


@hydra.main(
    config_path="../../configs/",
    config_name="huggingface.yaml",
)
def merge_tokenizer(
    config: DictConfig,
) -> None:
    tokenizer = AutoTokenizer.from_pretrained(config.pretrained_model_name)

    sp = spm.SentencePieceProcessor()
    sp.load(f"{config.connected_dir}/data/sentencepiece/{config.dataset_name}.model")

    new_tokens = []
    for idx in range(sp.get_piece_size()):
        token = sp.id_to_piece(idx)
        if token not in tokenizer.get_vocab():
            new_tokens.append(token)

    eda_tokens = [
        "#Person1#",
        "#Person2#",
        "#Person3#",
        "#Person4#",
        "#Person5#",
        "#Person6#",
        "#Person7#",
        "#PhoneNumber#",
        "#Address#",
        "#PassportNumber#",
        "#CardNumber#",
        "#Email#",
        "#SSN#",
        "#DateOfBirth#",
    ]
    for eda_token in eda_tokens:
        if eda_token not in new_tokens and eda_token not in tokenizer.get_vocab():
            new_tokens.append(eda_token)

    tokenizer.add_tokens(new_tokens)

    os.makedirs(
        config.custom_data_encoder_path,
        exist_ok=True,
    )
    tokenizer.save_pretrained(config.custom_data_encoder_path)


if __name__ == "__main__":
    merge_tokenizer()
