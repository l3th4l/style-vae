from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

# 3rd party:
import fire
import tensorflow as tf

# different category:
from style_vae.model import StyleVae, VaeConfig
from style_vae.data import Dataset

# same category:
from style_vae.train.style_vae_trainer import StyleVaeTrainer
from style_vae.train.vae_trainer import VaeTrainerConfig


def train():
    trainer = _build_trainer()
    dataset = Dataset.get_cifar10()

    # trainer.load(save_path)
    trainer.train(dataset)
    # trainer.save(save_path)


def _build_trainer() -> StyleVaeTrainer:
    model_config = VaeConfig()
    print(model_config)

    model = StyleVae(model_config)
    trainer_config = VaeTrainerConfig()
    print(trainer_config)

    sess = tf.Session()
    trainer = StyleVaeTrainer(model, trainer_config, sess)
    return trainer


if __name__ == '__main__':
    fire.Fire(train)
